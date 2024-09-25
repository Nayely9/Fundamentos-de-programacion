#Crear el diccionario inicial
informacion_personal = {
    "nombre": "Juan Gómez",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Doctor"
}

#Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Cuenca"

#Actualizar la clave de la profesión
informacion_personal["profesion"] = "Abogado"

#Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "666-9876"

#Eliminar la clave "edad"
informacion_personal.pop("edad")

#Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
