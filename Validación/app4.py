import ollama
 
print("RF-16")
requerimiento = "Cuando ocurre el evento de registro de disponibilidad, es decir, cuando el capitán marca qué jugadores pueden asistir a un partido de liga y presiona el botón 'Guardar disponibilidad', el módulo de partidos y torneos debe registrar la disponibilidad de cada jugador en la base de datos, en la tabla disponibilidad, permitiendo hacer cambios solo hasta el sábado anterior al partido."
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
 
print("RF-09")
requerimiento = "Cuando ocurre el evento de cambio de rama, es decir, cuando el usuario selecciona el filtro 'Femenil' o 'Varonil' en cualquier sección del sistema, el módulo de filtrado debe consultar los jugadores, entrenamientos y partidos en la base de datos, mostrando únicamente los registros de la rama seleccionada."
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
 
print("RF-10")
requerimiento = "Cuando ocurre la situación que detona el evento de generación de reporte, es decir, cuando el entrenador selecciona un rango de fechas y presiona el botón 'Generar reporte', el módulo de reportes debe generar un informe de asistencias y resultados de partidos con los datos de la base de datos, en un tiempo máximo de 2 segundos."
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
 
print("RF-18")
requerimiento = "Cuando ocurre el evento de consulta del reporte individual, es decir, cuando el entrenador selecciona a un jugador y un rango de fechas y presiona el botón 'Ver reporte', el módulo de reportes debe consultar la información del jugador en la base de datos, mostrando los días que entrenó, sus faltas, su porcentaje de asistencia y los partidos para los que estuvo disponible o convocado, en un tiempo máximo de 3 segundos."
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
 
print("RF-19")
requerimiento = "Cuando ocurre el evento de consulta de la coordinación deportiva, es decir, cuando la coordinación selecciona una rama en el módulo de reportes y presiona el botón 'Consultar', el módulo de reportes debe consultar en la base de datos la lista de jugadores activos y los resultados de la liga y los torneos, mostrando el total de partidos ganados y perdidos y permitiendo descargar la información en PDF."
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