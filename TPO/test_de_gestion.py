import gestion_productos


def crear_proveedores():
    return [
        [2, "Megabyte Mayorista", "11-43219876", "pedidos@megabyte.com.ar"],
        [4, "Periféricos Express", "351-4208200", "ventas@perifericosexpress.com"]
    ]


def crear_productos():
    return {
        101: {"nombre": "Teclado Mecánico", "categoria": "Periféricos", "id_proveedor": 4, "stock": 15, "precio": 85000},
        106: {"nombre": "Placa de Video", "categoria": "Componentes", "id_proveedor": 2, "stock": 0, "precio": 850000}
    }


def test_buscar_producto():
    productos = crear_productos()

    assert gestion_productos.buscar_producto_dic(productos, 101)["nombre"] == "Teclado Mecánico"
    assert gestion_productos.buscar_producto_dic(productos, 999) is None


def test_eliminar_producto():
    productos = crear_productos()
    ids_unicos = {101, 106}

    assert gestion_productos.eliminar_producto_dic(productos, 101, ids_unicos) == 1
    assert 101 not in productos
    assert 101 not in ids_unicos

   
    assert gestion_productos.eliminar_producto_dic(productos, 999, ids_unicos) == 0


def test_modificar_con_proveedor_inexistente():
    productos = crear_productos()

    
    resultado = gestion_productos.modificar_producto_dic(productos, 101, "Teclado Gamer", None, 99, None, crear_proveedores())

    assert resultado == 0
    assert productos[101]["nombre"] == "Teclado Mecánico"
    assert productos[101]["id_proveedor"] == 4
