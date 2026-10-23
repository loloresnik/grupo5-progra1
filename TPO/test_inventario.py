import os
import shutil
import tempfile
import unittest

import gestion_productos
import proveedores
import Reporte
import empleados
import archivos
import validaciones


def datos_de_prueba():
    """Crea un inventario chico para usar en cada prueba."""

    lista_prov = [
        [1, "Logitech", "11-45678901", "ventas@logitech.com"],
        [2, "Kingston", "11-40001111", "info@kingston.com.ar"],
        [3, "Sin Productos", "11-40002222", "contacto@vacio.com"]
    ]

    productos = {
        1001: {"nombre": "Mouse", "categoria": "Perifericos", "id_proveedor": 1, "stock": 10, "precio": 100},
        1002: {"nombre": "Teclado", "categoria": "Perifericos", "id_proveedor": 1, "stock": 5, "precio": 300},
        1003: {"nombre": "Pendrive", "categoria": "Almacenamiento", "id_proveedor": 2, "stock": 0, "precio": 200}
    }

    return productos, lista_prov


class TestAltas(unittest.TestCase):

    def setUp(self):
        self.productos, self.proveedores = datos_de_prueba()

    def test_alta_producto_correcta(self):
        gestion_productos.alta_producto(self.productos, self.proveedores, 2000, "monitor ñandú 24HD",
                                        "pantallas", 2, 3, 5000)
        self.assertIn(2000, self.productos)
        self.assertEqual(self.productos[2000]["nombre"], "Monitor ñandú 24HD")

    def test_alta_producto_id_repetido(self):
        with self.assertRaises(ValueError):
            gestion_productos.alta_producto(self.productos, self.proveedores, 1001, "Otro", "Varios", 1, 1, 1)

    def test_alta_producto_proveedor_inexistente(self):
        with self.assertRaises(ValueError):
            gestion_productos.alta_producto(self.productos, self.proveedores, 2001, "Otro", "Varios", 99, 1, 1)

    def test_alta_producto_precio_negativo(self):
        with self.assertRaises(ValueError):
            gestion_productos.alta_producto(self.productos, self.proveedores, 2002, "Otro", "Varios", 1, 1, -5)

    def test_alta_proveedor_mail_invalido(self):
        with self.assertRaises(ValueError):
            proveedores.agregar_proveedor(self.proveedores, 10, "Nuevo", "11-45678901", "mail-sin-arroba")

    def test_alta_proveedor_id_repetido(self):
        with self.assertRaises(ValueError):
            proveedores.agregar_proveedor(self.proveedores, 1, "Nuevo", "11-45678901", "a@b.com")

    def test_alta_empleado_repetido(self):
        usuarios = {"admin": {"clave": "1234", "tipo": "admin"}}
        with self.assertRaises(ValueError):
            empleados.alta_usuario(usuarios, "admin", "abcd")


class TestBusquedas(unittest.TestCase):

    def setUp(self):
        self.productos, self.proveedores = datos_de_prueba()

    def test_buscar_producto_existente(self):
        self.assertEqual(gestion_productos.buscar_producto_dic(self.productos, 1002)["nombre"], "Teclado")

    def test_buscar_producto_inexistente(self):
        self.assertIsNone(gestion_productos.buscar_producto_dic(self.productos, 9999))

    def test_buscar_proveedor_recursivo(self):
        self.assertEqual(proveedores.buscar_proveedor_recursivo(self.proveedores, 2)[1], "Kingston")
        self.assertIsNone(proveedores.buscar_proveedor_recursivo(self.proveedores, 50))

    def test_productos_de_un_proveedor(self):
        resultado = proveedores.buscar_productos_por_proveedor(self.productos, self.proveedores, "logi")
        self.assertEqual(set(resultado), {1001, 1002})

    def test_busqueda_con_caracteres_especiales(self):
        # Con re.escape un "(" no rompe la expresión regular
        self.assertEqual(proveedores.buscar_productos_por_proveedor(self.productos, self.proveedores, "("), {})

    def test_enmascarar_mail(self):
        self.assertEqual(proveedores.enmascarar_mail("ventas@logitech.com"), "ven***@logitech.com")
        self.assertEqual(proveedores.enmascarar_mail("ok@prov.com"), "ok***@prov.com")

    def test_proveedores_sin_productos(self):
        self.assertEqual(proveedores.proveedores_sin_productos(self.proveedores, self.productos), {3})

    def test_no_se_elimina_proveedor_con_productos(self):
        with self.assertRaises(ValueError):
            proveedores.eliminar_proveedor(self.proveedores, 1, self.productos)

    def test_movimientos_de_producto(self):
        movimientos = [["Ingreso", 1001, 5, (1, 1, 2026)], ["Egreso", 1002, 1, (2, 1, 2026)],
                       ["Egreso", 1001, 2, (3, 1, 2026)]]
        self.assertEqual(len(gestion_productos.movimientos_de_producto(movimientos, 1001)), 2)
        self.assertEqual(gestion_productos.contar_movimientos_recursivo(movimientos, "Egreso"), 2)


