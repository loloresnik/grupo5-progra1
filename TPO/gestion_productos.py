from functools import reduce

def agregar_producto(productos):

    print("\n=== AGREGAR PRODUCTO ===")

    id_prod = int(input("Ingrese ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    proveedor = input("Ingrese el proveedor: ")

    stock = int(input("Ingrese el stock inicial: "))

    while stock < 0:

        print("El stock no puede ser negativo.")
        stock = int(input("Ingrese el stock inicial: "))

    nuevo = [id_prod, nombre, categoria, proveedor, stock]

    productos.append(nuevo)

    print("Producto agregado correctamente.\n")

    return 1


def mostrar_productos(productos):

    if len(productos) == 0:

        print("No hay productos cargados.")

        return

    print("\n--- LISTA DE PRODUCTOS ---")
    print("#" * 80)
    print("ID             Nombre          Categoria       Proveedor       Stock")
    print("#" * 80)

    for fila in productos:
        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:>5}")

    print("#" * 80)


def buscar_producto(productos, id_prod):

    for prod in productos:

        if prod[0] == id_prod:

            return prod
        
    return None


def modificar_producto(productos, id_prod, nuevo_nombre=None, nueva_categoria=None, nuevo_proveedor=None):

    prod = buscar_producto(productos, id_prod)

    if prod is None:

        print("Producto no encontrado.")
        return 0

    if nuevo_nombre is not None:

        prod[1] = nuevo_nombre

    if nueva_categoria is not None:

        prod[2] = nueva_categoria

    if nuevo_proveedor is not None:

        prod[3] = nuevo_proveedor

    print("Producto modificado correctamente.")
    return 1

#falta agregar la funcion de eliminar al main
def eliminar_producto(productos, id_prod):

    for i in range(len(productos)):

        if productos[i][0] == id_prod:

            productos.pop(i)
            print("Producto eliminado.")
            return 1

    print("Producto no encontrado.")
    return 0

#ingresar cosas que ya estaban en la lista falta agregarlo al main
def ingreso_stock(productos, id_prod, cantidad):

    prod = buscar_producto(productos, id_prod)

    if prod is None:
        print("Producto no encontrado.")
        return 0

    if cantidad <= 0:
        print("Cantidad inválida.")
        return 0

    prod[4] += cantidad
    print("Ingreso registrado. Nuevo stock:", prod[4])
    return 1

#falta hacer que se puedan vender cosas
def egreso_stock(productos, id_prod, cantidad):

    prod = buscar_producto(productos, id_prod)

    if prod is None:
        print("Producto no encontrado.")
        return 0

    if cantidad <= 0:
        print("Cantidad inválida.")
        return 0

    if prod[4] < cantidad:
        print("Stock insuficiente.")
        return 0

    prod[4] -= cantidad
    print("Egreso registrado. Nuevo stock:", prod[4])
    return 1
