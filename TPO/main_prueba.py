from gestion_productos import (
    agregar_producto_dic,
    mostrar_productos_dic,
    modificar_producto_dic,
    eliminar_producto_dic,
    ingreso_stock_dic,
    egreso_stock_dic,
    agregar_movimiento,
    mostrar_movimientos,
    filtrar_movimientos
)

def main():

    # Lista de productos 
    productos_dic = []

    # Movimientos 
    movimientos = []

    #para evitar duplicados
    ids_unicos = set()
    categorias_unicas = set()
    proveedores_unicos = set()

    opcion = ""

    while opcion != "0":

        print("\n=== MENU PRINCIPAL ===")
        print("1 - Gestionar productos ")
        print("2 - Gestionar movimientos")
        print("3 - Ver conjuntos")
        print("0 - Salir")

        opcion = input("Ingrese una opcion: ").strip()

        if opcion == "1":

            print("\n--- GESTION DE PRODUCTOS ---")
            print("1 - Agregar producto")
            print("2 - Mostrar productos")
            print("3 - Modificar producto")
            print("4 - Eliminar producto")
            print("5 - Ingreso de stock")
            print("6 - Egreso de stock")
            print("0 - Volver")

            sub = input("Ingrese opcion: ").strip()

            if sub == "1":

                agregar_producto_dic(productos_dic, ids_unicos, categorias_unicas, proveedores_unicos)

            elif sub == "2":

                mostrar_productos_dic(productos_dic)

            elif sub == "3":

                id_prod = input("ID del producto: ").strip()

                if id_prod.isdigit():
                    id_prod = int(id_prod)

                    nuevo_nombre = input("Nuevo nombre (ENTER para no cambiar): ").strip()
                    nueva_categoria = input("Nueva categoria (ENTER para no cambiar): ").strip()
                    nuevo_proveedor = input("Nuevo proveedor (ENTER para no cambiar): ").strip()

                    if nuevo_nombre == "":
                        nuevo_nombre = None
                    if nueva_categoria == "":
                        nueva_categoria = None
                    if nuevo_proveedor == "":
                        nuevo_proveedor = None

                    modificar_producto_dic(
                        productos_dic,
                        id_prod,
                        nuevo_nombre,
                        nueva_categoria,
                        nuevo_proveedor,
                        categorias_unicas,
                        proveedores_unicos
                    )
                else:

                    print("ID invalido.")

            elif sub == "4":

                id_prod = input("ID del producto: ").strip()

                if id_prod.isdigit():

                    eliminar_producto_dic(productos_dic, int(id_prod), ids_unicos)
                    
                else:

                    print("ID invalido.")

            elif sub == "5":

                id_prod = input("ID del producto: ").strip()

                cantidad = input("Cantidad a ingresar: ").strip()

                if id_prod.isdigit() and cantidad.isdigit():

                    ingreso_stock_dic(productos_dic, int(id_prod), int(cantidad))

                else:

                    print("Datos invalidos.")

            elif sub == "6":

                id_prod = input("ID del producto: ").strip()

                cantidad = input("Cantidad a retirar: ").strip()

                if id_prod.isdigit() and cantidad.isdigit():

                    egreso_stock_dic(productos_dic, int(id_prod), int(cantidad))

                else:

                    print("Datos invalidos.")

        elif opcion == "2":

            print("\n--- GESTION DE MOVIMIENTOS ---")
            print("1 - Registrar ingreso")
            print("2 - Registrar egreso")
            print("3 - Mostrar movimientos")
            print("4 - Filtrar ingresos")
            print("5 - Filtrar egresos")
            print("0 - Volver")

            sub = input("Ingrese opcion: ").strip()

            if sub == "1":

                id_prod = input("ID del producto: ").strip()

                cantidad = input("Cantidad: ").strip()

                if id_prod.isdigit() and cantidad.isdigit():

                    agregar_movimiento(movimientos, "ingreso", int(id_prod), int(cantidad), productos_dic)
                else:

                    print("Datos invalidos.")

            elif sub == "2":

                id_prod = input("ID del producto: ").strip()

                cantidad = input("Cantidad: ").strip()

                if id_prod.isdigit() and cantidad.isdigit():

                    agregar_movimiento(movimientos, "egreso", int(id_prod), int(cantidad), productos_dic)

                else:

                    print("Datos invalidos.")

            elif sub == "3":

                mostrar_movimientos(movimientos)

            elif sub == "4":

                filtrar_movimientos(movimientos, "ingreso")

            elif sub == "5":

                filtrar_movimientos(movimientos, "egreso")

        elif opcion == "3":

            print("\n--- PANELES DE CONJUNTOS ---")
            print("IDs únicos:", ids_unicos)
            print("Categorías únicas:", categorias_unicas)
            print("Proveedores únicos:", proveedores_unicos)

        elif opcion == "0":

            print("Saliendo del programa...")

        else:

            print("Opcion invalida.")

main()