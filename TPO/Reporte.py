from functools import reduce
import gestion_productos
import proveedores



def registrar_venta(ventas_dic, productos_dic, movimientos, id_prod, cantidad, fecha):
  

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

    if producto is None:
        return "Eliminado"

    return producto["nombre"]


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

    lista = [(cantidad, nombre_producto(productos_dic, id_prod)) for id_prod, cantidad in ventas_dic.items()]
    return sorted(lista, reverse=True)


def top_mas_vendidos(ventas_dic, productos_dic):
    return [nombre for cantidad, nombre in ranking_ventas(ventas_dic, productos_dic)[:3]]



def menos_vendidos(ventas_dic, productos_dic):
    return [nombre for cantidad, nombre in ranking_ventas(ventas_dic, productos_dic)[::-1][:3]]


def recaudacion_total(ventas_dic, productos_dic):
    total = 0

    for id_prod, cantidad in ventas_dic.items():
        producto = gestion_productos.buscar_producto_dic(productos_dic, id_prod)
        if producto is not None:
            total += cantidad * producto["precio"]

    return total



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
    
    return set(ventas_dic.keys()) & set(productos_sin_stock(productos_dic).keys())


def categorias_sin_ventas(ventas_dic, productos_dic):

    categorias_vendidas = set()

    for id_prod in ventas_dic:
        if id_prod in productos_dic:
            categorias_vendidas.add(productos_dic[id_prod]["categoria"])

    return gestion_productos.categorias_unicas(productos_dic) - categorias_vendidas




def resumen_estadistico(productos_dic):


    if len(productos_dic) == 0:
        return {}

    precios = [p["precio"] for p in productos_dic.values()]
    minimo = min(precios)
    maximo = max(precios)

    return {
        "productos": total_registros(productos_dic),
        "categorias": len(gestion_productos.categorias_unicas(productos_dic)),
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
