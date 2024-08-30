#ejercicio 2 matriz 3*3
matriz = [
    [2, 1, 20],
    [6, 9, 13],
    [19, 8, 5]
]
print(matriz)
#metodo de ordenamiento buble_sort
def buble_sort(fila):
    #algoritmo buble sort
    n=len(fila)
    for i in range(n):
        for j in range(n-1, i,-1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

print("Matriz original")
print(matriz)
buble_sort(matriz[0])
print(matriz)

