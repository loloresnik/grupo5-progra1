import gestion_productos
import proveedores
import Reporte
import empleados

# ============================
# MENÚ DE INICIO
# ============================

def menu_inicio():
    """Devuelve "1" para iniciar sesión o "0" para salir del programa."""

    while True:
        print("\n==============================")
        print("    GESTION DE INVENTARIO")
        print("==============================")
        print("1. Iniciar sesion")
        print("0. Salir del programa")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1" or opcion == "0":
            return opcion

        print("Opcion invalida.")


# ============================
# MENÚ PRODUCTOS
# ============================

def menu_productos(productos_dic, ids_unicos, proveedores_lista):
    while True:
        print("\n===== GESTION DE PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            gestion_productos.agregar_producto_dic(productos_dic, ids_unicos, proveedores_lista)

        elif opcion == "2":
            gestion_productos.mostrar_productos_dic(productos_dic, proveedores_lista)

        elif opcion == "3":
            gestion_productos.consultar_producto(productos_dic, proveedores_lista)

        elif opcion == "4":
            gestion_productos.modificar_producto(productos_dic, proveedores_lista)

        elif opcion == "5":
            gestion_productos.eliminar_producto(productos_dic, ids_unicos)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ MOVIMIENTOS
# ============================

def menu_movimientos(productos_dic, movimientos):
    while True:
        print("\n===== STOCK Y MOVIMIENTOS =====")
        print("1. Registrar ingreso")
        print("2. Mostrar movimientos")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            gestion_productos.registrar_ingreso(productos_dic, movimientos)

        elif opcion == "2":
            gestion_productos.mostrar_movimientos(movimientos)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ PROVEEDORES
# ============================

def menu_proveedores(productos_dic, proveedores_lista):
    while True:
        print("\n===== GESTION DE PROVEEDORES =====")
        print("1. Agregar proveedor")
        print("2. Mostrar proveedores")
        print("3. Buscar proveedor")
        print("4. Modificar proveedor")
        print("5. Eliminar proveedor")
        print("6. Productos de un proveedor")
        print("7. Stock por proveedor")
        print("8. Proveedores sin productos")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            proveedores.alta_proveedor(proveedores_lista)

        elif opcion == "2":
            proveedores.mostrar_proveedores(proveedores_lista)

        elif opcion == "3":
            proveedores.consultar_proveedor(proveedores_lista)

        elif opcion == "4":
            proveedores.editar_proveedor(proveedores_lista)

        elif opcion == "5":
            proveedores.baja_proveedor(proveedores_lista, productos_dic)

        elif opcion == "6":
            proveedores.mostrar_productos_de_proveedor(productos_dic, proveedores_lista)

        elif opcion == "7":
            proveedores.mostrar_stock_por_proveedor(productos_dic, proveedores_lista)

        elif opcion == "8":
            proveedores.mostrar_proveedores_sin_productos(proveedores_lista, productos_dic)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ CATEGORÍAS
# ============================

def menu_categorias(productos_dic, ventas_dic, proveedores_lista):
    while True:
        print("\n===== CATEGORIAS =====")
        print("1. Ver categorias")
        print("2. Buscar productos por categoria")
        print("3. Cantidad de productos por categoria")
        print("4. Precio promedio por categoria")
        print("5. Valor por categoria")
        print("6. Porcentaje del valor por categoria")
        print("7. Categorias sin ventas")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            Reporte.mostrar_categorias(productos_dic)

        elif opcion == "2":
            Reporte.mostrar_productos_por_categoria(productos_dic, proveedores_lista)

        elif opcion == "3":
            Reporte.mostrar_cantidad_por_categoria(productos_dic)

        elif opcion == "4":
            Reporte.mostrar_promedio_por_categoria(productos_dic)

        elif opcion == "5":
            Reporte.mostrar_valor_por_categoria(productos_dic)

        elif opcion == "6":
            Reporte.mostrar_porcentaje_valor_por_categoria(productos_dic)

        elif opcion == "7":
            Reporte.mostrar_categorias_sin_ventas(ventas_dic, productos_dic)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ VENTAS Y REPORTES
# ============================

def menu_reportes(productos_dic, ventas_dic, movimientos, proveedores_lista):
    while True:
        print("\n===== VENTAS Y REPORTES =====")
        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Unidades vendidas")
        print("4. Top 3 mas vendidos")
        print("5. Top 3 menos vendidos")
        print("6. Recaudacion total")
        print("7. Producto mas caro")
        print("8. Producto mas barato")
        print("9. Producto con mayor stock")
        print("10. Producto con menor stock")
        print("11. Valor total del stock")
        print("12. Precios con IVA")
        print("13. Productos sin stock")
        print("14. Vendidos que quedaron sin stock")
        print("15. Cantidad de productos por proveedor")
        print("16. Resumen estadistico")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            Reporte.venta(ventas_dic, productos_dic, movimientos)

        elif opcion == "2":
            Reporte.mostrar_ventas(ventas_dic, productos_dic)

        elif opcion == "3":
            Reporte.mostrar_ventas_totales(ventas_dic)

        elif opcion == "4":
            Reporte.mostrar_mas_vendidos(ventas_dic, productos_dic)

        elif opcion == "5":
            Reporte.mostrar_menos_vendidos(ventas_dic, productos_dic)

        elif opcion == "6":
            Reporte.mostrar_recaudacion(ventas_dic)

        elif opcion == "7":
            Reporte.mostrar_mas_caro(productos_dic)

        elif opcion == "8":
            Reporte.mostrar_mas_barato(productos_dic)

        elif opcion == "9":
            Reporte.mostrar_mayor_stock(productos_dic)

        elif opcion == "10":
            Reporte.mostrar_menor_stock(productos_dic)

        elif opcion == "11":
            Reporte.mostrar_valor_total(productos_dic)

        elif opcion == "12":
            Reporte.mostrar_precios_con_iva(productos_dic)

        elif opcion == "13":
            Reporte.mostrar_productos_sin_stock(productos_dic, proveedores_lista)

        elif opcion == "14":
            Reporte.mostrar_vendidos_sin_stock(ventas_dic, productos_dic)

        elif opcion == "15":
            Reporte.mostrar_conteo_por_proveedor(productos_dic, proveedores_lista)

        elif opcion == "16":
            Reporte.mostrar_resumen(productos_dic)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ ADMIN
# ============================

def menu_admin(usuarios, productos_dic, movimientos, ventas_dic, proveedores_lista, ids_unicos):

    while True:
        print("\n==============================")
        print("      MENU ADMINISTRADOR")
        print("==============================")

        print("1. Gestion de productos")
        print("2. Stock y movimientos")
        print("3. Gestion de proveedores")
        print("4. Categorias")
        print("5. Ventas y reportes")
        print("6. Alta de empleado")
        print("7. Baja de empleado")
        print("0. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_productos(productos_dic, ids_unicos, proveedores_lista)

        elif opcion == "2":
            menu_movimientos(productos_dic, movimientos)

        elif opcion == "3":
            menu_proveedores(productos_dic, proveedores_lista)

        elif opcion == "4":
            menu_categorias(productos_dic, ventas_dic, proveedores_lista)

        elif opcion == "5":
            menu_reportes(productos_dic, ventas_dic, movimientos, proveedores_lista)

        elif opcion == "6":
            empleados.alta_usuario(usuarios)

        elif opcion == "7":
            empleados.baja_usuario(usuarios)

        elif opcion == "0":
            print("Sesion cerrada.")
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ USUARIO
# ============================

def menu_usuario(productos_dic, movimientos, ventas_dic, proveedores_lista, ids_unicos):

    while True:
        print("\n==============================")
        print("         MENU USUARIO")
        print("==============================")

        print("1. Productos")
        print("2. Stock y movimientos")
        print("3. Proveedores")
        print("4. Categorias")
        print("5. Ventas y reportes")
        print("0. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_productos(productos_dic, ids_unicos, proveedores_lista)

        elif opcion == "2":
            menu_movimientos(productos_dic, movimientos)

        elif opcion == "3":
            menu_proveedores(productos_dic, proveedores_lista)

        elif opcion == "4":
            menu_categorias(productos_dic, ventas_dic, proveedores_lista)

        elif opcion == "5":
            menu_reportes(productos_dic, ventas_dic, movimientos, proveedores_lista)

        elif opcion == "0":
            print("Sesion cerrada.")
            break

        else:
            print("Opcion invalida.")