class TestValidaciones(unittest.TestCase):

    def test_mail(self):
        self.assertTrue(validaciones.validar_mail("ventas@empresa.com.ar"))
        self.assertFalse(validaciones.validar_mail("ventas@empresa"))
        self.assertFalse(validaciones.validar_mail("@empresa.com"))

    def test_telefono(self):
        self.assertTrue(validaciones.validar_telefono("11-45678901"))
        self.assertFalse(validaciones.validar_telefono("telefono"))

    def test_texto_con_tildes_y_enie(self):
        self.assertTrue(validaciones.validar_texto("Cañón Pérez"))
        self.assertFalse(validaciones.validar_texto(""))
        self.assertFalse(validaciones.validar_texto("Hola$%"))

    def test_fecha_valida(self):
        self.assertEqual(validaciones.convertir_fecha("29/02/2024"), (29, 2, 2024))

    def test_fecha_invalida(self):
        with self.assertRaises(ValueError):
            validaciones.convertir_fecha("31/02/2026")
        with self.assertRaises(ValueError):
            validaciones.convertir_fecha("2026-01-01")

    def test_entero_con_letras_vacio_y_negativo(self):
        for texto in ("abc", "", "-3"):
            with self.assertRaises(ValueError):
                validaciones.convertir_entero(texto)


class TestCalculos(unittest.TestCase):

    def setUp(self):
        self.productos, self.proveedores = datos_de_prueba()

    def test_valor_total_tres_formas(self):
        esperado = 10 * 100 + 5 * 300 + 0 * 200
        self.assertEqual(Reporte.valor_total_stock(self.productos), esperado)
        self.assertEqual(Reporte.valor_total_reduce(self.productos), esperado)
        self.assertEqual(Reporte.valor_total_recursivo(list(self.productos.values())), esperado)

    def test_promedio_por_categoria(self):
        promedios = Reporte.promedio_precio_por_categoria(self.productos)
        self.assertEqual(promedios, {"Perifericos": 200, "Almacenamiento": 200})

    def test_conteos(self):
        self.assertEqual(Reporte.total_registros(self.productos), 3)
        self.assertEqual(Reporte.conteo_por_categoria(self.productos), {"Perifericos": 2, "Almacenamiento": 1})
        self.assertEqual(Reporte.conteo_por_proveedor(self.productos, self.proveedores),
                         {"Logitech": 2, "Kingston": 1, "Sin Productos": 0})

    def test_porcentajes_suman_100(self):
        porcentajes = Reporte.porcentaje_cantidad_por_categoria(self.productos)
        self.assertAlmostEqual(sum(porcentajes.values()), 100, places=1)

    def test_maximos_y_minimos(self):
        self.assertEqual(Reporte.producto_mas_caro(self.productos)["nombre"], "Teclado")
        self.assertEqual(Reporte.producto_menos_caro(self.productos)["nombre"], "Mouse")
        self.assertEqual(Reporte.producto_menor_stock(self.productos)["nombre"], "Pendrive")

    def test_venta_descuenta_stock_y_registra_egreso(self):
        ventas, movimientos = {}, []
        Reporte.registrar_venta(ventas, self.productos, movimientos, 1001, 4, (1, 10, 2026))
        self.assertEqual(self.productos[1001]["stock"], 6)
        self.assertEqual(ventas[1001], 4)
        self.assertEqual(movimientos[0][0], "Egreso")

    def test_venta_sin_stock_suficiente(self):
        with self.assertRaises(ValueError):
            Reporte.registrar_venta({}, self.productos, [], 1003, 1, (1, 10, 2026))

    def test_ranking_con_producto_eliminado(self):
        ventas = {1001: 3, 5555: 3}  # 5555 ya no existe
        self.assertEqual(len(Reporte.top_mas_vendidos(ventas, self.productos)), 2)

    def test_resumen_estadistico(self):
        resumen = Reporte.resumen_estadistico(self.productos)
        self.assertEqual(resumen["precios"], (100, 300, 200))
        self.assertEqual(resumen["sin_stock"], 1)


class TestArchivos(unittest.TestCase):

    def setUp(self):
        self.carpeta = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.carpeta)

    def test_guardar_y_leer_todo(self):
        productos, lista_prov = datos_de_prueba()
        datos = {
            "productos": productos,
            "proveedores": lista_prov,
            "movimientos": [["Ingreso", 1001, 5, (1, 2, 2026)]],
            "ventas": {1001: 2},
            "usuarios": {"admin": {"clave": "1234", "tipo": "admin"}}
        }

        archivos.guardar_datos(datos, self.carpeta)
        leidos = archivos.cargar_datos(self.carpeta)

        self.assertEqual(leidos, datos)

    def test_archivo_inexistente(self):
        self.assertEqual(archivos.leer_productos(self.carpeta), {})
        self.assertEqual(archivos.leer_proveedores_txt(self.carpeta), [])

    def test_linea_danada_en_txt(self):
        with open(os.path.join(self.carpeta, archivos.ARCHIVO_PROVEEDORES), "w", encoding="utf-8") as f:
            f.write("1;Logitech;11-45678901;a@b.com\n")
            f.write("linea rota\n")
            f.write("1;Repetido;11-45678901;c@d.com\n")

        self.assertEqual(len(archivos.leer_proveedores_txt(self.carpeta)), 1)


if __name__ == "__main__":
    unittest.main()
