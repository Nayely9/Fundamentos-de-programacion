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
