import menu
import gestion_productos
import Reporte


def main():

    productos = []

    opcion = 0

    while opcion != 2:

        menu.mostrar_menu_inicio()

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:

            tipo_usuario = menu.iniciar_sesion()

            if tipo_usuario == "admin":

                opcion_admin = 0

                while opcion_admin != 5:

                    menu.mostrar_menu_admin()

                    opcion_admin = int(input("Ingrese una opción: "))

                    if opcion_admin == 1:

                        print("Alta de empleado")

                    elif opcion_admin == 2:

                        print("Baja de empleado")

                    elif opcion_admin == 3:

                        print("Cambiar precio de producto")

                    elif opcion_admin == 4:

                        print("\n===== ESTADÍSTICAS =====")

                        print(
                            "Ventas totales:",
                            Reporte.ventas_totales(productos)
                        )

                        print(
                            "Recaudación total:",
                            Reporte.recaudacion_total(productos)
                        )

                        print(
                            "Stock total:",
                            Reporte.total_stock(productos)
                        )

                    elif opcion_admin == 5:

                        print("Cerrando sesión...")

                    else:

                        print("Opción inválida.")

            elif tipo_usuario == "usuario":

                opcion_usuario = 0

                while opcion_usuario != 6:

                    menu.mostrar_menu_usuario()

                    opcion_usuario = int(
                        input("Ingrese una opción: ")
                    )

                    # =========================
                    # PRODUCTOS
                    # =========================

                    if opcion_usuario == 1:

                        opcion_productos = 0

                        while opcion_productos != 3:

                            print("\n===== PRODUCTOS =====")
                            print("1. Agregar producto")
                            print("2. Mostrar productos")
                            print("3. Volver")

                            opcion_productos = int(
                                input("Ingrese una opción: ")
                            )

                            if opcion_productos == 1:

                                gestion_productos.agregar_producto(
                                    productos
                                )

                            elif opcion_productos == 2:

                                gestion_productos.mostrar_productos(
                                    productos
                                )

                            elif opcion_productos == 3:

                                print(
                                    "Volviendo al menú de usuario..."
                                )

                            else:

                                print("Opción inválida.")

                    # =========================
                    # STOCK
                    # =========================

                    elif opcion_usuario == 2:

                        print("\n===== STOCK =====")
                        print("Stock")

                    # =========================
                    # PROVEEDORES
                    # =========================

                    elif opcion_usuario == 3:

                        print("\n===== PROVEEDORES =====")
                        print("Proveedores")

                    # =========================
                    # CATEGORÍAS
                    # =========================

                    elif opcion_usuario == 4:

                        print("\n===== CATEGORÍAS =====")
                        print("Categorías")

                    # =========================
                    # REPORTES
                    # =========================

                    elif opcion_usuario == 5:

                        opcion_reporte = 0

                        while opcion_reporte != 4:

                            print("\n===== REPORTES =====")
                            print("1. Ventas totales")
                            print("2. Recaudación total")
                            print("3. Stock total")
                            print("4. Volver")

                            opcion_reporte = int(
                                input("Ingrese una opción: ")
                            )

                            if opcion_reporte == 1:

                                total = Reporte.ventas_totales(
                                    productos
                                )

                                print(
                                    "Ventas totales:",
                                    total
                                )

                            elif opcion_reporte == 2:

                                total = Reporte.recaudacion_total(
                                    productos
                                )

                                print(
                                    "Recaudación total:",
                                    total
                                )

                            elif opcion_reporte == 3:

                                total = Reporte.total_stock(
                                    productos
                                )

                                print(
                                    "Stock total:",
                                    total
                                )

                            elif opcion_reporte == 4:

                                print(
                                    "Volviendo al menú de usuario..."
                                )

                            else:

                                print("Opción inválida.")

                    # =========================
                    # CERRAR SESIÓN
                    # =========================

                    elif opcion_usuario == 6:

                        print("Cerrando sesión...")

                    else:

                        print("Opción inválida.")

        elif opcion == 2:

            print("Saliendo del sistema...")

        else:

            print("Opción inválida.")


main()