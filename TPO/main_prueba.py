from gestion_productos import *
from gestion_proveedores import *
from reportes import *

# ============================
#   ESTRUCTURAS PRINCIPALES
# ============================

productos_dic = []
movimientos = []
ventas_dic = {}

proveedores = []  # matriz: [id, nombre, telefono, mail]

ids_unicos = set()
categorias_unicas = set()
proveedores_unicos = set()


while True:
    print("\n=== SISTEMA DE GESTIÓN ===")
    print("1. Gestión de Productos")
    print("2. Gestión de Proveedores")
    print("3. Movimientos")
    print("4. Reportes")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        while True:
            print("\n--- PRODUCTOS ---")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Modificar producto")
            print("4. Eliminar producto")
            print("5. Ingreso de stock")
            print("6. Egreso de stock")
            print("0. Volver")

            op = input("Seleccione una opción: ")

            if op == "1":
                agregar_producto_dic(productos_dic, ids_unicos, categorias_unicas, proveedores_unicos)

            elif op == "2":
                mostrar_productos_dic(productos_dic)

            elif op == "3":
                id_prod = int(input("ID del producto a modificar: "))
                nuevo_nombre = input("Nuevo nombre (ENTER para no cambiar): ").strip() or None
                nueva_categoria = input("Nueva categoría (ENTER para no cambiar): ").strip() or None
                nuevo_proveedor = input("Nuevo proveedor (ENTER para no cambiar): ").strip() or None
                nuevo_precio = input("Nuevo precio (ENTER para no cambiar): ").strip()
                nuevo_precio = int(nuevo_precio) if nuevo_precio.isdigit() else None

                modificar_producto_dic(productos_dic, id_prod, nuevo_nombre, nueva_categoria,
                                       nuevo_proveedor, nuevo_precio, categorias_unicas, proveedores_unicos)

            elif op == "4":
                id_prod = int(input("ID del producto a eliminar: "))
                eliminar_producto_dic(productos_dic, id_prod, ids_unicos)

            elif op == "5":
                id_prod = int(input("ID del producto: "))
                cantidad = int(input("Cantidad a ingresar: "))
                ingreso_stock_dic(productos_dic, id_prod, cantidad)

            elif op == "6":
                id_prod = int(input("ID del producto: "))
                cantidad = int(input("Cantidad a egresar: "))
                egreso_stock_dic(productos_dic, id_prod, cantidad)

            elif op == "0":
                break


    elif opcion == "2":
        while True:
            print("\n--- PROVEEDORES ---")
            print("1. Agregar proveedor")
            print("2. Mostrar proveedores")
            print("3. Buscar proveedor")
            print("4. Modificar proveedor")
            print("5. Eliminar proveedor")
            print("6. Productos por proveedor")
            print("7. Stock por proveedor")
            print("0. Volver")

            op = input("Seleccione una opción: ")

            if op == "1":
                print("\n=== AGREGAR PROVEEDOR ===")
                idp = input("ID proveedor: ").strip()
                nombre = input("Nombre: ").strip()
                telefono = input("Teléfono: ").strip()
                mail = input("Mail: ").strip()
                proveedor = [idp, nombre, telefono, mail]
                agregar_proveedor(proveedores, proveedor)

            elif op == "2":
                print("\n--- LISTA DE PROVEEDORES ---")
                for fila in proveedores:
                    print(fila)

            elif op == "3":
                nombre = input("Nombre del proveedor: ")
                resultado = buscar_proveedor(proveedores, nombre)
                print(resultado)

            elif op == "4":
                nombre = input("Proveedor a modificar: ")
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_mail = input("Nuevo mail: ")
                modificar_proveedor(proveedores, nombre, nuevo_nombre, nuevo_telefono, nuevo_mail, productos_dic)

            elif op == "5":
                nombre = input("Proveedor a eliminar: ")
                eliminar_proveedor(proveedores, nombre, productos_dic)

            elif op == "6":
                nombre = input("Proveedor: ")
                resultado = buscar_productos_por_proveedor(productos_dic, nombre)
                print(resultado)

            elif op == "7":
                nombre = input("Proveedor: ")
                total = stock_por_proveedor(productos_dic, nombre)
                print("Stock total:", total)

            elif op == "0":
                break


    elif opcion == "3":
        while True:
            print("\n--- MOVIMIENTOS ---")
            print("1. Registrar movimiento")
            print("2. Mostrar movimientos")
            print("3. Filtrar movimientos por tipo")
            print("0. Volver")

            op = input("Seleccione una opción: ")

            if op == "1":
                tipo = input("Tipo (ingreso/egreso): ").strip()
                id_prod = int(input("ID producto: "))
                cantidad = int(input("Cantidad: "))
                agregar_movimiento(movimientos, tipo, id_prod, cantidad, productos_dic)

            elif op == "2":
                mostrar_movimientos(movimientos)

            elif op == "3":
                tipo = input("Tipo a filtrar: ")
                filtrar_movimientos(movimientos, tipo)

            elif op == "0":
                break

    elif opcion == "4":
        while True:
            print("\n--- REPORTES ---")
            print("1. Ventas totales")
            print("2. Top 3 más vendidos")
            print("3. Top 3 menos vendidos")
            print("4. Recaudación total")
            print("5. Producto más caro")
            print("6. Producto menos caro")
            print("7. Valor total del stock")
            print("8. Valor por categoría")
            print("9. Porcentaje por categoría")
            print("10. Buscar por proveedor")
            print("11. Buscar por categoría")
            print("12. Promedio de precio")
            print("13. Precios con IVA")
            print("14. Valor total con reduce")
            print("15. Productos sin stock")
            print("0. Volver")

            op = input("Seleccione una opción: ")

            if op == "1":
                print("Ventas totales:", ventas_totales(ventas_dic))

            elif op == "2":
                print("Top 3 más vendidos:", top_mas_vendidos(ventas_dic, productos_dic))

            elif op == "3":
                print("Top 3 menos vendidos:", menos_vendidos(ventas_dic, productos_dic))

            elif op == "4":
                print("Recaudación total:", recaudacion_total(ventas_dic, productos_dic))

            elif op == "5":
                print("Producto más caro:", producto_mas_caro(productos_dic))

            elif op == "6":
                print("Producto menos caro:", producto_menos_caro(productos_dic))

            elif op == "7":
                print("Valor total del stock:", valor_total_stock(productos_dic))

            elif op == "8":
                print("Valor por categoría:", valor_por_categoria(productos_dic))

            elif op == "9":
                print("Porcentaje por categoría:", porcentaje_valor_por_categoria(productos_dic))

            elif op == "10":
                prov = input("Proveedor: ")
                print(buscar_por_proveedor(productos_dic, prov))

            elif op == "11":
                cat = input("Categoría: ")
                print(buscar_por_categoria(productos_dic, cat))

            elif op == "12":
                print("Promedio de precio:", promedio_precio(productos_dic))

            elif op == "13":
                print("Precios con IVA:", precios_con_iva(productos_dic))

            elif op == "14":
                print("Valor total con reduce:", valor_total_reduce(productos_dic))

            elif op == "15":
                print("Productos sin stock:", productos_sin_stock(productos_dic))

            elif op == "0":
                break

    elif opcion == "0":
        print("Saliendo del sistema...")
        break