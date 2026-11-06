import re
import json
import proveedores

# Agregar producto
def agregar_producto_dic(productos_dic, ids_unicos, proveedores_lista):
    """Registra un nuevo producto en el diccionario de productos (clave = ID del producto).
    Valida cada campo ingresado por el usuario, evita que se repitan IDs
    y verifica que el proveedor exista en la lista de proveedores."""

    print("\n=== AGREGAR PRODUCTO ===")

    id_prod = input("Ingrese ID del producto: ").strip()

    while re.match(r"^\d+$", id_prod) is None:

        print("El ID debe ser numérico.")

        id_prod = input("Ingrese ID del producto: ").strip()

    id_prod = int(id_prod)

    if id_prod in productos_dic:

        print("El ID ya existe.")

        return 0

    nombre = input("Ingrese el nombre del producto: ").strip()

    while re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", nombre) is None:

        print("El nombre solo puede contener letras.")

        nombre = input("Ingrese el nombre del producto: ").strip()

    categoria = input("Ingrese la categoría: ").strip()

    while re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", nombre) is None:

        print("La categoría solo puede contener letras.")

        categoria = input("Ingrese la categoría: ").strip()

    id_proveedor = input("Ingrese el ID del proveedor: ").strip()

    while re.match(r"^\d+$", id_proveedor) is None:

        print("El ID del proveedor debe ser numérico.")

        id_proveedor = input("Ingrese el ID del proveedor: ").strip()

    id_proveedor = int(id_proveedor)

    if proveedores.buscar_proveedor_por_id(proveedores_lista, id_proveedor) is None:

        print("No existe un proveedor con ese ID. Registre primero el proveedor.")

        return 0

    stock = input("Ingrese el stock inicial: ").strip()

    while re.match(r"^\d+$", stock) is None:

        print("El stock debe ser numérico.")

        stock = input("Ingrese el stock inicial: ").strip()

    precio = input("Ingrese el precio del producto: ").strip()

    while re.match(r"^\d+$", precio) is None:

        print("El precio debe ser numérico.")

        precio = input("Ingrese el precio del producto: ").strip()

    nuevo = {
        "nombre": nombre,
        "categoria": categoria,
        "id_proveedor": id_proveedor,
        "stock": int(stock),
        "precio": int(precio)
    }

    productos_dic[id_prod] = nuevo

    ids_unicos.add(id_prod)

    print("Producto agregado correctamente.\n")

    return 1

# Buscar producto 
def buscar_producto_dic(productos_dic, id_prod):
    """Devuelve el diccionario del producto con ese ID.
    Si no existe, devuelve None."""

    return productos_dic.get(id_prod)

# Mostrar productos 
def mostrar_productos_dic(productos_dic, proveedores_lista):
    """Muestra todos los productos almacenados en formato de tabla,
    con el nombre del proveedor obtenido a partir de su ID."""

    if len(productos_dic) == 0:

        print("No hay productos cargados.")

        return

    print("\n--- LISTA DE PRODUCTOS ---")
    print("-" * 100)
    print("ID             Nombre          Categoria       Proveedor       Stock     Precio")
    print("-" * 100)

    for id_prod, p in productos_dic.items():

        nombre_prov = proveedores.nombre_proveedor(proveedores_lista, p["id_proveedor"])

        print(f"{id_prod:<15} {p['nombre']:<15} {p['categoria']:<15} {nombre_prov:<15} {p['stock']:<10} ${p['precio']}")

    print("-" * 100)

# Modificar producto 
def modificar_producto_dic(productos_dic, id_prod, nuevo_nombre, nueva_categoria, nuevo_id_proveedor, nuevo_precio, proveedores_lista):

    producto = buscar_producto_dic(productos_dic, id_prod)

    if producto is None:

        print("Producto no encontrado.")

        return 0

    if nuevo_id_proveedor is not None and proveedores.buscar_proveedor_por_id(proveedores_lista, nuevo_id_proveedor) is None:

        print("No existe un proveedor con ese ID.")

        return 0

    if nuevo_nombre is not None:

        producto["nombre"] = nuevo_nombre

    if nueva_categoria is not None:

        producto["categoria"] = nueva_categoria

    if nuevo_id_proveedor is not None:

        producto["id_proveedor"] = nuevo_id_proveedor

    if nuevo_precio is not None:

        producto["precio"] = nuevo_precio

    print("Producto modificado correctamente.")

    return 1

