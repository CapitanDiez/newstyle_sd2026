import ollama
 
print("RF-01")
requerimiento = "Cuando ocurre la situación que detona el evento de inicio de sesión, es decir, cuando el usuario presiona el botón 'Iniciar sesión' después de escribir su nombre de usuario y contraseña, el módulo de autenticación debe validar las credenciales en la base de datos, en la tabla usuarios, permitiendo el acceso solo si el registro está activo y tiene uno de los roles permitidos (entrenador, capitán o coordinación deportiva), y mostrando un mensaje de error en caso contrario."
response = ollama.systemone (
    model ="d1-omni:600m",
    state = requerimiento,
    questions ={
        'condicion':{
            'type':'noul',
            "instructions":"¿Incluye una situacion que detone el evento?",
            'criteria':{
                'true': "Especifica claramente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        },
        'sujeto':{
            'type':'noul',
            "instructions":"¿Indica qué sistema o módulo realiza la acción?",
            'criteria':{
                'true': "Menciona claramente el sistema o módulo responsable",
                "false": "No dice qué sistema o módulo realiza la acción"
            }
        },
        'verbo':{
            'type':'noul',
            "instructions":"¿Usa el verbo normativo debe?",
            'criteria':{
                'true': "Usa el verbo debe para indicar obligación",
                "false": "No usa el verbo debe"
            }
        },
        'accion':{
            'type':'noul',
            "instructions":"¿Indica qué acción técnica realiza el sistema?",
            'criteria':{
                'true': "Especifica claramente la acción técnica que se ejecuta",
                "false": "No menciona qué acción realiza el sistema"
            }
        },
        'objeto':{
            'type':'noul',
            "instructions":"¿Indica sobre qué objeto o entidad se realiza la acción?",
            'criteria':{
                'true': "Menciona el objeto o entidad sobre el que se realiza la acción",
                "false": "No menciona sobre qué objeto o entidad se realiza la acción"
            }
        },
        'criterio':{
            'type':'noul',
            "instructions":"¿Incluye un criterio o restricción que se pueda verificar?",
            'criteria':{
                'true': "Especifica un criterio o restricción verificable",
                "false": "No incluye ningún criterio o restricción"
            }
        }
    }
)
condicion=response.answers['condicion'].noul
sujeto=response.answers['sujeto'].noul
verbo=response.answers['verbo'].noul
accion=response.answers['accion'].noul
objeto=response.answers['objeto'].noul
criterio=response.answers['criterio'].noul
 
if condicion >= 0.05:
    print(f"1. Cumple con la condición")
else:
    print(f"1. No cumple con la condición")
 
if sujeto >= 0.05:
    print(f"2. Cumple con el sujeto")
else:
    print(f"2. No cumple con el sujeto")
 
if verbo >= 0.05:
    print(f"3. Cumple con el verbo normativo")
else:
    print(f"3. No cumple con el verbo normativo")
 
if accion >= 0.05:
    print(f"4. Cumple con la acción")
else:
    print(f"4. No cumple con la acción")
 
if objeto >= 0.05:
    print(f"5. Cumple con el objeto")
else:
    print(f"5. No cumple con el objeto")
 
if criterio >= 0.05:
    print(f"6. Cumple con el criterio")
else:
    print(f"6. No cumple con el criterio")
 
print()
 
print("RF-02")
requerimiento = "Cuando el entrenador o el capitán ingresa el nombre, la matrícula, la carrera, la rama y la posición de un jugador en el formulario de registro y presiona el botón 'Guardar', el módulo de gestión de jugadores debe validar que todos los campos obligatorios del formulario estén completos, mostrando el resultado en un tiempo máximo de 2 segundos."
response = ollama.systemone (
    model ="d1-omni:600m",
    state = requerimiento,
    questions ={
        'condicion':{
            'type':'noul',
            "instructions":"¿Incluye una situacion que detone el evento?",
            'criteria':{
                'true': "Especifica claramente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        },
        'sujeto':{
            'type':'noul',
            "instructions":"¿Indica qué sistema o módulo realiza la acción?",
            'criteria':{
                'true': "Menciona claramente el sistema o módulo responsable",
                "false": "No dice qué sistema o módulo realiza la acción"
            }
        },
        'verbo':{
            'type':'noul',
            "instructions":"¿Usa el verbo normativo debe?",
            'criteria':{
                'true': "Usa el verbo debe para indicar obligación",
                "false": "No usa el verbo debe"
            }
        },
        'accion':{
            'type':'noul',
            "instructions":"¿Indica qué acción técnica realiza el sistema?",
            'criteria':{
                'true': "Especifica claramente la acción técnica que se ejecuta",
                "false": "No menciona qué acción realiza el sistema"
            }
        },
        'objeto':{
            'type':'noul',
            "instructions":"¿Indica sobre qué objeto o entidad se realiza la acción?",
            'criteria':{
                'true': "Menciona el objeto o entidad sobre el que se realiza la acción",
                "false": "No menciona sobre qué objeto o entidad se realiza la acción"
            }
        },
        'criterio':{
            'type':'noul',
            "instructions":"¿Incluye un criterio o restricción que se pueda verificar?",
            'criteria':{
                'true': "Especifica un criterio o restricción verificable",
                "false": "No incluye ningún criterio o restricción"
            }
        }
    }
)
condicion=response.answers['condicion'].noul
sujeto=response.answers['sujeto'].noul
verbo=response.answers['verbo'].noul
accion=response.answers['accion'].noul
objeto=response.answers['objeto'].noul
criterio=response.answers['criterio'].noul
 
if condicion >= 0.05:
    print(f"1. Cumple con la condición")
else:
    print(f"1. No cumple con la condición")
 
if sujeto >= 0.05:
    print(f"2. Cumple con el sujeto")
else:
    print(f"2. No cumple con el sujeto")
 
if verbo >= 0.05:
    print(f"3. Cumple con el verbo normativo")
else:
    print(f"3. No cumple con el verbo normativo")
 
if accion >= 0.05:
    print(f"4. Cumple con la acción")
else:
    print(f"4. No cumple con la acción")
 
if objeto >= 0.05:
    print(f"5. Cumple con el objeto")
else:
    print(f"5. No cumple con el objeto")
 
if criterio >= 0.05:
    print(f"6. Cumple con el criterio")
else:
    print(f"6. No cumple con el criterio")
 
print()
 
print("RF-11")
requerimiento = "Cuando ocurre el evento de guardado de un jugador, es decir, cuando el entrenador o el capitán confirma el registro después de que el formulario pasó la validación, el módulo de gestión de jugadores debe guardar al nuevo jugador en la base de datos, en la tabla jugadores, con estado 'activo', verificando que la matrícula no esté registrada y que el número de playera no se repita dentro de la misma rama."
response = ollama.systemone (
    model ="d1-omni:600m",
    state = requerimiento,
    questions ={
        'condicion':{
            'type':'noul',
            "instructions":"¿Incluye una situacion que detone el evento?",
            'criteria':{
                'true': "Especifica claramente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        },
        'sujeto':{
            'type':'noul',
            "instructions":"¿Indica qué sistema o módulo realiza la acción?",
            'criteria':{
                'true': "Menciona claramente el sistema o módulo responsable",
                "false": "No dice qué sistema o módulo realiza la acción"
            }
        },
        'verbo':{
            'type':'noul',
            "instructions":"¿Usa el verbo normativo debe?",
            'criteria':{
                'true': "Usa el verbo debe para indicar obligación",
                "false": "No usa el verbo debe"
            }
        },
        'accion':{
            'type':'noul',
            "instructions":"¿Indica qué acción técnica realiza el sistema?",
            'criteria':{
                'true': "Especifica claramente la acción técnica que se ejecuta",
                "false": "No menciona qué acción realiza el sistema"
            }
        },
        'objeto':{
            'type':'noul',
            "instructions":"¿Indica sobre qué objeto o entidad se realiza la acción?",
            'criteria':{
                'true': "Menciona el objeto o entidad sobre el que se realiza la acción",
                "false": "No menciona sobre qué objeto o entidad se realiza la acción"
            }
        },
        'criterio':{
            'type':'noul',
            "instructions":"¿Incluye un criterio o restricción que se pueda verificar?",
            'criteria':{
                'true': "Especifica un criterio o restricción verificable",
                "false": "No incluye ningún criterio o restricción"
            }
        }
    }
)
condicion=response.answers['condicion'].noul
sujeto=response.answers['sujeto'].noul
verbo=response.answers['verbo'].noul
accion=response.answers['accion'].noul
objeto=response.answers['objeto'].noul
criterio=response.answers['criterio'].noul
 
if condicion >= 0.05:
    print(f"1. Cumple con la condición")
else:
    print(f"1. No cumple con la condición")
 
if sujeto >= 0.05:
    print(f"2. Cumple con el sujeto")
else:
    print(f"2. No cumple con el sujeto")
 
if verbo >= 0.05:
    print(f"3. Cumple con el verbo normativo")
else:
    print(f"3. No cumple con el verbo normativo")
 
if accion >= 0.05:
    print(f"4. Cumple con la acción")
else:
    print(f"4. No cumple con la acción")
 
if objeto >= 0.05:
    print(f"5. Cumple con el objeto")
else:
    print(f"5. No cumple con el objeto")
 
if criterio >= 0.05:
    print(f"6. Cumple con el criterio")
else:
    print(f"6. No cumple con el criterio")
 
print()
 
print("RF-12")
requerimiento = "Cuando ocurre el evento de cambio de estado de un jugador, es decir, cuando el entrenador presiona el botón 'Dar de baja' o 'Reactivar', el módulo de gestión de jugadores debe cambiar el estado del jugador a 'baja' o 'activo' en la base de datos, en la tabla jugadores, conservando su historial de asistencias y partidos sin eliminar el registro."
response = ollama.systemone (
    model ="d1-omni:600m",
    state = requerimiento,
    questions ={
        'condicion':{
            'type':'noul',
            "instructions":"¿Incluye una situacion que detone el evento?",
            'criteria':{
                'true': "Especifica claramente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        },
        'sujeto':{
            'type':'noul',
            "instructions":"¿Indica qué sistema o módulo realiza la acción?",
            'criteria':{
                'true': "Menciona claramente el sistema o módulo responsable",
                "false": "No dice qué sistema o módulo realiza la acción"
            }
        },
        'verbo':{
            'type':'noul',
            "instructions":"¿Usa el verbo normativo debe?",
            'criteria':{
                'true': "Usa el verbo debe para indicar obligación",
                "false": "No usa el verbo debe"
            }
        },
        'accion':{
            'type':'noul',
            "instructions":"¿Indica qué acción técnica realiza el sistema?",
            'criteria':{
                'true': "Especifica claramente la acción técnica que se ejecuta",
                "false": "No menciona qué acción realiza el sistema"
            }
        },
        'objeto':{
            'type':'noul',
            "instructions":"¿Indica sobre qué objeto o entidad se realiza la acción?",
            'criteria':{
                'true': "Menciona el objeto o entidad sobre el que se realiza la acción",
                "false": "No menciona sobre qué objeto o entidad se realiza la acción"
            }
        },
        'criterio':{
            'type':'noul',
            "instructions":"¿Incluye un criterio o restricción que se pueda verificar?",
            'criteria':{
                'true': "Especifica un criterio o restricción verificable",
                "false": "No incluye ningún criterio o restricción"
            }
        }
    }
)
condicion=response.answers['condicion'].noul
sujeto=response.answers['sujeto'].noul
verbo=response.answers['verbo'].noul
accion=response.answers['accion'].noul
objeto=response.answers['objeto'].noul
criterio=response.answers['criterio'].noul
 
if condicion >= 0.05:
    print(f"1. Cumple con la condición")
else:
    print(f"1. No cumple con la condición")
 
if sujeto >= 0.05:
    print(f"2. Cumple con el sujeto")
else:
    print(f"2. No cumple con el sujeto")
 
if verbo >= 0.05:
    print(f"3. Cumple con el verbo normativo")
else:
    print(f"3. No cumple con el verbo normativo")
 
if accion >= 0.05:
    print(f"4. Cumple con la acción")
else:
    print(f"4. No cumple con la acción")
 
if objeto >= 0.05:
    print(f"5. Cumple con el objeto")
else:
    print(f"5. No cumple con el objeto")
 
if criterio >= 0.05:
    print(f"6. Cumple con el criterio")
else:
    print(f"6. No cumple con el criterio")
 
print()
 
print("RF-20")
requerimiento = "Cuando ocurre el evento de inicio de sesión de un capitán o de la coordinación deportiva, es decir, cuando uno de estos usuarios entra al sistema, el módulo de autenticación debe consultar su rol en la base de datos, en la tabla usuarios, habilitando al capitán solo el registro de jugadores, el pase de lista y la disponibilidad, y a la coordinación deportiva solo la consulta de jugadores y reportes."
response = ollama.systemone (
    model ="d1-omni:600m",
    state = requerimiento,
    questions ={
        'condicion':{
            'type':'noul',
            "instructions":"¿Incluye una situacion que detone el evento?",
            'criteria':{
                'true': "Especifica claramente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        },
        'sujeto':{
            'type':'noul',
            "instructions":"¿Indica qué sistema o módulo realiza la acción?",
            'criteria':{
                'true': "Menciona claramente el sistema o módulo responsable",
                "false": "No dice qué sistema o módulo realiza la acción"
            }
        },
        'verbo':{
            'type':'noul',
            "instructions":"¿Usa el verbo normativo debe?",
            'criteria':{
                'true': "Usa el verbo debe para indicar obligación",
                "false": "No usa el verbo debe"
            }
        },
        'accion':{
            'type':'noul',
            "instructions":"¿Indica qué acción técnica realiza el sistema?",
            'criteria':{
                'true': "Especifica claramente la acción técnica que se ejecuta",
                "false": "No menciona qué acción realiza el sistema"
            }
        },
        'objeto':{
            'type':'noul',
            "instructions":"¿Indica sobre qué objeto o entidad se realiza la acción?",
            'criteria':{
                'true': "Menciona el objeto o entidad sobre el que se realiza la acción",
                "false": "No menciona sobre qué objeto o entidad se realiza la acción"
            }
        },
        'criterio':{
            'type':'noul',
            "instructions":"¿Incluye un criterio o restricción que se pueda verificar?",
            'criteria':{
                'true': "Especifica un criterio o restricción verificable",
                "false": "No incluye ningún criterio o restricción"
            }
        }
    }
)
condicion=response.answers['condicion'].noul
sujeto=response.answers['sujeto'].noul
verbo=response.answers['verbo'].noul
accion=response.answers['accion'].noul
objeto=response.answers['objeto'].noul
criterio=response.answers['criterio'].noul
 
if condicion >= 0.05:
    print(f"1. Cumple con la condición")
else:
    print(f"1. No cumple con la condición")
 
if sujeto >= 0.05:
    print(f"2. Cumple con el sujeto")
else:
    print(f"2. No cumple con el sujeto")
 
if verbo >= 0.05:
    print(f"3. Cumple con el verbo normativo")
else:
    print(f"3. No cumple con el verbo normativo")
 
if accion >= 0.05:
    print(f"4. Cumple con la acción")
else:
    print(f"4. No cumple con la acción")
 
if objeto >= 0.05:
    print(f"5. Cumple con el objeto")
else:
    print(f"5. No cumple con el objeto")
 
if criterio >= 0.05:
    print(f"6. Cumple con el criterio")
else:
    print(f"6. No cumple con el criterio")
 
print()