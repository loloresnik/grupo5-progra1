from functools import reduce

# Registrar venta
def registrar_venta(ventas_dic, productos_dic, id_prod, cantidad):
    producto = None
    for p in productos_dic:
        if p["id"] == id_prod:
            producto = p
            break

    if producto is None:
        print("Producto no encontrado.")
        return 0

    if cantidad > producto["stock"]:
        print("Stock insuficiente.")
        return 0

    producto["stock"] -= cantidad

    if id_prod in ventas_dic:
        ventas_dic[id_prod] += cantidad
    else:
        ventas_dic[id_prod] = cantidad

    print("Venta registrada correctamente.")
    return 1


# Mostrar ventas
def mostrar_ventas(ventas_dic, productos_dic):
    if len(ventas_dic) == 0:
        print("No hay ventas registradas.")
        return

    print("\n--- LISTA DE VENTAS ---")
    print("-" * 60)
    print("ID Producto     Nombre           Cantidad Vendida")
    print("-" * 60)

    for id_prod in ventas_dic:
        cantidad = ventas_dic[id_prod]
        nombre = "Desconocido"

        for p in productos_dic:
            if p["id"] == id_prod:
                nombre = p["nombre"]
                break

        print(f"{id_prod:<15} {nombre:<15} {cantidad:<10}")

    print("-" * 60)


# Ventas totales
def ventas_totales(ventas_dic):
    total = 0
    for id_prod in ventas_dic:
        total += ventas_dic[id_prod]
    return total


# Top 3 más vendidos
def top_mas_vendidos(ventas_dic, productos_dic):
    lista = []

    for id_prod in ventas_dic:
        cantidad = ventas_dic[id_prod]
        nombre = None

        for p in productos_dic:
            if p["id"] == id_prod:
                nombre = p["nombre"]
                break

        lista.append((cantidad, nombre))

    lista_ordenada = sorted(lista, reverse=True)[:3]

    return [nombre for cantidad, nombre in lista_ordenada]


# Top 3 menos vendidos
def menos_vendidos(ventas_dic, productos_dic):
    lista = []

    for id_prod in ventas_dic:
        cantidad = ventas_dic[id_prod]
        nombre = None

        for p in productos_dic:
            if p["id"] == id_prod:
                nombre = p["nombre"]
                break

        lista.append((cantidad, nombre))

    lista_ordenada = sorted(lista)[:3]

    return [nombre for cantidad, nombre in lista_ordenada]


# Recaudación total
def recaudacion_total(ventas_dic, productos_dic):
    total = 0

    for id_prod in ventas_dic:
        cantidad = ventas_dic[id_prod]

        for p in productos_dic:
            if p["id"] == id_prod:
                total += cantidad * p["precio"]
                break

    return total


# Producto más caro
def producto_mas_caro(productos_dic):
    if len(productos_dic) == 0:
        return None

    mayor = productos_dic[0]

    for p in productos_dic:
        if p["precio"] > mayor["precio"]:
            mayor = p

    return mayor


# Producto menos caro
def producto_menos_caro(productos_dic):
    if len(productos_dic) == 0:
        return None

    menor = productos_dic[0]

    for p in productos_dic:
        if p["precio"] < menor["precio"]:
            menor = p

    return menor


# Valor total del stock
def valor_total_stock(productos_dic):
    total = 0
    for p in productos_dic:
        total += p["stock"] * p["precio"]
    return total


# Valor por categoría
def valor_por_categoria(productos_dic):
    categorias = {}

    for p in productos_dic:
        cat = p["categoria"]
        valor = p["stock"] * p["precio"]

        if cat in categorias:
            categorias[cat] += valor
        else:
            categorias[cat] = valor

    return categorias


# Porcentaje del valor por categoría
def porcentaje_valor_por_categoria(productos_dic):
    total = valor_total_stock(productos_dic)

    if total == 0:
        return {}

    valores = valor_por_categoria(productos_dic)
    porcentajes = {}

    for cat in valores:
        porcentaje = (valores[cat] / total) * 100
        porcentaje = round(porcentaje, 2) 
        porcentajes[cat] = porcentaje

    return porcentajes


# Buscar por proveedor
def buscar_por_proveedor(productos_dic, proveedor):
    proveedor = proveedor.lower()
    resultado = []

    for p in productos_dic:
        if p["proveedor"].lower() == proveedor:
            resultado.append(p)

    return resultado


# Buscar por categoría
def buscar_por_categoria(productos_dic, categoria):
    categoria = categoria.lower()
    resultado = []

    for p in productos_dic:
        if p["categoria"].lower() == categoria:
            resultado.append(p)

    return resultado


# Promedio de precio
def promedio_precio(productos_dic):
    if len(productos_dic) == 0:
        return 0

    total = 0
    for p in productos_dic:
        total += p["precio"]

    return total / len(productos_dic)


# precios con IVA
def precios_con_iva(productos_dic):
    return list(map(lambda p: p["precio"] * 1.21, productos_dic))


# valor total del inventario
def valor_total_reduce(productos_dic):
    return reduce(lambda total, p: total + (p["precio"] * p["stock"]), productos_dic, 0)


# productos sin stock
def productos_sin_stock(productos_dic):
    return list(filter(lambda p: p["stock"] == 0, productos_dic))