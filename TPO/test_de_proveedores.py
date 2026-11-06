import proveedores


def crear_proveedores():
    """Matriz de proveedores de prueba."""
    return [
        [1, "Tecno Sur Distribuidora", "11-45678901", "ventas@tecnosur.com.ar"],
        [2, "Megabyte Mayorista", "11-43219876", "pedidos@megabyte.com.ar"],
        [4, "Periféricos Express", "351-4208200", "ventas@perifericosexpress.com"]
    ]


def crear_productos():
    """Productos de prueba relacionados con los proveedores por ID."""
    return {
        101: {"nombre": "Teclado Mecánico", "categoria": "Periféricos", "id_proveedor": 4, "stock": 15, "precio": 85000},
        106: {"nombre": "Placa de Video", "categoria": "Componentes", "id_proveedor": 2, "stock": 0, "precio": 850000}
    }


def test_buscar_proveedor_por_id():
    lista = crear_proveedores()


    assert proveedores.buscar_proveedor_por_id(lista, 1) == lista[0]
    assert proveedores.buscar_proveedor_por_id(lista, 4) == lista[2]
    assert proveedores.buscar_proveedor_por_id(lista, 99) is None


def test_agregar_proveedor_con_id_repetido():
    lista = crear_proveedores()

    try:
        proveedores.agregar_proveedor(lista, 1, "Byte Center", "11-46667788", "byte@bytecenter.com")
        assert False  
    except ValueError:
        assert len(lista) == 3


def test_no_elimina_proveedor_con_productos():
    lista = crear_proveedores()
    productos = crear_productos()

    try:
       
        proveedores.eliminar_proveedor(lista, 4, productos)
        assert False  
    except ValueError:
        
        assert proveedores.buscar_proveedor_por_id(lista, 4) is not None
