import ollama
 
print("RF-04")
requerimiento = "Cuando ocurre la situación que detona el evento de programación de un entrenamiento extra, es decir, cuando el entrenador programa una sesión fuera del horario fijo y presiona el botón 'Crear', el módulo de entrenamientos debe registrar la fecha, la hora y la rama de la sesión en la base de datos, en la tabla entrenamientos, habilitándola para el pase de lista y verificando que no se empalme con otro entrenamiento de la misma rama."
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
 
print("RF-15")
requerimiento = "Cuando ocurre el evento de inicio de semana, es decir, cuando el reloj del sistema marca el lunes a las 00:00, el módulo de entrenamientos debe crear automáticamente en la base de datos, en la tabla entrenamientos, los 4 entrenamientos del horario fijo para cada rama: lunes de 13:00 a 15:00, martes y jueves de 16:30 a 18:00 y viernes de 8:30 a 10:30."
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
 
print("RF-07")
requerimiento = "Cuando ocurre el evento de guardado de un partido, es decir, cuando el entrenador presiona el botón 'Guardar partido', el módulo de partidos y torneos debe almacenar el rival, la fecha, los marcadores por set y el resultado final del encuentro en la base de datos, en la tabla partidos, en un tiempo máximo de 3 segundos."
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
 
print("RF-08")
requerimiento = "Cuando ocurre el evento de registro de una competencia, es decir, cuando el entrenador captura el nombre, el tipo (liga o torneo) y las fechas y presiona el botón 'Guardar', el módulo de partidos y torneos debe registrar la competencia en la base de datos, en la tabla torneos, permitiendo asociarle sus partidos para dar seguimiento a los resultados."
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
 
print("RF-17")
requerimiento = "Cuando ocurre el evento de convocatoria, es decir, cuando el entrenador selecciona a los jugadores que irán a un torneo y presiona el botón 'Guardar convocatoria', el módulo de partidos y torneos debe registrar la convocatoria en la base de datos, en la tabla convocatorias, permitiendo un máximo de 12 jugadores activos de la misma rama."
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