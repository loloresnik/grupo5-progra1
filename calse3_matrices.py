matriz = [
    ["Teclado", "Perifericos", "Proveedor A", 15],
    ["Monitor", "Pantallas", "Proveedor B", 8],
    ["Mouse", "Perifericos", "Proveedor A", 25],
    ["Notebook", "Computacion", "Proveedor C", 5]
]


def mostrar_matriz(matriz):
    print("Producto        Categoria       Proveedor        Stock")
    
    for fila in matriz:
        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:>5}")


mostrar_matriz(matriz)

columna = int(input("Ingrese el número de columna para ordenar: "))

while columna < 0 or columna >= len(matriz[0]):
    print("Columna inválida")
    columna = int(input("Ingrese el número de columna para ordenar: "))

for i in range(len(matriz)):
    for j in range(len(matriz) - 1):
        if matriz[j][columna] > matriz[j + 1][columna]:
            aux = matriz[j]
            matriz[j] = matriz[j + 1]
            matriz[j + 1] = aux

mostrar_matriz(matriz)