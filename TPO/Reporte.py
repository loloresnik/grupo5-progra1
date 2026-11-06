from functools import reduce
import json
import gestion_productos
import proveedores
import validaciones



def clave_venta(id_prod, producto):
    """Clave de la venta segun el producto: (ID, nombre).
    Si se borra un producto y se reutiliza su ID con otro producto,
    las ventas nuevas quedan separadas de las viejas."""

    return (id_prod, producto["nombre"])


def registrar_venta(ventas_dic, productos_dic, movimientos, id_prod, cantidad):
    """Registra la venta solo si el movimiento de egreso se pudo registrar.
    Si el movimiento falla, lanza ValueError y no modifica stock, ventas ni recaudacion."""

    producto = gestion_productos.buscar_producto_dic(productos_dic, id_prod)

    if producto is None:
        raise ValueError("Producto no encontrado.")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")

    if cantidad > producto["stock"]:
        raise ValueError(f"Stock insuficiente (disponible: {producto['stock']}).")

    ok = gestion_productos.agregar_movimiento(movimientos, "Egreso", id_prod, cantidad, productos_dic)

    if ok == 0:
        raise ValueError("No se pudo registrar el movimiento. La venta no se realizo.")

    producto["stock"] -= cantidad

    clave = clave_venta(id_prod, producto)

    if clave not in ventas_dic:
        ventas_dic[clave] = {"categoria": producto["categoria"], "cantidad": 0, "recaudado": 0}

    ventas_dic[clave]["cantidad"] += cantidad
    ventas_dic[clave]["recaudado"] += cantidad * producto["precio"]


def nombre_producto(productos_dic, clave):
    """Devuelve el nombre guardado en la venta. Si ese producto ya no existe, lo marca como eliminado."""
    id_prod, nombre = clave
    producto = gestion_productos.buscar_producto_dic(productos_dic, id_prod)

    if producto is None or clave_venta(id_prod, producto) != clave:
        return nombre + " (eliminado)"

    return nombre


def mostrar_ventas(ventas_dic, productos_dic):
    if len(ventas_dic) == 0:
        print("No hay ventas registradas.")
        return

    print("\n--- LISTA DE VENTAS ---")
    print("-" * 65)
    print(f"{'ID Producto':<15} {'Nombre':<20} {'Vendidos':<10} {'Recaudado':>15}")
    print("-" * 65)

    for clave, datos in ventas_dic.items():
        print(f"{clave[0]:<15} {nombre_producto(productos_dic, clave)[:20]:<20} {datos['cantidad']:<10} ${datos['recaudado']:>14}")

    print("-" * 65)


def ventas_totales(ventas_dic):
    return sum(datos["cantidad"] for datos in ventas_dic.values())


def ranking_ventas(ventas_dic, productos_dic, incluir_sin_ventas=False):
    """Lista de tuplas (cantidad, nombre) ordenada de mayor a menor.
    Con incluir_sin_ventas=True agrega los productos actuales que no vendieron nada, con 0."""

    lista = [(datos["cantidad"], nombre_producto(productos_dic, clave)) for clave, datos in ventas_dic.items()]

    if incluir_sin_ventas:
        lista += [(0, p["nombre"]) for id_prod, p in productos_dic.items() if clave_venta(id_prod, p) not in ventas_dic]

    return sorted(lista, reverse=True)


def top_mas_vendidos(ventas_dic, productos_dic):
    return [nombre for cantidad, nombre in ranking_ventas(ventas_dic, productos_dic)[:3]]



def menos_vendidos(ventas_dic, productos_dic):
    return [nombre for cantidad, nombre in ranking_ventas(ventas_dic, productos_dic, True)[::-1][:3]]


def recaudacion_total(ventas_dic):
    """Suma lo recaudado en cada venta con el precio que tenia el producto al venderse,
    asi no cambia si despues se modifica el precio o se elimina el producto."""
    total = 0

    for datos in ventas_dic.values():
        total += datos["recaudado"]

    return total



def guardar_ventas_json(ventas_dic):
    """Guarda las ventas en ventas.json.
    JSON no acepta tuplas como clave, asi que cada venta se guarda como
    un diccionario con el id y el nombre por separado."""

    lista = []

    for clave, datos in ventas_dic.items():
        lista.append({
            "id": clave[0],
            "nombre": clave[1],
            "categoria": datos["categoria"],
            "cantidad": datos["cantidad"],
            "recaudado": datos["recaudado"]
        })

    try:
        archivo = open("ventas.json", "w", encoding="utf-8")
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
        archivo.close()
        return 1

    except (OSError, TypeError) as error:
        print("Error al guardar ventas:", error)
        return 0


