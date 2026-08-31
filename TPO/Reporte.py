def ventas_totales(inventario):
    """Devuelve la suma total de unidades vendidas de todos los productos."""
    return sum(map(lambda item: item[3], inventario))

# Instrucciones: recibe una lista de productos y suma las ventas de cada uno.
# Esta función calcula el total de unidades vendidas en el inventario.


def top_mas_vendidos(inventario):
    """Devuelve los 3 productos con mayor cantidad vendida, ordenados de mayor a menor."""
    return sorted(inventario, key=lambda item: item[3])[-3:][::-1]

# Instrucciones: ordena los productos por ventas y devuelve los tres mejores.
# Sirve para ver qué artículos se venden más.


def menos_vendidos(inventario):
    """Devuelve los 3 productos con menor cantidad vendida, ordenados de menor a mayor."""
    return sorted(inventario, key=lambda item: item[3])[:3]

# Instrucciones: ordena los productos por ventas y muestra los tres menos vendidos.
# Ayuda a identificar productos con menor demanda.


def productos_mas_caros(inventario):
    """Devuelve los 3 productos más costosos, ordenados del más caro al más barato."""
    return sorted(inventario, key=lambda item: item[1])[-3:][::-1]

# Instrucciones: ordena los productos por precio y obtiene los tres más caros.
# Se usa para comparar artículos de mayor valor.


def productos_menos_caros(inventario):
    """Devuelve los 3 productos más baratos, ordenados del más barato al más caro."""
    return sorted(inventario, key=lambda item: item[1])[:3]

# Instrucciones: ordena por precio y muestra los tres productos más económicos.
# Sirve para detectar opciones de menor costo.


def recaudacion_total(inventario):
    """Calcula el total recaudado multiplicando precio por unidades vendidas."""
    return sum(map(lambda item: item[1] * item[3], inventario))

# Instrucciones: multiplica el precio de cada producto por las ventas realizadas.
# Esta función devuelve la ganancia total generada por el inventario.


def buscar_por_proveedor(inventario, proveedor):
    """Filtra los productos cuyo proveedor coincide con el nombre recibido."""
    return list(filter(lambda fila: fila[5].lower() == proveedor.lower(), inventario))

# Instrucciones: compara el proveedor ingresado con cada fila del inventario.
# Devuelve todos los productos asociados a ese proveedor.


def buscar_por_categoria(inventario, categoria):
    """Filtra los productos que pertenecen a la categoría indicada."""
    return list(filter(lambda fila: fila[4].lower() == categoria.lower(), inventario))

# Instrucciones: busca los elementos según la categoría especificada.
# Permite obtener solo los productos de una misma clasificación.


def total_stock(inventario):
    """Suma la cantidad total disponible en stock de todos los productos."""
    return sum(map(lambda fila: fila[2], inventario))

# Instrucciones: suma todas las cantidades en stock del inventario.
# Sirve para conocer la cantidad total disponible.


def porcentaje_stock_por_proveedor(inventario):
    """Calcula qué porcentaje del stock total pertenece a cada proveedor."""
    total_absoluto = sum(map(lambda fila: fila[2], inventario))

    if total_absoluto == 0:
        return []

    proveedores_unicos = []
    for fila in inventario:
        if fila[5] not in proveedores_unicos:
            proveedores_unicos.append(fila[5])

    estadisticas = []
    for prov in proveedores_unicos:
        productos_prov = filter(lambda fila: fila[5] == prov, inventario)
        stock_proveedor = sum(map(lambda fila: fila[2], productos_prov))

        porcentaje = (stock_proveedor / total_absoluto) * 100
        estadisticas.append([prov, round(porcentaje, 2)])

    return sorted(estadisticas, key=lambda fila: fila[1])[::-1]

# Instrucciones: reúne el stock por proveedor y calcula su porcentaje sobre el total.
# Muestra qué parte del inventario corresponde a cada uno.

# Estructura de la matriz (Índices)
# [0] Nombre | [1] Precio | [2] Stock | [3] Cantidad Vendida | [4] Categoría | [5] Proveedor

# Horas perdidas en este codigo: 6