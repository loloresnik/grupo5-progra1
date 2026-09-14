import re
from functools import reduce

# Agregar producto
def agregar_producto_dic(productos_dic, ids_unicos, categorias_unicas, proveedores_unicos):
    """Registra un nuevo producto en la lista de diccionarios.
    Valida cada campo ingresado por el usuario y evita que se repitan IDs utilizando un conjunto."""

    print("\n=== AGREGAR PRODUCTO ===")

    # ID
    id_prod = input("Ingrese ID del producto: ").strip()

    while not id_prod.isdigit():

        print("El ID debe ser numerico.")

        id_prod = input("Ingrese ID del producto: ").strip()

    id_prod = int(id_prod)

    # Evito IDs repetidos
    if id_prod in ids_unicos:

        print("El ID ya existe.")

        return 0

    # Nombre
    nombre = input("Ingrese el nombre del producto: ").strip()

    while re.match(r"^[A-Za-z ]+$", nombre) is None:

        print("El nombre solo puede contener letras.")

        nombre = input("Ingrese el nombre del producto: ").strip()

    # Categoria
    categoria = input("Ingrese la categoria: ").strip()

    while re.match(r"^[A-Za-z ]+$", categoria) is None:

        print("La categoria solo puede contener letras.")

        categoria = input("Ingrese la categoria: ").strip()

    # Proveedor
    proveedor = input("Ingrese el proveedor: ").strip()

    while re.match(r"^[A-Za-z ]+$", proveedor) is None:

        print("El proveedor solo puede contener letras.")

        proveedor = input("Ingrese el proveedor: ").strip()

    # Stock
    stock = input("Ingrese el stock inicial: ").strip()

    while not stock.isdigit():

        print("El stock debe ser numerico.")

        stock = input("Ingrese el stock inicial: ").strip()

    nuevo = {
        "id": id_prod,
        "nombre": nombre,
        "categoria": categoria,
        "proveedor": proveedor,
        "stock": int(stock)
    }

    productos_dic.append(nuevo)

    # Actualizo conjuntos
    ids_unicos.add(id_prod)
    categorias_unicas.add(categoria)
    proveedores_unicos.add(proveedor)

    print("Producto agregado correctamente.\n")
    return 1


# Buscar producto 
def buscar_producto_dic(productos_dic, id_prod):
    """Recorre la lista y devuelve el diccionario del producto si encuentra coincidencia.
    Si no existe, devuelve None."""

    for p in productos_dic:

        if p["id"] == id_prod:

            return p

    return None


# Mostrar productos 
def mostrar_productos_dic(productos_dic):
    """Muestra todos los productos almacenados en formato de tabla."""

    if len(productos_dic) == 0:

        print("No hay productos cargados.")

        return

    print("\n--- LISTA DE PRODUCTOS ---")
    print("-" * 80)
    print("ID             Nombre          Categoria       Proveedor       Stock")
    print("-" * 80)

    for p in productos_dic:

        print(f"{p['id']:<15} {p['nombre']:<15} {p['categoria']:<15} {p['proveedor']:<15} {p['stock']:>5}")

    print("-" * 80)


# Modificar producto 
def modificar_producto_dic(productos_dic, id_prod, nuevo_nombre, nueva_categoria, nuevo_proveedor, categorias_unicas, proveedores_unicos):
    #Modifica los datos de un producto existente.
    producto = buscar_producto_dic(productos_dic, id_prod)

    if producto is None:

        print("Producto no encontrado.")

        return 0

    if nuevo_nombre is not None:

        producto["nombre"] = nuevo_nombre

    if nueva_categoria is not None:

        producto["categoria"] = nueva_categoria

        categorias_unicas.add(nueva_categoria)

    if nuevo_proveedor is not None:

        producto["proveedor"] = nuevo_proveedor

        proveedores_unicos.add(nuevo_proveedor)

    print("Producto modificado correctamente.")

    return 1


# Eliminar producto
def eliminar_producto_dic(productos_dic, id_prod, ids_unicos):

    for i in range(len(productos_dic)):
        if productos_dic[i]["id"] == id_prod:
            productos_dic.pop(i)
            ids_unicos.remove(id_prod)
            print("Producto eliminado.")
            return 1

    print("Producto no encontrado.")
    return 0

# Registrar movimiento (ingreso o egreso)
def agregar_movimiento(movimientos, tipo, id_prod, cantidad, productos_dic):

    print("\n=== Registrar movimiento ===")

    # Validar que el ID exista 
    producto = buscar_producto_dic(productos_dic, id_prod)

    if producto is None:

        print("El ID ingresado no existe en el inventario.")

        return 0

    # Fecha como tupla ingresada por el usuario
    dia = input("Dia: ").strip()
    mes = input("Mes: ").strip()
    anio = input("Año: ").strip()

    # Validar que sean números
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):

        print("Fecha invalida (debe contener solo numeros).")

        return 0

    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    # hay alguna libreria que tenga la fecha asi no tengo que hacer esta validacion? 
    # Validar rangos
    if dia < 1 or dia > 31:

        print("Dia invalido (debe estar entre 1 y 31).")

        return 0

    if mes < 1 or mes > 12:

        print("Mes invalido (debe estar entre 1 y 12).")

        return 0

    if anio <= 0:
        print("Año invalido.")
        return 0

    fecha = (dia, mes, anio)

    nuevo = [tipo, id_prod, cantidad, fecha]

    movimientos.append(nuevo)

    print("Movimiento registrado.\n")

    return 1

# Mostrar movimientos
def mostrar_movimientos(movimientos):

    if len(movimientos) == 0:
        
        print("No hay movimientos registrados.")
        
        return

    print("\n--- GESTION DE MOVIMIENTOS ---")
    print("-" * 80)
    print("Tipo           ID Producto     Cantidad        Fecha")
    print("-" * 80)

    for m in movimientos:

        fecha = f"{m[3][0]}/{m[3][1]}/{m[3][2]}"

        print(f"{m[0]:<15} {m[1]:<15} {m[2]:<15} {fecha:<15}")

    print("-" * 80)


# Filtrar movimientos por tipo
def filtrar_movimientos(movimientos, tipo):

    filtrados = list(filter(lambda m: m[0] == tipo, movimientos))

    mostrar_movimientos(filtrados)


def ingreso_stock_dic(productos_dic, id_prod, cantidad):

    producto = buscar_producto_dic(productos_dic, id_prod)

    if producto is None:

        print("Producto no encontrado.")

        return 0

    if cantidad <= 0:

        print("Cantidad invalida.")

        return 0

    producto["stock"] += cantidad

    print("Ingreso registrado. Nuevo stock:", producto["stock"])

    return 1


def egreso_stock_dic(productos_dic, id_prod, cantidad):

    producto = buscar_producto_dic(productos_dic, id_prod)

    if producto is None:

        print("Producto no encontrado.")

        return 0

    if cantidad <= 0:

        print("Cantidad invalida.")

        return 0

    if producto["stock"] < cantidad:

        print("Stock insuficiente.")

        return 0

    producto["stock"] -= cantidad

    print("Egreso registrado. Nuevo stock:", producto["stock"])

    return 1