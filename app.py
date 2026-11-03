import base64
import json
import os
import time
from functools import wraps

from dotenv import load_dotenv
from flask import Flask, abort, jsonify, render_template, request, session
from supabase import create_client
from werkzeug.exceptions import HTTPException

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "cambia-esto-en-produccion")
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax")

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

class SesionExpirada(Exception):
    pass


def _exp(token):
    """Lee la fecha de expiración del JWT (sin verificarlo; Supabase lo verifica)."""
    try:
        p = token.split(".")[1]
        p += "=" * (-len(p) % 4)
        return json.loads(base64.urlsafe_b64decode(p))["exp"]
    except Exception:
        return 0


def db():
    """Cliente de Supabase con el token del usuario: las reglas RLS aplican sus permisos."""
    if "token" not in session:
        raise SesionExpirada()
    if _exp(session["token"]) - time.time() < 60:  # renueva el token antes de que venza
        try:
            r = create_client(URL, KEY).auth.refresh_session(session["refresh"])
            session["token"] = r.session.access_token
            session["refresh"] = r.session.refresh_token
        except Exception:
            raise SesionExpirada()
    client = create_client(URL, KEY)
    client.postgrest.auth(session["token"])
    return client


def requiere_rol(*roles):
    """Protege una ruta: exige sesión y, opcionalmente, ciertos roles."""
    def decorador(fn):
        @wraps(fn)
        def envoltura(*args, **kwargs):
            if "token" not in session:
                return jsonify(error="Inicia sesión"), 401
            if roles and session.get("rol") not in roles:
                return jsonify(error="No tienes permiso para esta acción"), 403
            return fn(*args, **kwargs)
        return envoltura
    return decorador


def body():
    return request.get_json(silent=True) or {}


def solo(d, campos):
    """Toma solo los campos permitidos y convierte '' en None."""
    return {k: (None if d.get(k) == "" else d.get(k)) for k in campos if k in d}


def temporada_de(c, fecha):
    t = (c.table("temporadas").select("id")
         .lte("fecha_inicio", fecha).gte("fecha_fin", fecha).limit(1).execute().data)
    return t[0]["id"] if t else None


def traducir(msg):
    m = msg.lower()
    if "duplicate key" in m or "unique" in m:
        return "Ya existe un registro igual (matrícula, entrenamiento o asistencia repetidos)."
    if "row-level security" in m:
        return "No tienes permiso para esta acción."
    if "foreign key" in m:
        return "Referencia inválida."
    return msg


@app.errorhandler(Exception)
def errores(e):
    if isinstance(e, HTTPException):
        return jsonify(error=e.description), e.code
    msg = str(getattr(e, "message", None) or e)
    if isinstance(e, SesionExpirada) or "JWT" in msg:
        session.clear()
        return jsonify(error="Sesión expirada, vuelve a iniciar sesión"), 401
    return jsonify(error=traducir(msg)), 400

@app.get("/")
def inicio():
    return render_template("index.html")


def perfil_actual():
    p = (db().table("perfiles").select("rol,nombre,jugador_id")
         .eq("id", session["user_id"]).single().execute().data)
    session["rol"] = p["rol"]
    return p


@app.post("/api/login")
def login():
    d = body()
    try:
        r = create_client(URL, KEY).auth.sign_in_with_password(
            {"email": (d.get("email") or "").strip(), "password": d.get("password") or ""}
        )
    except Exception:
        return jsonify(error="Correo o contraseña incorrectos"), 401
    session.clear()
    session["token"] = r.session.access_token
    session["refresh"] = r.session.refresh_token
    session["user_id"] = r.user.id
    return jsonify(perfil_actual())


@app.post("/api/registro")
def registro():
    d = body()
    try:
        create_client(URL, KEY).auth.sign_up({
            "email": (d.get("email") or "").strip(),
            "password": d.get("password") or "",
            "options": {"data": {"nombre": d.get("nombre")}},
        })
    except Exception as e:
        return jsonify(error=str(getattr(e, "message", e))), 400
    return jsonify(mensaje="Cuenta creada. Si te piden confirmar el correo, hazlo y luego inicia sesión. "
                           "El entrenador te asignará tu rol.")


@app.post("/api/logout")
def logout():
    session.clear()
    return jsonify(ok=True)


@app.get("/api/me")
@requiere_rol()
def me():
    return jsonify(perfil_actual())


@app.get("/api/catalogos")
@requiere_rol()
def catalogos():
    c = db()
    return jsonify(
        ramas=c.table("ramas").select("*").order("id").execute().data,
        posiciones=c.table("posiciones").select("*").order("id").execute().data,
        temporadas=c.table("temporadas").select("*").order("fecha_inicio", desc=True).execute().data,
    )

