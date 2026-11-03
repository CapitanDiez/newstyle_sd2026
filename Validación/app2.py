import ollama
 
print("RF-03")
requerimiento = "Cuando ocurre el evento de pase de lista, es decir, cuando el entrenador o el capitán presiona el botón 'Pase de lista', el módulo de asistencias debe consultar el estado de cada jugador en la base de datos, en la tabla jugadores, mostrando únicamente a los jugadores con estado 'activo' en un tiempo máximo de 3 segundos."
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
 
print("RF-05")
requerimiento = "Cuando ocurre el evento de registro de asistencia, es decir, cuando el entrenador o el capitán marca a cada jugador como presente, falta o justificada y presiona el botón 'Guardar asistencia', el módulo de asistencias debe registrar el estado de cada jugador en la base de datos, en la tabla asistencias, asociando cada registro al entrenamiento seleccionado."
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
 
print("RF-06")
requerimiento = "Cuando ocurre el evento de consulta de la lista de jugadores, es decir, cuando el entrenador, el capitán o la coordinación deportiva abre esa lista, el módulo de asistencias debe calcular el porcentaje de asistencia de cada jugador con los datos de la base de datos, en la tabla asistencias, dividiendo sus asistencias entre el total de entrenamientos realizados en el periodo y multiplicando por 100."
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
 
print("RF-13")
requerimiento = "Cuando ocurre el evento de apertura de la lista de jugadores, es decir, cuando el entrenador entra a esa pantalla, el módulo de asistencias debe revisar las asistencias de cada jugador activo en la base de datos, en la tabla asistencias, marcando como 'posible baja' a quien no haya asistido a ninguno de los últimos 12 entrenamientos (3 semanas)."
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
 
print("RF-14")
requerimiento = "Cuando ocurre el evento de guardado del pase de lista, es decir, cuando el entrenador o el capitán presiona el botón 'Guardar asistencia', el módulo de asistencias debe buscar en la base de datos, en la tabla asistencias, si ya existe un registro del mismo jugador para ese entrenamiento, bloqueando el guardado y mostrando un mensaje de error si lo encuentra."
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
 