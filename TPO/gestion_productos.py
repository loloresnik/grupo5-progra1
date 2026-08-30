from functools import reduce

def agregar_producto():
    print("\n=== AGREGAR PRODUCTO ===")

    id_prod = int(input("Ingrese ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    id_categoria = input("Ingrese la categoría: ")
    proveedor = input("Ingrese el proveedor: ")
    productos =[]
    stock = int(input("Ingrese el stock inicial: "))
    while stock < 0:
        print("El stock no puede ser negativo.")
        stock = int(input("Ingrese el stock inicial: "))

    nuevo = [id_prod, nombre, categoria, proveedor, stock]
    productos.append(nuevo)

    print("Producto agregado correctamente.\n")
    return 1


# ============================================================
# 2. BUSCAR PRODUCTO
# ============================================================
def buscar_producto(id_prod):
    for prod in productos:
        if prod[0] == id_prod:
            return prod
    return None


# ============================================================
# 3. MODIFICAR PRODUCTO
# ============================================================
def modificar_producto(id_prod, nuevo_nombre=None, nueva_categoria=None, nuevo_proveedor=None):
    prod = buscar_producto(id_prod)

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


# ============================================================
# 4. ELIMINAR PRODUCTO
# ============================================================
def eliminar_producto(id_prod):
    for i in range(len(productos)):
        if productos[i][0] == id_prod:
            productos.pop(i)
            print("Producto eliminado.")
            return 1

    print("Producto no encontrado.")
    return 0


# ============================================================
# 5. MOSTRAR PRODUCTOS
# ============================================================
def mostrar_productos():
    if len(productos) == 0:
        print("No hay productos cargados.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        print("ID:", p[0], "| Nombre:", p[1], "| Categoría:", p[2],
              "| Proveedor:", p[3], "| Stock:", p[4])
    print("---------------------------\n")


# ============================================================
# 6. INGRESO DE STOCK
# ============================================================
def ingreso_stock(id_prod, cantidad):
    prod = buscar_producto(id_prod)

    if prod is None:
        print("Producto no encontrado.")
        return 0

    if cantidad <= 0:
        print("Cantidad inválida.")
        return 0

    prod[4] += cantidad
    print("Ingreso registrado. Nuevo stock:", prod[4])
    return 1

def egreso_stock(id_prod, cantidad):
    prod = buscar_producto(id_prod)

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

def consultar_stock(id_prod):
    prod = buscar_producto(id_prod)

    if prod is None:
        print("Producto no encontrado.")
        return None

    print("Stock actual:", prod[4])
    return prod[4]