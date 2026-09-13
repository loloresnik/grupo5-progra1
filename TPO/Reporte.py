def ventas_totales(inventario):
    return sum(item[2] for item in inventario.values())


def top_mas_vendidos(inventario):
    lista_para_ordenar = []
    for nombre, datos in inventario.items():
        lista_para_ordenar.append((datos[2], nombre))
    
    lista_ordenada = sorted(lista_para_ordenar)[::-1][:3]
    return tuple(nombre for cantidad, nombre in lista_ordenada)


def menos_vendidos(inventario):
    lista_para_ordenar = []
    for nombre, datos in inventario.items():
        lista_para_ordenar.append((datos[2], nombre))
        
    lista_ordenada = sorted(lista_para_ordenar)[:3]
    return tuple(nombre for cantidad, nombre in lista_ordenada)


def productos_mas_caros(inventario):
    lista_para_ordenar = []
    for nombre, datos in inventario.items():
        lista_para_ordenar.append((datos[0], nombre))
        
    lista_ordenada = sorted(lista_para_ordenar)[::-1][:3]
    return tuple(nombre for precio, nombre in lista_ordenada)


def productos_menos_caros(inventario):
    lista_para_ordenar = []
    for nombre, datos in inventario.items():
        lista_para_ordenar.append((datos[0], nombre))
        
    lista_ordenada = sorted(lista_para_ordenar)[:3]
    return tuple(nombre for precio, nombre in lista_ordenada)


def recaudacion_total(inventario):
    return sum(item[0] * item[2] for item in inventario.values())


def buscar_por_proveedor(inventario, proveedor):
    elementos_filtrados = filter(lambda item: item[1][4].lower() == proveedor.lower(), inventario.items())
    resultados = list(elementos_filtrados)
    return resultados


def buscar_por_categoria(inventario, categoria):
    elementos_filtrados = filter(lambda item: item[1][3].lower() == categoria.lower(), inventario.items())
    resultados = list(elementos_filtrados)
    return resultados


def total_stock(inventario):
    return sum(datos[1] for datos in inventario.values())


def porcentaje_stock_por_proveedor(inventario):
    total_absoluto = sum(map(lambda fila: fila[1], inventario.values()))

    if total_absoluto == 0:
        return []

    proveedores_unicos = []
    for fila in inventario.values():
        if fila[4] not in proveedores_unicos:
            proveedores_unicos.append(fila[4])

    estadisticas = []
    for prov in proveedores_unicos:
        productos_prov = filter(lambda fila: fila[4] == prov, inventario.values())
        stock_proveedor = sum(map(lambda fila: fila[1], productos_prov))

        porcentaje = (stock_proveedor / total_absoluto) * 100
        estadisticas.append([prov, round(porcentaje, 2)])

    return sorted(estadisticas, key=lambda fila: fila[1])[::-1]