# Eliminar producto
def eliminar_producto_dic(productos_dic, id_prod, ids_unicos):

    try:

        del productos_dic[id_prod]

    except KeyError:

        print("Producto no encontrado.")

        return 0

    ids_unicos.discard(id_prod)

    print("Producto eliminado.")

    return 1

# Registrar movimiento
def agregar_movimiento(movimientos, tipo, id_prod, cantidad, productos_dic):

    try:

        print("\n=== Registrar movimiento ===")

        producto = buscar_producto_dic(productos_dic, id_prod)

        if producto is None:

            print("El ID ingresado no existe en el inventario.")

            return 0

        dia = input("Dia: ").strip()
        mes = input("Mes: ").strip()
        anio = input("Año: ").strip()

        if re.match(r"^\d+$", dia) is None or re.match(r"^\d+$", mes) is None or re.match(r"^\d+$", anio) is None:

            print("Fecha inválida.")

            return 0

        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        if dia < 1 or dia > 31:

            print("Día inválido.")

            return 0

        if mes < 1 or mes > 12:

            print("Mes inválido.")

            return 0

        if anio <= 0:

            print("Año inválido.")

            return 0

        fecha = (dia, mes, anio)

        movimientos.append([tipo, id_prod, cantidad, fecha])

        print("Movimiento registrado.")

        return 1

    except ValueError as error:

        print("Fecha inválida:", error)

        return 0

# Mostrar movimientos
def mostrar_movimientos(movimientos):
    """Muestra todos los movimientos registrados."""

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

# Ingreso de stock
def ingreso_stock_dic(productos_dic, id_prod, cantidad):

    try:

        producto = buscar_producto_dic(productos_dic, id_prod)

        if producto is None:

            print("Producto no encontrado.")

            return 0

        if cantidad <= 0:

            print("Cantidad inválida.")

            return 0

        producto["stock"] += cantidad

        print("Ingreso registrado. Nuevo stock:", producto["stock"])

        return 1

    except (KeyError, TypeError) as error:

        print("Error en los datos del producto:", error)

        return 0

def guardar_productos_json(productos_dic):
    """Guarda el diccionario de productos en productos.json.
    JSON guarda las claves como texto: el ID 1 queda como "1"."""

    try:

        archivo = open("productos.json", "w", encoding="utf-8")

        json.dump(
            productos_dic,
            archivo,
            indent=4,
            ensure_ascii=False
        )

        archivo.close()

        return 1

    except (OSError, TypeError) as error:

        print("Error al guardar productos:", error)

        return 0


def cargar_productos_json():
    """Carga productos.json y vuelve a convertir las claves (IDs) de texto a número."""

    try:

        archivo = open("productos.json", "r", encoding="utf-8")

        datos = json.load(archivo)

        archivo.close()

        productos_dic = {}

        for id_prod, producto in datos.items():

            productos_dic[int(id_prod)] = producto

        return productos_dic

    except FileNotFoundError:

        return {}

    except (OSError, ValueError, AttributeError) as error:

        print("Error al cargar productos:", error)

        return {}

def guardar_movimientos_txt(movimientos):

    try:

        archivo = open(
            "movimientos.txt",
            "w",
            encoding="utf-8"
        )

        for movimiento in movimientos:

            tipo = movimiento[0]
            id_prod = movimiento[1]
            cantidad = movimiento[2]

            fecha = movimiento[3]

            linea = "{};{};{};{};{};{}\n".format(
                tipo,
                id_prod,
                cantidad,
                fecha[0],
                fecha[1],
                fecha[2]
            )

            archivo.write(linea)

        archivo.close()

        return 1

    except OSError as error:

        print("Error al guardar movimientos:", error)

        return 0

def cargar_movimientos_txt():

    movimientos = []

    try:

        archivo = open(
            "movimientos.txt",
            "r",
            encoding="utf-8"
        )

        for linea in archivo:

            datos = linea.strip().split(";")

            movimiento = [
                datos[0],
                int(datos[1]),
                int(datos[2]),
                (
                    int(datos[3]),
                    int(datos[4]),
                    int(datos[5])
                )
            ]

            movimientos.append(movimiento)

        archivo.close()

        return movimientos

    except FileNotFoundError:

        return []

    except (OSError, ValueError, IndexError) as error:

        print("Error al cargar movimientos:", error)

        return []