def cargar_ventas_json():
    """Carga ventas.json y vuelve a armar la clave (id, nombre) como tupla."""

    try:
        archivo = open("ventas.json", "r", encoding="utf-8")
        lista = json.load(archivo)
        archivo.close()

        ventas_dic = {}

        for venta in lista:
            clave = (int(venta["id"]), venta["nombre"])
            ventas_dic[clave] = {
                "categoria": venta["categoria"],
                "cantidad": venta["cantidad"],
                "recaudado": venta["recaudado"]
            }

        return ventas_dic

    except FileNotFoundError:
        return {}

    except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
        print("Error al cargar ventas:", error)
        return {}



def extremo_recursivo(lista, clave, buscar_mayor):

    if len(lista) == 0:
        return None

    if len(lista) == 1:
        return lista[0]

    extremo_resto = extremo_recursivo(lista[1:], clave, buscar_mayor)

    if buscar_mayor:
        if lista[0][clave] >= extremo_resto[clave]:
            return lista[0]
        return extremo_resto

    if lista[0][clave] <= extremo_resto[clave]:
        return lista[0]
    return extremo_resto


def producto_mas_caro(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "precio", True)


def producto_menos_caro(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "precio", False)


def producto_mayor_stock(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "stock", True)


def producto_menor_stock(productos_dic):
    return extremo_recursivo(list(productos_dic.values()), "stock", False)



def valor_total_stock(productos_dic):
    total = 0
    for p in productos_dic.values():
        total += p["stock"] * p["precio"]
    return total


def valor_total_reduce(productos_dic):
    return reduce(lambda total, p: total + (p["precio"] * p["stock"]), productos_dic.values(), 0)


def valor_total_recursivo(lista_productos):


    if len(lista_productos) == 0:
        return 0

    primero = lista_productos[0]

    return primero["precio"] * primero["stock"] + valor_total_recursivo(lista_productos[1:])




def valor_por_categoria(productos_dic):
    categorias = {}

    for p in productos_dic.values():
        categorias[p["categoria"]] = categorias.get(p["categoria"], 0) + p["stock"] * p["precio"]

    return categorias


def porcentaje_valor_por_categoria(productos_dic):
    total = valor_total_stock(productos_dic)
    porcentajes = {}

    if total == 0:
        return porcentajes

    valores = valor_por_categoria(productos_dic)

    for cat, valor in valores.items():
        porcentajes[cat] = valor / total * 100

    return porcentajes


def total_registros(productos_dic):
    return len(productos_dic)


def conteo_por_categoria(productos_dic):

    conteo = {}

    for p in productos_dic.values():
        conteo[p["categoria"]] = conteo.get(p["categoria"], 0) + 1

    return conteo


def conteo_por_proveedor(productos_dic, lista_prov):

    conteo = {}

    for fila in lista_prov:
        conteo[fila[1]] = 0

    for p in productos_dic.values():
        nombre = proveedores.nombre_proveedor(lista_prov, p["id_proveedor"])
        conteo[nombre] = conteo.get(nombre, 0) + 1

    return conteo


def porcentaje_cantidad_por_categoria(productos_dic):

    total = total_registros(productos_dic)
    porcentajes = {}

    if total == 0:
        return porcentajes

    for cat, cant in conteo_por_categoria(productos_dic).items():
        porcentajes[cat] = cant / total * 100

    return porcentajes


def promedio_precio(productos_dic):
    if len(productos_dic) == 0:
        return 0

    return sum(p["precio"] for p in productos_dic.values()) / len(productos_dic)


def promedio_precio_por_categoria(productos_dic):

    sumas = {}

    for p in productos_dic.values():
        sumas[p["categoria"]] = sumas.get(p["categoria"], 0) + p["precio"]

    conteo = conteo_por_categoria(productos_dic)
    promedios = {}

    for cat in sumas:
        promedios[cat] = sumas[cat] / conteo[cat]

    return promedios


def buscar_por_categoria(productos_dic, categoria):
    categoria = categoria.strip().lower()
    resultado = {}

    for id_prod, p in productos_dic.items():
        if p["categoria"].lower() == categoria:
            resultado[id_prod] = p

    return resultado




def precios_con_iva(productos_dic):

    return list(map(lambda p: (p["nombre"], p["precio"] * 1.21), productos_dic.values()))


