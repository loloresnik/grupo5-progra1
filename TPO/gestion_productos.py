import proveedores

# Los productos se guardan en un diccionario cuya clave es el ID:
# productos = {1001: {"nombre": "Teclado", "categoria": "Perifericos",
#                     "id_proveedor": 1, "stock": 20, "precio": 15000.0}}
#
# Los movimientos se guardan en una matriz (lista de listas):
# movimiento = [tipo, id_producto, cantidad, (dia, mes, anio)]
#
# "lista_prov" es la matriz de proveedores (se llama así para no confundirla con el módulo proveedores).


def capitalizar(texto):
    """Pone en mayúscula solo la primera letra usando rebanadas: 'ssd 1TB' -> 'Ssd 1TB'"""
    texto = texto.strip()
    return texto[:1].upper() + texto[1:]


# Agregar producto
def alta_producto(productos, lista_prov, id_prod, nombre, categoria, id_proveedor, stock, precio):
    """Registra un nuevo producto.
    Lanza ValueError si el ID está repetido, el proveedor no existe o algún dato es inválido."""

    if id_prod in productos:
        raise ValueError("El ID ya existe.")

    if id_prod <= 0:
        raise ValueError("El ID debe ser mayor a 0.")

    if not proveedores.validar_nombre(nombre.strip()):
        raise ValueError("El nombre es inválido.")

    if not proveedores.validar_nombre(categoria.strip()):
        raise ValueError("La categoría es inválida.")

    if proveedores.buscar_proveedor_por_id(lista_prov, id_proveedor) is None:
        raise ValueError("No existe un proveedor con ese ID.")

    if stock < 0 or precio < 0:
        raise ValueError("El stock y el precio no pueden ser negativos.")

    productos[id_prod] = {
        "nombre": capitalizar(nombre),
        "categoria": capitalizar(categoria),
        "id_proveedor": id_proveedor,
        "stock": stock,
        "precio": precio
    }


# Buscar producto
def buscar_producto_dic(productos, id_prod):
    """Devuelve el diccionario del producto o None si no existe."""
    return productos.get(id_prod)


# Modificar producto
def modificar_producto_dic(productos, lista_prov, id_prod, nuevo_nombre, nueva_categoria,
                           nuevo_id_proveedor, nuevo_precio):
    """Modifica los datos indicados (los que llegan en None no se cambian)."""

    producto = buscar_producto_dic(productos, id_prod)

    if producto is None:
        raise ValueError("Producto no encontrado.")

    if nuevo_nombre is not None:
        if not proveedores.validar_nombre(nuevo_nombre.strip()):
            raise ValueError("El nombre es inválido.")
        producto["nombre"] = capitalizar(nuevo_nombre)

    if nueva_categoria is not None:
        if not proveedores.validar_nombre(nueva_categoria.strip()):
            raise ValueError("La categoría es inválida.")
        producto["categoria"] = capitalizar(nueva_categoria)

    if nuevo_id_proveedor is not None:
        if proveedores.buscar_proveedor_por_id(lista_prov, nuevo_id_proveedor) is None:
            raise ValueError("No existe un proveedor con ese ID.")
        producto["id_proveedor"] = nuevo_id_proveedor

    if nuevo_precio is not None:
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        producto["precio"] = nuevo_precio


# Eliminar producto
def eliminar_producto_dic(productos, id_prod):
    if id_prod not in productos:
        raise ValueError("Producto no encontrado.")

    del productos[id_prod]


# Categorías
def categorias_unicas(productos):
    """Conjunto de categorías. Se calcula a partir de los productos,
    así al eliminar uno no quedan categorías que ya no existen."""
    categorias = set()

    for p in productos.values():
        categorias.add(p["categoria"])

    return categorias


# Movimientos
def agregar_movimiento(movimientos, tipo, id_prod, cantidad, fecha):
    """Registra un movimiento en la matriz."""

    if tipo not in ("Ingreso", "Egreso"):
        raise ValueError("Tipo de movimiento inválido.")

    movimientos.append([tipo, id_prod, cantidad, fecha])


def ingreso_stock_dic(productos, movimientos, id_prod, cantidad, fecha):
    """Suma stock y registra el movimiento. Primero valida todo y después modifica,
    así no queda el stock cambiado sin su movimiento."""

    producto = buscar_producto_dic(productos, id_prod)

    if producto is None:
        raise ValueError("Producto no encontrado.")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")

    producto["stock"] += cantidad
    agregar_movimiento(movimientos, "Ingreso", id_prod, cantidad, fecha)


def movimientos_de_producto(movimientos, id_prod):
    """Relación producto (A) -> movimientos (B)."""
    return [m for m in movimientos if m[1] == id_prod]


def contar_movimientos_recursivo(movimientos, tipo, i=0):
    """Cuenta en forma recursiva cuántos movimientos hay de un tipo.
    Caso base: se recorrió toda la matriz."""

    if i == len(movimientos):
        return 0

    suma = 0
    if movimientos[i][0] == tipo:
        suma = 1

    return suma + contar_movimientos_recursivo(movimientos, tipo, i + 1)


# Mostrar
def mostrar_productos_dic(productos, lista_prov):
    """Muestra los productos en formato de tabla."""

    if len(productos) == 0:
        print("No hay productos cargados.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")
    print("-" * 90)
    print(f"{'ID':<8} {'Nombre':<18} {'Categoria':<15} {'Proveedor':<18} {'Stock':<8} {'Precio':>12}")
    print("-" * 90)

    for id_prod, p in productos.items():
        nombre_prov = proveedores.nombre_proveedor(lista_prov, p["id_proveedor"])
        print(f"{id_prod:<8} {p['nombre'][:18]:<18} {p['categoria'][:15]:<15} "
              f"{nombre_prov[:18]:<18} {p['stock']:<8} ${p['precio']:>11.2f}")

    print("-" * 90)


def mostrar_movimientos(movimientos, productos):
    """Muestra los movimientos registrados en formato de tabla."""

    if len(movimientos) == 0:
        print("No hay movimientos registrados.")
        return

    print("\n--- MOVIMIENTOS ---")
    print("-" * 65)
    print(f"{'Tipo':<10} {'ID Prod':<10} {'Producto':<20} {'Cantidad':<10} {'Fecha':<12}")
    print("-" * 65)

    for m in movimientos:
        producto = buscar_producto_dic(productos, m[1])

        if producto is None:
            nombre = "Eliminado"
        else:
            nombre = producto["nombre"]

        dia, mes, anio = m[3]
        fecha = f"{dia}/{mes}/{anio}"
        print(f"{m[0]:<10} {m[1]:<10} {nombre[:20]:<20} {m[2]:<10} {fecha:<12}")

    print("-" * 65)
