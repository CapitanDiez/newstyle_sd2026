import ollama

requerimiento = "El usuario ingresa su email, contraseña, y el sistema autentica los datos "
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
        }
    }
)
condicion=response.answers['condicion'].noul