def productos_sin_stock(productos_dic):
    return dict(filter(lambda item: item[1]["stock"] == 0, productos_dic.items()))




def productos_vendidos_sin_stock(ventas_dic, productos_dic):
    
    sin_stock = {clave_venta(id_prod, p) for id_prod, p in productos_sin_stock(productos_dic).items()}

    return {clave[0] for clave in set(ventas_dic.keys()) & sin_stock}


def categorias_sin_ventas(ventas_dic, productos_dic):

    categorias_vendidas = set()

    for datos in ventas_dic.values():
        categorias_vendidas.add(datos["categoria"])

    categorias = {p["categoria"] for p in productos_dic.values()}

    return categorias - categorias_vendidas




def resumen_estadistico(productos_dic):


    if len(productos_dic) == 0:
        return {}

    precios = [p["precio"] for p in productos_dic.values()]
    minimo = min(precios)
    maximo = max(precios)

    return {
        "productos": total_registros(productos_dic),
        "categorias": len({p["categoria"] for p in productos_dic.values()}),
        "unidades": sum(p["stock"] for p in productos_dic.values()),
        "valor_total": valor_total_stock(productos_dic),
        "precios": (minimo, maximo, promedio_precio(productos_dic)),
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


def mostrar_tabla(titulo, datos, columna, formato):

    if len(datos) == 0:
        print("No hay datos.")
        return

    print(f"\n--- {titulo} ---")
    print("-" * 40)
    print(f"{'':<5}{'Nombre':<20} {columna:>14}")
    print("-" * 40)

    for clave, valor in datos.items():
        
        print(f"{clave[:3].upper():<5}{clave[:20]:<20} {formato.format(valor):>14}")

    print("-" * 40)


# ============================
# FUNCIONES QUE LLAMA EL MENU
# ============================

# Registrar venta (pide los datos)
def venta(ventas_dic, productos_dic, movimientos):
    """Pide producto y cantidad y registra la venta.
    Si algún dato es inválido, muestra el error y no registra nada."""

    print("\n=== REGISTRAR VENTA ===")

    id_prod = validaciones.pedir_entero("Ingrese ID del producto: ")

    cantidad = validaciones.pedir_entero("Ingrese cantidad: ")

    try:

        registrar_venta(ventas_dic, productos_dic, movimientos, id_prod, cantidad)

    except ValueError as error:

        print("Error:", error)

        return 0

    gestion_productos.guardar_productos_json(productos_dic)

    guardar_ventas_json(ventas_dic)

    print("Venta registrada correctamente.")

    return 1


# Ventas totales
def mostrar_ventas_totales(ventas_dic):

    print(f"Unidades vendidas en total: {ventas_totales(ventas_dic)}")


# Recaudacion
def mostrar_recaudacion(ventas_dic):

    print(f"Recaudación total: ${recaudacion_total(ventas_dic):.2f}")


# Top de productos
def mostrar_top(titulo, nombres):
    """Muestra una lista de nombres numerada."""

    if len(nombres) == 0:

        print("No hay datos.")

        return

    print(f"\n--- {titulo} ---")

    for i in range(len(nombres)):

        print(f"{i + 1}. {nombres[i]}")


def mostrar_mas_vendidos(ventas_dic, productos_dic):

    mostrar_top("TOP 3 MAS VENDIDOS", top_mas_vendidos(ventas_dic, productos_dic))


def mostrar_menos_vendidos(ventas_dic, productos_dic):

    mostrar_top("TOP 3 MENOS VENDIDOS", menos_vendidos(ventas_dic, productos_dic))


# Producto con valor maximo o minimo
def mostrar_producto_extremo(titulo, producto, campo):
    """Muestra el nombre del producto y el valor del campo pedido (precio o stock)."""

    if producto is None:

        print("No hay productos cargados.")

        return

    print(f"{titulo}: {producto['nombre']} ({campo}: {producto[campo]})")


def mostrar_mas_caro(productos_dic):

    mostrar_producto_extremo("Producto más caro", producto_mas_caro(productos_dic), "precio")


def mostrar_mas_barato(productos_dic):

    mostrar_producto_extremo("Producto más barato", producto_menos_caro(productos_dic), "precio")


def mostrar_mayor_stock(productos_dic):

    mostrar_producto_extremo("Producto con mayor stock", producto_mayor_stock(productos_dic), "stock")


def mostrar_menor_stock(productos_dic):

    mostrar_producto_extremo("Producto con menor stock", producto_menor_stock(productos_dic), "stock")


# Valor total del stock
def mostrar_valor_total(productos_dic):
    """Muestra el valor total del stock calculado de tres formas:
    con un ciclo, con reduce y con recursividad. Las tres deben coincidir."""

    print("\n--- VALOR TOTAL DEL STOCK ---")
    print(f"Con ciclo for:      ${valor_total_stock(productos_dic):.2f}")
    print(f"Con reduce:         ${valor_total_reduce(productos_dic):.2f}")
    print(f"Con recursividad:   ${valor_total_recursivo(list(productos_dic.values())):.2f}")


# Precios con IVA
def mostrar_precios_con_iva(productos_dic):

    precios = precios_con_iva(productos_dic)

    if len(precios) == 0:

        print("No hay productos cargados.")

        return

    print("\n--- PRECIOS CON IVA (21%) ---")

    for nombre, precio in precios:

        print(f"{nombre[:20]:<20} ${precio:>10.2f}")


# Productos sin stock
def mostrar_productos_sin_stock(productos_dic, proveedores_lista):

    print("\n=== PRODUCTOS SIN STOCK ===")

    gestion_productos.mostrar_productos_dic(productos_sin_stock(productos_dic), proveedores_lista)


# Productos vendidos que se quedaron sin stock (interseccion de conjuntos)
def mostrar_vendidos_sin_stock(ventas_dic, productos_dic):

    ids = productos_vendidos_sin_stock(ventas_dic, productos_dic)

    if len(ids) == 0:

        print("No hay productos vendidos sin stock.")

        return

    print("\n--- VENDIDOS Y SIN STOCK (reponer) ---")

    for id_prod in sorted(ids):

        print(f"{id_prod:<8} {productos_dic[id_prod]['nombre']}")


# Cantidad de productos por proveedor
def mostrar_conteo_por_proveedor(productos_dic, proveedores_lista):

    mostrar_tabla("PRODUCTOS POR PROVEEDOR", conteo_por_proveedor(productos_dic, proveedores_lista), "Productos", "{}")


# ============================
# CATEGORIAS
# ============================

def mostrar_categorias(productos_dic):
    """Muestra las categorías sin repetir, usando un conjunto."""

    categorias = set()

    for p in productos_dic.values():

        categorias.add(p["categoria"])

    if len(categorias) == 0:

        print("No hay categorías registradas.")

        return

    print("\n--- CATEGORIAS ---")

    for cat in sorted(categorias):

        print("-", cat)


def mostrar_productos_por_categoria(productos_dic, proveedores_lista):

    categoria = validaciones.pedir_texto("Ingrese categoría: ")

    resultado = buscar_por_categoria(productos_dic, categoria)

    gestion_productos.mostrar_productos_dic(resultado, proveedores_lista)


def mostrar_valor_por_categoria(productos_dic):

    mostrar_tabla("VALOR POR CATEGORIA", valor_por_categoria(productos_dic), "Valor", "${:.2f}")


def mostrar_porcentaje_valor_por_categoria(productos_dic):

    mostrar_tabla("PORCENTAJE DEL VALOR POR CATEGORIA", porcentaje_valor_por_categoria(productos_dic), "Porcentaje", "{:.2f}%")


def mostrar_cantidad_por_categoria(productos_dic):

    print(f"\nTotal de productos registrados: {total_registros(productos_dic)}")

    mostrar_tabla("PRODUCTOS POR CATEGORIA", conteo_por_categoria(productos_dic), "Cantidad", "{}")

    mostrar_tabla("PORCENTAJE DE PRODUCTOS POR CATEGORIA", porcentaje_cantidad_por_categoria(productos_dic), "Porcentaje", "{:.2f}%")


def mostrar_promedio_por_categoria(productos_dic):

    print(f"\nPrecio promedio general: ${promedio_precio(productos_dic):.2f}")

    mostrar_tabla("PRECIO PROMEDIO POR CATEGORIA", promedio_precio_por_categoria(productos_dic), "Promedio", "${:.2f}")


# Categorias sin ventas (diferencia de conjuntos)
def mostrar_categorias_sin_ventas(ventas_dic, productos_dic):

    categorias = categorias_sin_ventas(ventas_dic, productos_dic)

    if len(categorias) == 0:

        print("Todas las categorías tienen ventas.")

        return

    print("\n--- CATEGORIAS SIN VENTAS ---")

    for cat in sorted(categorias):

        print("-", cat)
