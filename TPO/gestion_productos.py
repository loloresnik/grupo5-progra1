import re
from functools import reduce

# AGREGAR PRODUCTO
# Pide los datos del producto, los valida y los agrega a la lista.
def agregar_producto(productos):

    print("\n=== AGREGAR PRODUCTO ===")

    # ID (solo números)
    id_prod = input("Ingrese ID del producto: ")

    while re.match(r"^\d+$", id_prod) is None:

        print("El ID debe ser numerico.")

        id_prod = input("Ingrese ID del producto: ")

    id_prod = int(id_prod)

    # Nombre (solo letras y espacios)
    nombre = input("Ingrese el nombre del producto: ")

    while re.match(r"^[A-Za-z ]+$", nombre) is None:

        print("El nombre solo puede contener letras.")

        nombre = input("Ingrese el nombre del producto: ")

    # Categoria
    id_categoria = input("Ingrese la categoria: ")

    while re.match(r"^[A-Za-z ]+$", id_categoria) is None:

        print("La categoria solo puede contener letras.")

        id_categoria = input("Ingrese la categoria: ")



    # Proveedor
    proveedor = input("Ingrese el proveedor: ")

    while re.match(r"^[A-Za-z ]+$", proveedor) is None:

        print("El proveedor solo puede contener letras.")

        proveedor = input("Ingrese el proveedor: ")

    # Stock (solo números)
    stock = input("Ingrese el stock inicial: ")

    while re.match(r"^\d+$", stock) is None:

        print("El stock debe ser un numero entero.")
        stock = input("Ingrese el stock inicial: ")

    stock = int(stock)

    nuevo = [id_prod, nombre, id_categoria, proveedor, stock]

    productos.append(nuevo)

    print("Producto agregado correctamente.\n")

    return 1

# BUSCAR PRODUCTO
# Busca un producto por ID.
def buscar_producto(productos, id_prod):

    for producto in productos:

        if producto[0] == id_prod:

            return producto

    return None

# MODIFICAR PRODUCTO
# Cambia nombre, categoria o proveedor del producto.
def modificar_producto(productos, id_prod, nuevo_nombre=None, nueva_categoria=None, nuevo_proveedor=None):

    producto = buscar_producto(productos, id_prod)

    if producto is None:
        print("Producto no encontrado.")
        return 0


    if nuevo_nombre is not None:

        producto[1] = nuevo_nombre

    if nueva_categoria is not None:

        producto[2] = nueva_categoria

    if nuevo_proveedor is not None:

        producto[3] = nuevo_proveedor


    print("Producto modificado correctamente.")
    return 1

# ELIMINAR PRODUCTO
def eliminar_producto(productos, id_prod):

    for i in range(len(productos)):

        if productos[i][0] == id_prod:

            productos.pop(i)
            print("Producto eliminado.")
            return 1

    print("Producto no encontrado.")
    return 0

# MOSTRAR PRODUCTOS
def mostrar_productos(productos):

    if len(productos) == 0:
        print("No hay productos cargados.")
        return


    print("\n--- LISTA DE PRODUCTOS ---")
    print("#" * 80)
    print("ID             Nombre          Categoria       Proveedor       Stock")
    print("#" * 80)

    for p in productos:
        
        print(f"{p[0]:<15} {p[1]:<15} {p[2]:<15} {p[3]:<15} {p[4]:>5}")

    print("#" * 80)

# INGRESO DE STOCK
def ingreso_stock(productos, id_prod, cantidad):

    producto = buscar_producto(productos, id_prod)

    if producto is None:
        print("Producto no encontrado.")
        return 0


    if cantidad <= 0:
        print("Cantidad invalida.")
        return 0


    producto[4] += cantidad

    print("Ingreso registrado. Nuevo stock:", producto[4])

    return 1

# EGRESO DE STOCK
def egreso_stock(productos, id_prod, cantidad):

    producto = buscar_producto(productos, id_prod)

    if producto is None:
        print("Producto no encontrado.")
        return 0


    if cantidad <= 0:
        print("Cantidad invalida.")
        return 0


    if producto[4] < cantidad:
        print("Stock insuficiente.")
        return 0


    producto[4] -= cantidad

    print("Egreso registrado. Nuevo stock:", producto[4])

    return 1

# CONSULTAR STOCK
def consultar_stock(productos, id_prod):

    producto = buscar_producto(productos, id_prod)

    if producto is None:
        print("Producto no encontrado.")
        return None


    print("Stock actual:", producto[4])

    return producto[4]

# ORDENAR POR NOMBRE
def ordenar_por_nombre(productos):

    productos.sort(key=lambda p: p[1])


    print("Productos ordenados por nombre:")
    print("#" * 80)
    print("ID             Nombre          Categoria       Proveedor       Stock")
    print("#" * 80)

    for fila in productos:

        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:>5}")

    print("#" * 80)


# ORDENAR POR STOCK
def ordenar_por_stock(productos):

    ordenados = sorted(productos, key=lambda p: p[4])


    print("Productos ordenados por stock:")
    print("#" * 80)
    print("ID             Nombre          Categoria       Proveedor       Stock")
    print("#" * 80)

    for fila in ordenados:

        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:>5}")

    print("#" * 80)

# FILTRAR STOCK BAJO
def filtrar_stock_bajo(productos, limite):

    bajos = list(filter(lambda p: p[4] < limite, productos))


    print("Productos con stock menor al limite:")
    print("#" * 80)
    print("ID             Nombre          Categoria       Proveedor       Stock")
    print("#" * 80)

    for fila in bajos:

        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:>5}")

    print("#" * 80)

# MOSTRAR NOMBRES
def mostrar_nombres(productos):

    nombres = list(map(lambda p: p[1], productos))


    print("Nombres de productos:")
    print("#" * 40)
    print("Nombre")
    print("#" * 40)

    for nombre in nombres:
        print(f"{nombre:<30}")

    print("#" * 40)

# STOCK TOTAL
def stock_total(productos):

    total = reduce(lambda acum, p: acum + p[4], productos, 0)


    print("#" * 40)
    print(f"{'Stock total en inventario:':<30} {total:>5}")
    print("#" * 40)
