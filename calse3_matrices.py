matriz = [
    ["Teclado", "Perifericos", "Proveedor A", 15],
    ["Monitor", "Pantallas", "Proveedor B", 8],
    ["Mouse", "Perifericos", "Proveedor A", 25],
    ["Notebook", "Computacion", "Proveedor C", 5]
]


def mostrar_tabla(matriz):
    print("#" * 80)
    print("Producto        Categoria       Proveedor        Stock")
    print("#" * 80)

    for fila in matriz:
        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:>5}")

    print("#" * 80)


mostrar_tabla(matriz)

columna = int(input("Ingrese el número de columna para ordenar: "))

while columna < 0 or columna >= len(matriz[0]):
    print("error en la columna")
    columna = int(input("Ingrese el número de columna para ordenar: "))

for i in range(len(matriz)):
    for j in range(len(matriz) - 1):
        if matriz[j][columna] > matriz[j + 1][columna]:
            aux = matriz[j]
            matriz[j] = matriz[j + 1]
            matriz[j + 1] = aux

mostrar_tabla(matriz)


def pedir_datos():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una descripcion: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    disponibilidad = input("¿Esta disponible? (True/False): ")

    return nombre, descripcion, precio, cantidad, disponibilidad


def mostrar_ficha(nombre, descripcion, precio, cantidad, disponibilidad):

    descripcion = descripcion[:50]

    if disponibilidad == "True":
        disponibilidad = "Sí"
    else:
        disponibilidad = "No"

    total = precio * cantidad

    print("#" * 80)
    print("FICHA DEL PRODUCTO")
    print("#" * 80)

    print(f"Producto: {nombre}")
    print(f"Descripcion: {descripcion}")
    print(f"Cantidad: {cantidad:>5}")
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Disponibilidad: {disponibilidad}")

    print("#" * 80)


nombre, descripcion, precio, cantidad, disponibilidad = pedir_datos()

mostrar_ficha(nombre, descripcion, precio, cantidad, disponibilidad)