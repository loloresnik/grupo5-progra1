import Reporte


def crear_productos():
    """Productos de prueba.
    Valor total del stock: 15*85000 + 30*25000 + 0*850000 = 2025000."""
    return {
        101: {"nombre": "Teclado Mecánico", "categoria": "Periféricos", "id_proveedor": 4, "stock": 15, "precio": 85000},
        102: {"nombre": "Mouse Inalámbrico", "categoria": "Periféricos", "id_proveedor": 4, "stock": 30, "precio": 25000},
        106: {"nombre": "Placa de Video", "categoria": "Componentes", "id_proveedor": 2, "stock": 0, "precio": 850000}
    }


def test_valor_total_de_las_tres_formas():
    productos = crear_productos()

   
    assert Reporte.valor_total_stock(productos) == 2025000
    assert Reporte.valor_total_reduce(productos) == 2025000
    assert Reporte.valor_total_recursivo(list(productos.values())) == 2025000
    assert Reporte.valor_total_stock({}) == 0


def test_promedio_y_conteo_por_categoria():
    productos = crear_productos()

    
    assert Reporte.promedio_precio_por_categoria(productos) == {"Periféricos": 55000, "Componentes": 850000}
    assert Reporte.conteo_por_categoria(productos) == {"Periféricos": 2, "Componentes": 1}


def test_venta_con_stock_insuficiente_no_modifica_nada():
    productos = crear_productos()
    ventas = {}
    movimientos = []

    try:
        
        Reporte.registrar_venta(ventas, productos, movimientos, 101, 20)
        assert False  
    except ValueError:
        assert productos[101]["stock"] == 15
        assert ventas == {}
        assert movimientos == []
