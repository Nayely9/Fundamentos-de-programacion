#Matriz 3 * 3

matriz = [
    [2, 11, 20],
    [16, 9, 13],
    [19, 8, 5]
]
print(matriz)
#Buscar valor especifico
def buscar_valor(matriz,valor_especifico):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_especifico:
                return i,j

valor_especifico = 16
#print(buscar_valor(matriz,valor_especifico))

if valor_especifico == valor_especifico:
    print("valor encontrado en la posicion",buscar_valor(matriz,valor_especifico))
else:
    print("valor no encontrado")