CAMPOS_JUGADOR = ["nombre", "apellidos", "matricula", "carrera", "rama_id", "posicion_id"]


@app.get("/api/jugadores")
@requiere_rol("entrenador", "capitan", "coordinacion")
def jugadores():
    q = db().table("jugadores").select("*, ramas(nombre), posiciones(nombre)").order("apellidos")
    if request.args.get("rama_id"):
        q = q.eq("rama_id", request.args["rama_id"])
    if request.args.get("estado"):
        q = q.eq("estado", request.args["estado"])
    return jsonify(q.execute().data)


@app.post("/api/jugadores")
@requiere_rol("entrenador")
def crear_jugador():
    r = db().table("jugadores").insert(solo(body(), CAMPOS_JUGADOR)).execute()
    return jsonify(r.data[0]), 201


@app.put("/api/jugadores/<id>")
@requiere_rol("entrenador")
def editar_jugador(id):
    r = db().table("jugadores").update(solo(body(), CAMPOS_JUGADOR)).eq("id", id).execute()
    return jsonify(r.data)


@app.post("/api/jugadores/<id>/baja")
@requiere_rol("entrenador")
def dar_de_baja(id):
    motivo = body().get("motivo") or None
    r = db().table("jugadores").update({"estado": "baja", "motivo_baja": motivo}).eq("id", id).execute()
    return jsonify(r.data)


@app.post("/api/jugadores/<id>/reactivar")
@requiere_rol("entrenador")
def reactivar(id):
    r = db().table("jugadores").update({"estado": "activo"}).eq("id", id).execute()
    return jsonify(r.data)

@app.get("/api/entrenamientos")
@requiere_rol("entrenador", "capitan")
def entrenamientos():
    q = (db().table("entrenamientos").select("*")
         .order("fecha", desc=True).order("hora", desc=True).limit(60))
    if request.args.get("rama_id"):
        q = q.eq("rama_id", request.args["rama_id"])
    return jsonify(q.execute().data)


@app.post("/api/entrenamientos")
@requiere_rol("entrenador")
def crear_entrenamiento():
    c = db()
    d = solo(body(), ["rama_id", "fecha", "hora", "lugar", "notas"])
    if not d.get("fecha"):
        abort(400, "Falta la fecha")
    d["temporada_id"] = temporada_de(c, d["fecha"])
    d["created_by"] = session["user_id"]
    return jsonify(c.table("entrenamientos").insert(d).execute().data[0]), 201


@app.get("/api/entrenamientos/<id>/lista")
@requiere_rol("entrenador", "capitan")
def lista_del_dia(id):
    r = (db().table("v_lista_entrenamiento").select("*")
         .eq("entrenamiento_id", id).order("apellidos").execute())
    return jsonify(r.data)


@app.post("/api/entrenamientos/<id>/asistencia")
@requiere_rol("entrenador", "capitan")
def pasar_asistencia(id):
    d = body()
    fila = {"entrenamiento_id": id, "jugador_id": d["jugador_id"], "estado": d["estado"],
            "registrado_por": session["user_id"]}
    r = db().table("asistencias").upsert(fila, on_conflict="entrenamiento_id,jugador_id").execute()
    return jsonify(r.data)


@app.post("/api/entrenamientos/<id>/asistencia-masiva")
@requiere_rol("entrenador", "capitan")
def asistencia_masiva(id):
    d = body()
    filas = [{"entrenamiento_id": id, "jugador_id": j, "estado": d["estado"],
              "registrado_por": session["user_id"]} for j in d.get("jugadores", [])]
    if filas:
        db().table("asistencias").upsert(filas, on_conflict="entrenamiento_id,jugador_id").execute()
    return jsonify(ok=True, total=len(filas))


@app.get("/api/asistencias/porcentaje")
@requiere_rol()
def porcentaje():

    return jsonify(db().table("v_porcentaje_asistencia").select("*").execute().data)


@app.get("/api/mis-asistencias")
@requiere_rol()
def mis_asistencias():
    r = db().table("asistencias").select("estado, observaciones, entrenamientos(fecha, hora)").execute().data
    r.sort(key=lambda a: a["entrenamientos"]["fecha"], reverse=True)
    return jsonify(r[:40])

@app.get("/api/torneos")
@requiere_rol()
def torneos():
    r = db().table("torneos").select("*, ramas(nombre)").order("fecha_inicio", desc=True).execute()
    return jsonify(r.data)


