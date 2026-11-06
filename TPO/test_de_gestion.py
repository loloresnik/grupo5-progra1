import gestion_productos


def crear_proveedores():
    return [
        [10, "Taragui", "11-45678901", "ventas@taragui.com"],
        [20, "Ledesma", "11-22223333", "info@ledesma.com"]
    ]


def crear_productos():
    return {
        1: {"nombre": "Yerba", "categoria": "Almacen", "id_proveedor": 10, "stock": 5, "precio": 1500},
        2: {"nombre": "Azucar", "categoria": "Almacen", "id_proveedor": 20, "stock": 0, "precio": 900}
    }


def test_buscar_producto():
    productos = crear_productos()

    assert gestion_productos.buscar_producto_dic(productos, 1)["nombre"] == "Yerba"
    assert gestion_productos.buscar_producto_dic(productos, 99) is None


def test_eliminar_producto():
    productos = crear_productos()
    ids_unicos = {1, 2}

    assert gestion_productos.eliminar_producto_dic(productos, 1, ids_unicos) == 1
    assert 1 not in productos
    assert 1 not in ids_unicos


    assert gestion_productos.eliminar_producto_dic(productos, 99, ids_unicos) == 0


def test_modificar_con_proveedor_inexistente():
    productos = crear_productos()


    resultado = gestion_productos.modificar_producto_dic(productos, 1, "Yerba Mate", None, 99, None, crear_proveedores())

    assert resultado == 0
    assert productos[1]["nombre"] == "Yerba"
    assert productos[1]["id_proveedor"] == 10
