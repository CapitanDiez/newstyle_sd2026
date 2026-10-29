import ollama

requerimiento = "Cuando el usuario ingresa su matrícula y contraseña y presiona el botón Iniciar sesión, el sistema de autenticación debe validar la matrícula y la contraseña en la base de datos en la tabla usuarios, verificando que exista un usuario con esa matrícula y contraseña y dándole acceso según su rol."
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


