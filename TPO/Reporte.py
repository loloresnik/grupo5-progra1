from functools import reduce
import gestion_productos
import proveedores as prov

# Las ventas se guardan en un diccionario: {id_producto: cantidad_vendida}


# ============================
# VENTAS
# ============================

def registrar_venta(ventas_dic, productos_dic, movimientos, id_prod, cantidad, fecha):
    """Descuenta stock, acumula la venta y registra un movimiento de Egreso."""

    producto = gestion_productos.buscar_producto_dic(productos_dic, id_prod)

    if producto is None:
        raise ValueError("Producto no encontrado.")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")

    if cantidad > producto["stock"]:
        raise ValueError(f"Stock insuficiente (disponible: {producto['stock']}).")

    producto["stock"] -= cantidad
    ventas_dic[id_prod] = ventas_dic.get(id_prod, 0) + cantidad
    gestion_productos.agregar_movimiento(movimientos, "Egreso", id_prod, cantidad, fecha)


def nombre_producto(productos_dic, id_prod):
    producto = gestion_productos.buscar_producto_dic(productos_dic, id_prod)
    return producto["nombre"] if producto else "Eliminado"


def mostrar_ventas(ventas_dic, productos_dic):
    if len(ventas_dic) == 0:
        print("No hay ventas registradas.")
        return

    print("\n--- LISTA DE VENTAS ---")
    print("-" * 50)
    print(f"{'ID Producto':<15} {'Nombre':<20} {'Vendidos':<10}")
    print("-" * 50)

    for id_prod, cantidad in ventas_dic.items():
        print(f"{id_prod:<15} {nombre_producto(productos_dic, id_prod)[:20]:<20} {cantidad:<10}")

    print("-" * 50)


def ventas_totales(ventas_dic):
    return sum(ventas_dic.values())


def ranking_ventas(ventas_dic, productos_dic):
    """Lista de tuplas (cantidad, nombre) ordenada de mayor a menor."""
    lista = [(cantidad, nombre_producto(productos_dic, id_prod)) for id_prod, cantidad in ventas_dic.items()]
    return sorted(lista, reverse=True)


# Top 3 más vendidos
def top_mas_vendidos(ventas_dic, productos_dic):
    return [nombre for cantidad, nombre in ranking_ventas(ventas_dic, productos_dic)[:3]]


# Top 3 menos vendidos
def menos_vendidos(ventas_dic, productos_dic):
    return [nombre for cantidad, nombre in ranking_ventas(ventas_dic, productos_dic)[::-1][:3]]


def recaudacion_total(ventas_dic, productos_dic):
    total = 0

    for id_prod, cantidad in ventas_dic.items():
        producto = gestion_productos.buscar_producto_dic(productos_dic, id_prod)
        if producto is not None:
            total += cantidad * producto["precio"]

    return total


# ============================
# MÁXIMOS Y MÍNIMOS (RECURSIVO)
# ============================

def extremo_recursivo(lista, clave, buscar_mayor=True):
    """Devuelve el elemento con el mayor (o menor) valor en la clave indicada.
    Caso base: lista con un solo elemento.
    Caso recursivo: se compara el primero con el extremo del resto de la lista."""

    if len(lista) == 0:
        return None

    if len(lista) == 1:
        return lista[0]

    extremo_resto = extremo_recursivo(lista[1:], clave, buscar_mayor)

    if buscar_mayor:
        return lista[0] if lista[0][clave] >= extremo_resto[clave] else extremo_resto

    return lista[0] if lista[0][clave] <= extremo_resto[clave] else extremo_resto


def producto_mas_caro(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "precio", True)


def producto_menos_caro(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "precio", False)


def producto_mayor_stock(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "stock", True)


def producto_menor_stock(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "stock", False)


# ============================
# VALOR DEL INVENTARIO
# ============================

def valor_total_stock(productos_dic):
    total = 0
    for p in productos_dic.values():
        total += p["stock"] * p["precio"]
    return total


def valor_total_reduce(productos_dic):
    return reduce(lambda total, p: total + (p["precio"] * p["stock"]), productos_dic.values(), 0)


def valor_total_recursivo(lista_productos):
    """Suma precio * stock de forma recursiva.
    Caso base: lista vacía (vale 0)."""

    if len(lista_productos) == 0:
        return 0

    primero = lista_productos[0]

    return primero["precio"] * primero["stock"] + valor_total_recursivo(lista_productos[1:])


# ============================
# ESTADÍSTICAS POR CATEGORÍA Y PROVEEDOR
# ============================

def valor_por_categoria(productos_dic):
    categorias = {}

    for p in productos_dic.values():
        categorias[p["categoria"]] = categorias.get(p["categoria"], 0) + p["stock"] * p["precio"]

    return categorias


def porcentaje_valor_por_categoria(productos_dic):
    total = valor_total_stock(productos_dic)

    if total == 0:
        return {}

    valores = valor_por_categoria(productos_dic)

    return {cat: round(valor / total * 100, 2) for cat, valor in valores.items()}


def total_registros(productos_dic):
    return len(productos_dic)


def conteo_por_categoria(productos_dic):
    """Cantidad de productos de cada categoría."""
    conteo = {}

    for p in productos_dic.values():
        conteo[p["categoria"]] = conteo.get(p["categoria"], 0) + 1

    return conteo


