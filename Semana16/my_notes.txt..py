with open("my_notes.txt", "w") as file:
# Escritura de tres líneas de notas personales en el archivo
    file.write("1. Nombre: Nayely Lissbeth Tumbaco Panchi.\n")
    file.write("2. Carrera: Tecnologias de la informacion.\n")
    file.write("3. Materia: Fundamentos de programacion.\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", "r") as file:
    while True:
        # Usamos readline() para leer cada línea del archivo
        line = file.readline()
        if not line:  # Si no hay más líneas, salimos del bucle
            break
        # Mostramos la línea leída
        print(line.strip())  # Usamos strip() para eliminar el salto de línea

# Asegurándonos de cerrar el archivo automáticamente con 'with'
