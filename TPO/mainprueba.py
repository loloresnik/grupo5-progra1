from gestion_productos import (
    agregar_producto,
    buscar_producto,
    modificar_producto,
    eliminar_producto,
    mostrar_productos,
    ingreso_stock,
    egreso_stock,
    consultar_stock,
    ordenar_por_nombre,
    ordenar_por_stock,
    filtrar_stock_bajo,
    mostrar_nombres,
    stock_total,
)

def main():

    productos = []

    opcion = ""

    while opcion != "0":

        print("\n=== MENU PRINCIPAL ===")
        print("1 - Agregar producto")
        print("2 - Buscar producto")
        print("3 - Modificar producto")
        print("4 - Eliminar producto")
        print("5 - Mostrar productos")
        print("6 - Ingreso de stock")
        print("7 - Egreso de stock")
        print("8 - Consultar stock")
        print("9 - Ordenar por nombre")
        print("10 - Ordenar por stock")
        print("11 - Filtrar stock bajo")
        print("12 - Mostrar nombres")
        print("13 - Stock total")
        print("0 - Salir")

        opcion = input("Ingrese una opcion: ")

        print()

        if opcion == "1":

            agregar_producto(productos)

        elif opcion == "2":

            id_prod = input("Ingrese ID a buscar: ")

            if id_prod.isdigit():

                id_prod = int(id_prod)

                prod = buscar_producto(productos, id_prod)

                if prod is None:
                    print("Producto no encontrado.")
                else:
                    print("Producto encontrado:", prod)

            else:
                print("ID invalido.")

        elif opcion == "3":

            id_prod = input("Ingrese ID a modificar: ")

            if id_prod.isdigit():

                id_prod = int(id_prod)

                nuevo_nombre = input("Nuevo nombre (ENTER para no cambiar): ")
                nueva_categoria = input("Nueva categoria (ENTER para no cambiar): ")
                nuevo_proveedor = input("Nuevo proveedor (ENTER para no cambiar): ")

                if nuevo_nombre == "":
                    nuevo_nombre = None

                if nueva_categoria == "":
                    nueva_categoria = None

                if nuevo_proveedor == "":
                    nuevo_proveedor = None

                modificar_producto(productos, id_prod, nuevo_nombre, nueva_categoria, nuevo_proveedor)

            else:
                print("ID invalido.")

        elif opcion == "4":

            id_prod = input("Ingrese ID a eliminar: ")

            if id_prod.isdigit():

                id_prod = int(id_prod)

                eliminar_producto(productos, id_prod)

            else:
                print("ID invalido.")

        elif opcion == "5":

            mostrar_productos(productos)

        elif opcion == "6":

            id_prod = input("ID del producto: ")
            cantidad = input("Cantidad a ingresar: ")

            if id_prod.isdigit() and cantidad.isdigit():

                ingreso_stock(productos, int(id_prod), int(cantidad))

            else:
                print("Datos invalidos.")



        elif opcion == "7":

            id_prod = input("ID del producto: ")
            cantidad = input("Cantidad a retirar: ")

            if id_prod.isdigit() and cantidad.isdigit():

                egreso_stock(productos, int(id_prod), int(cantidad))

            else:
                print("Datos invalidos.")



        elif opcion == "8":

            id_prod = input("ID del producto: ")

            if id_prod.isdigit():

                consultar_stock(productos, int(id_prod))

            else:
                print("ID invalido.")



        elif opcion == "9":

            ordenar_por_nombre(productos)



        elif opcion == "10":

            ordenar_por_stock(productos)



        elif opcion == "11":

            limite = input("Ingrese limite de stock: ")

            if limite.isdigit():

                filtrar_stock_bajo(productos, int(limite))

            else:
                print("Limite invalido.")



        elif opcion == "12":

            mostrar_nombres(productos)



        elif opcion == "13":

            stock_total(productos)

        elif opcion == "0":

            print("Saliendo del programa...")

        else:

            print("Opcion invalida.")

main()