@app.post("/api/torneos")
@requiere_rol("entrenador")
def crear_torneo():
    c = db()
    d = solo(body(), ["nombre", "rama_id", "sede", "fecha_inicio", "fecha_fin"])
    if not d.get("fecha_inicio"):
        abort(400, "Falta la fecha de inicio")
    d["temporada_id"] = temporada_de(c, d["fecha_inicio"])
    return jsonify(c.table("torneos").insert(d).execute().data[0]), 201


@app.get("/api/partidos")
@requiere_rol()
def partidos():
    q = (db().table("partidos")
         .select("*, ramas(nombre), torneos(nombre), sets_partido(numero_set, puntos_propios, puntos_rival)")
         .order("fecha", desc=True))
    if request.args.get("rama_id"):
        q = q.eq("rama_id", request.args["rama_id"])
    data = q.execute().data
    for p in data:
        p["sets_partido"].sort(key=lambda s: s["numero_set"])
    return jsonify(data)


@app.post("/api/partidos")
@requiere_rol("entrenador")
def crear_partido():
    d = solo(body(), ["torneo_id", "rama_id", "rival", "fecha", "hora", "lugar", "formato_sets"])
    return jsonify(db().table("partidos").insert(d).execute().data[0]), 201


@app.post("/api/partidos/<id>/sets")
@requiere_rol("entrenador")
def guardar_sets(id):
    sets = body().get("sets", [])
    c = db()
    c.table("sets_partido").delete().eq("partido_id", id).execute()
    if sets:
        filas = [{"partido_id": id, **solo(s, ["numero_set", "puntos_propios", "puntos_rival"])} for s in sets]
        c.table("sets_partido").insert(filas).execute()
    # el resultado (victoria/derrota) lo calcula un trigger en la base de datos
    return jsonify(c.table("partidos").select("*").eq("id", id).single().execute().data)

@app.get("/api/reporte")
@requiere_rol("entrenador", "coordinacion")
def reporte():
    desde, hasta, rama = (request.args.get(k) for k in ("desde", "hasta", "rama_id"))
    c = db()

    q = c.table("asistencias").select(
        "estado, jugador_id, jugadores(nombre, apellidos, matricula, estado), "
        "entrenamientos!inner(fecha, rama_id)")
    qe = c.table("entrenamientos").select("id", count="exact")
    qp = c.table("partidos").select("fecha, rival, sets_ganados, sets_perdidos, resultado, torneos(nombre), ramas(nombre)")
    if desde:
        q, qe, qp = (q.gte("entrenamientos.fecha", desde), qe.gte("fecha", desde), qp.gte("fecha", desde))
    if hasta:
        q, qe, qp = (q.lte("entrenamientos.fecha", hasta), qe.lte("fecha", hasta), qp.lte("fecha", hasta))
    if rama:
        q, qe, qp = (q.eq("entrenamientos.rama_id", rama), qe.eq("rama_id", rama), qp.eq("rama_id", rama))

    clave = {"presente": "presentes", "falta": "faltas", "justificada": "justificadas"}
    agg = {}
    for f in q.execute().data:
        j = f["jugadores"]
        a = agg.setdefault(f["jugador_id"], {
            "jugador": f"{j['apellidos']} {j['nombre']}", "matricula": j["matricula"],
            "estado_jugador": j["estado"], "presentes": 0, "faltas": 0, "justificadas": 0})
        a[clave[f["estado"]]] += 1
    filas = []
    for a in agg.values():
        a["total"] = a["presentes"] + a["faltas"] + a["justificadas"]
        a["porcentaje"] = round(100 * a["presentes"] / a["total"], 1) if a["total"] else 0
        filas.append(a)
    filas.sort(key=lambda a: a["jugador"])

    ps = qp.order("fecha").execute().data
    return jsonify(
        entrenamientos=qe.execute().count or 0,
        asistencias=filas,
        partidos=ps,
        partidos_resumen={
            "jugados": sum(p["resultado"] != "pendiente" for p in ps),
            "victorias": sum(p["resultado"] == "victoria" for p in ps),
            "derrotas": sum(p["resultado"] == "derrota" for p in ps),
        },
    )

@app.get("/api/perfiles")
@requiere_rol("entrenador")
def perfiles():
    return jsonify(db().table("perfiles").select("id, nombre, rol, jugador_id").order("nombre").execute().data)


@app.put("/api/perfiles/<id>")
@requiere_rol("entrenador")
def editar_perfil(id):
    d = solo(body(), ["rol", "jugador_id"])
    if id == session["user_id"] and d.get("rol") not in (None, "entrenador"):
        abort(400, "No puedes quitarte a ti mismo el rol de entrenador.")
    return jsonify(db().table("perfiles").update(d).eq("id", id).execute().data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_DEBUG", "1") == "1")