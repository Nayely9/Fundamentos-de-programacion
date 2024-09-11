# Definir los datos
ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear una matriz 3D para almacenar las temperaturas
# Inicializamos con valores aleatorios para el ejemplo (temperaturas entre -10°C y 35°C)
import random

temperaturas = [[[random.uniform(-10, 35) for _ in range(num_semanas)] for _ in range(len(dias_semana))] for _ in range(len(ciudades))]

# Imprimir la matriz de temperaturas
print("Matriz de temperaturas (ciudades, días, semanas):")
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas para {ciudad}:")
    for semana in range(num_semanas):
        print(f"  Semana {semana + 1}:")
        for dia in range(len(dias_semana)):
            print(f"    {dias_semana[dia]}: {temperaturas[i][dia][semana]:.2f}°C")

# Calcular los promedios semanales para cada ciudad
print("\nPromedio de temperaturas por ciudad y semana:")
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios para {ciudad}:")
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[i][dia][semana]
        promedio_semanal = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio_semanal:.2f}°C")

# Definir los datos
ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear una matriz 3D para almacenar las temperaturas
# Inicializamos con valores aleatorios para el ejemplo (temperaturas entre -10°C y 35°C)
import random

temperaturas = [[[random.uniform(-10, 35) for _ in range(num_semanas)] for _ in range(len(dias_semana))] for _ in
                range(len(ciudades))]


# Función para calcular los promedios de temperatura por ciudad
def calcular_promedio_total_ciudades(temperaturas, ciudades, dias_semana, num_semanas):
    promedios_totales = {}

    for i, ciudad in enumerate(ciudades):
        suma_total_temperaturas = 0
        num_datos = len(dias_semana) * num_semanas  # Número total de temperaturas registradas por ciudad

        for semana in range(num_semanas):
            for dia in range(len(dias_semana)):
                suma_total_temperaturas += temperaturas[i][dia][semana]

        # Calcular el promedio total de la ciudad
        promedio_total = suma_total_temperaturas / num_datos
        promedios_totales[ciudad] = promedio_total

    return promedios_totales


# Calcular el promedio total de temperaturas por ciudad
promedios_ciudades = calcular_promedio_total_ciudades(temperaturas, ciudades, dias_semana, num_semanas)

# Imprimir los resultados
print("\nPromedio total de temperaturas por ciudad:")
for ciudad, promedio in promedios_ciudades.items():
    print(f"{ciudad}: {promedio:.2f}°C")