def conteo_por_proveedor(productos_dic, proveedores):
    """Cantidad de productos de cada proveedor (los que no tienen productos cuentan 0)."""
    conteo = {fila[1]: 0 for fila in proveedores}

    for p in productos_dic.values():
        nombre = prov.nombre_proveedor(proveedores, p["id_proveedor"])
        conteo[nombre] = conteo.get(nombre, 0) + 1

    return conteo


def porcentaje_cantidad_por_categoria(productos_dic):
    """Porcentaje de productos de cada categoría sobre el total."""
    total = total_registros(productos_dic)

    if total == 0:
        return {}

    return {cat: round(cant / total * 100, 2) for cat, cant in conteo_por_categoria(productos_dic).items()}


def promedio_precio(productos_dic):
    if len(productos_dic) == 0:
        return 0

    return sum(p["precio"] for p in productos_dic.values()) / len(productos_dic)


def promedio_precio_por_categoria(productos_dic):
    """Promedio de precio de los productos de cada categoría."""
    sumas = {}

    for p in productos_dic.values():
        sumas[p["categoria"]] = sumas.get(p["categoria"], 0) + p["precio"]

    conteo = conteo_por_categoria(productos_dic)

    return {cat: round(sumas[cat] / conteo[cat], 2) for cat in sumas}


def buscar_por_categoria(productos_dic, categoria):
    categoria = categoria.strip().lower()
    return {id_prod: p for id_prod, p in productos_dic.items() if p["categoria"].lower() == categoria}


# ============================
# LAMBDA: MAP Y FILTER
# ============================

def precios_con_iva(productos_dic):
    """Lista de tuplas (nombre, precio con IVA)."""
    return list(map(lambda p: (p["nombre"], round(p["precio"] * 1.21, 2)), productos_dic.values()))


def productos_sin_stock(productos_dic):
    return dict(filter(lambda item: item[1]["stock"] == 0, productos_dic.items()))


# ============================
# OPERACIONES ENTRE CONJUNTOS
# ============================

def productos_vendidos_sin_stock(ventas_dic, productos_dic):
    """Intersección: productos que se vendieron y hoy no tienen stock (hay que reponer)."""
    return set(ventas_dic) & set(productos_sin_stock(productos_dic))


def categorias_sin_ventas(ventas_dic, productos_dic):
    """Diferencia: categorías que no tuvieron ninguna venta."""
    categorias_vendidas = {productos_dic[i]["categoria"] for i in ventas_dic if i in productos_dic}
    return gestion_productos.categorias_unicas(productos_dic) - categorias_vendidas


# ============================
# RESUMEN ESTADÍSTICO
# ============================

def resumen_estadistico(productos_dic):
    """Devuelve un diccionario con el resumen del inventario.
    El rango de precios se guarda en una tupla (minimo, maximo, promedio) porque no se modifica."""

    if len(productos_dic) == 0:
        return {}

    precios = [p["precio"] for p in productos_dic.values()]
    minimo, maximo = min(precios), max(precios)

    return {
        "productos": total_registros(productos_dic),
        "categorias": len(gestion_productos.categorias_unicas(productos_dic)),
        "unidades": sum(p["stock"] for p in productos_dic.values()),
        "valor_total": valor_total_stock(productos_dic),
        "precios": (minimo, maximo, round(promedio_precio(productos_dic), 2)),
        "rango_precios": maximo - minimo,
        "sin_stock": len(productos_sin_stock(productos_dic))
    }


def mostrar_resumen(productos_dic):
    resumen = resumen_estadistico(productos_dic)

    if len(resumen) == 0:
        print("No hay productos cargados.")
        return

    minimo, maximo, promedio = resumen["precios"]

    print("\n--- RESUMEN ESTADISTICO ---")
    print("-" * 40)
    print(f"{'Productos registrados':<28} {resumen['productos']:>10}")
    print(f"{'Categorias':<28} {resumen['categorias']:>10}")
    print(f"{'Unidades en stock':<28} {resumen['unidades']:>10}")
    print(f"{'Productos sin stock':<28} {resumen['sin_stock']:>10}")
    print(f"{'Valor total':<28} ${resumen['valor_total']:>9.2f}")
    print(f"{'Precio minimo':<28} ${minimo:>9.2f}")
    print(f"{'Precio maximo':<28} ${maximo:>9.2f}")
    print(f"{'Precio promedio':<28} ${promedio:>9.2f}")
    print(f"{'Rango de precios':<28} ${resumen['rango_precios']:>9.2f}")
    print("-" * 40)


def mostrar_tabla(titulo, datos, columna, formato="{}"):
    """Imprime un diccionario {clave: valor} como tabla de dos columnas."""

    if len(datos) == 0:
        print("No hay datos.")
        return

    print(f"\n--- {titulo} ---")
    print("-" * 40)
    print(f"{'':<5}{'Nombre':<20} {columna:>14}")
    print("-" * 40)

    for clave, valor in datos.items():
        # Código corto de 3 letras tomado con rebanadas
        print(f"{clave[:3].upper():<5}{clave[:20]:<20} {formato.format(valor):>14}")

    print("-" * 40)
