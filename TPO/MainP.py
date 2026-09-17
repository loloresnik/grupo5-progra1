import menu
import gestion_productos
import proveedores
import Reporte


# ==========================================================
# DATOS PRINCIPALES
# ==========================================================

productos_dic = []
movimientos = []
ventas_dic = {}
proveedores_lista = []

ids_unicos = set()
categorias_unicas = set()
proveedores_unicos = set()


# ==========================================================
# MENU DE PRODUCTOS
# ==========================================================

def menu_productos():

    while True:

        print("\n===== GESTION DE PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        # AGREGAR
        if opcion == "1":

            gestion_productos.agregar_producto_dic(
                productos_dic,
                ids_unicos,
                categorias_unicas,
                proveedores_unicos
            )

        # MOSTRAR
        elif opcion == "2":

            gestion_productos.mostrar_productos_dic(
                productos_dic
            )

        # BUSCAR
        elif opcion == "3":

            id_prod = input("Ingrese ID del producto: ")

            while id_prod.isdigit() is False:
                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto: ")

            id_prod = int(id_prod)

            producto = gestion_productos.buscar_producto_dic(
                productos_dic,
                id_prod
            )

            if producto is None:
                print("Producto no encontrado.")
            else:
                print("\nProducto encontrado:")
                print(producto)

        # MODIFICAR
        elif opcion == "4":

            id_prod = input(
                "Ingrese ID del producto a modificar: "
            )

            while id_prod.isdigit() is False:
                print("El ID debe ser numerico.")
                id_prod = input(
                    "Ingrese ID del producto a modificar: "
                )

            id_prod = int(id_prod)

            producto = gestion_productos.buscar_producto_dic(
                productos_dic,
                id_prod
            )

            if producto is None:

                print("Producto no encontrado.")

            else:

                print("\nDeje vacio un campo si no desea modificarlo.")

                nuevo_nombre = input(
                    "Nuevo nombre: "
                ).strip()

                nueva_categoria = input(
                    "Nueva categoria: "
                ).strip()

                nuevo_proveedor = input(
                    "Nuevo proveedor: "
                ).strip()

                nuevo_precio = input(
                    "Nuevo precio: "
                ).strip()

                if nuevo_nombre == "":
                    nuevo_nombre = None

                if nueva_categoria == "":
                    nueva_categoria = None

                if nuevo_proveedor == "":
                    nuevo_proveedor = None

                if nuevo_precio == "":
                    nuevo_precio = None

                else:

                    while nuevo_precio.isdigit() is False:
                        print("El precio debe ser numerico.")
                        nuevo_precio = input(
                            "Nuevo precio: "
                        ).strip()

                    nuevo_precio = int(nuevo_precio)

                gestion_productos.modificar_producto_dic(
                    productos_dic,
                    id_prod,
                    nuevo_nombre,
                    nueva_categoria,
                    nuevo_proveedor,
                    nuevo_precio,
                    categorias_unicas,
                    proveedores_unicos
                )

        # ELIMINAR
        elif opcion == "5":

            id_prod = input(
                "Ingrese ID del producto a eliminar: "
            )

            while id_prod.isdigit() is False:
                print("El ID debe ser numerico.")
                id_prod = input(
                    "Ingrese ID del producto a eliminar: "
                )

            id_prod = int(id_prod)

            gestion_productos.eliminar_producto_dic(
                productos_dic,
                id_prod,
                ids_unicos
            )

        elif opcion == "0":

            break

        else:

            print("Opcion invalida.")


# ==========================================================
# MENU DE MOVIMIENTOS Y STOCK
# ==========================================================

def menu_movimientos():

    while True:

        print("\n===== STOCK Y MOVIMIENTOS =====")
        print("1. Registrar ingreso")
        print("2. Registrar egreso")
        print("3. Mostrar movimientos")
        print("4. Mostrar ingresos")
        print("5. Mostrar egresos")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        # INGRESO
        if opcion == "1":

            id_prod = input("Ingrese ID del producto: ")

            while id_prod.isdigit() is False:
                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto: ")

            cantidad = input("Ingrese cantidad: ")

            while cantidad.isdigit() is False:
                print("La cantidad debe ser numerica.")
                cantidad = input("Ingrese cantidad: ")

            id_prod = int(id_prod)
            cantidad = int(cantidad)

            resultado = gestion_productos.ingreso_stock_dic(
                productos_dic,
                id_prod,
                cantidad
            )

            if resultado == 1:

                gestion_productos.agregar_movimiento(
                    movimientos,
                    "Ingreso",
                    id_prod,
                    cantidad,
                    productos_dic
                )

        # EGRESO
        elif opcion == "2":

            id_prod = input("Ingrese ID del producto: ")

            while id_prod.isdigit() is False:
                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto: ")

            cantidad = input("Ingrese cantidad: ")

            while cantidad.isdigit() is False:
                print("La cantidad debe ser numerica.")
                cantidad = input("Ingrese cantidad: ")

            id_prod = int(id_prod)
            cantidad = int(cantidad)

            resultado = gestion_productos.egreso_stock_dic(
                productos_dic,
                id_prod,
                cantidad
            )

            if resultado == 1:

                gestion_productos.agregar_movimiento(
                    movimientos,
                    "Egreso",
                    id_prod,
                    cantidad,
                    productos_dic
                )

        # MOSTRAR
        elif opcion == "3":

            gestion_productos.mostrar_movimientos(
                movimientos
            )

        # INGRESOS
        elif opcion == "4":

            gestion_productos.filtrar_movimientos(
                movimientos,
                "Ingreso"
            )

        # EGRESOS
        elif opcion == "5":

            gestion_productos.filtrar_movimientos(
                movimientos,
                "Egreso"
            )

        elif opcion == "0":

            break

        else:

            print("Opcion invalida.")


# ==========================================================
# MENU DE PROVEEDORES
# ==========================================================

def menu_proveedores():

    while True:

        print("\n===== GESTION DE PROVEEDORES =====")
        print("1. Agregar proveedor")
        print("2. Buscar proveedor")
        print("3. Modificar proveedor")
        print("4. Eliminar proveedor")
        print("5. Buscar productos por proveedor")
        print("6. Stock por proveedor")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        # AGREGAR
        if opcion == "1":

            id_proveedor = input(
                "Ingrese ID del proveedor: "
            )

            while id_proveedor.isdigit() is False:
                print("El ID debe ser numerico.")
                id_proveedor = input(
                    "Ingrese ID del proveedor: "
                )

            nombre = input(
                "Ingrese nombre del proveedor: "
            )

            telefono = input(
                "Ingrese telefono: "
            )

            mail = input(
                "Ingrese mail: "
            )

            proveedor = [
                int(id_proveedor),
                nombre,
                telefono,
                mail
            ]

            proveedores.agregar_proveedor(
                proveedores_lista,
                proveedor
            )

            proveedores_unicos.add(nombre)

            print("Proveedor agregado correctamente.")

        # BUSCAR
        elif opcion == "2":

            nombre = input(
                "Ingrese nombre del proveedor: "
            )

            resultado = proveedores.buscar_proveedor(
                proveedores_lista,
                nombre
            )

            if len(resultado) == 0:

                print("Proveedor no encontrado.")

            else:

                print("\nProveedor encontrado:")

                for fila in resultado:

                    print(
                        "ID:",
                        fila[0],
                        "| Nombre:",
                        fila[1],
                        "| Telefono:",
                        fila[2],
                        "| Mail:",
                        fila[3]
                    )

        # MODIFICAR
        elif opcion == "3":

            nombre = input(
                "Ingrese nombre actual: "
            )

            nuevo_nombre = input(
                "Nuevo nombre: "
            )

            nuevo_telefono = input(
                "Nuevo telefono: "
            )

            nuevo_mail = input(
                "Nuevo mail: "
            )

            proveedores.modificar_proveedor(
                proveedores_lista,
                nombre,
                nuevo_nombre,
                nuevo_telefono,
                nuevo_mail,
                productos_dic
            )

            proveedores_unicos.add(nuevo_nombre)

            print("Proveedor modificado correctamente.")

        # ELIMINAR
        elif opcion == "4":

            nombre = input(
                "Ingrese nombre del proveedor: "
            )

            proveedores.eliminar_proveedor(
                proveedores_lista,
                nombre,
                productos_dic
            )

        # PRODUCTOS POR PROVEEDOR
        elif opcion == "5":

            nombre = input(
                "Ingrese proveedor: "
            )

            resultado = proveedores.buscar_productos_por_proveedor(
                productos_dic,
                nombre
            )

            if len(resultado) == 0:

                print("No se encontraron productos.")

            else:

                print("\nProductos encontrados:")

                for producto in resultado:
                    print(producto)

        # STOCK POR PROVEEDOR
        elif opcion == "6":

            nombre = input(
                "Ingrese proveedor: "
            )

            resultado = proveedores.stock_por_proveedor(
                productos_dic,
                nombre
            )

            print(
                "Stock total del proveedor:",
                resultado
            )

        elif opcion == "0":

            break

        else:

            print("Opcion invalida.")


# ==========================================================
# MENU DE CATEGORIAS
# ==========================================================

def menu_categorias():

    while True:

        print("\n===== CATEGORIAS =====")
        print("1. Ver categorias")
        print("2. Buscar productos por categoria")
        print("3. Valor por categoria")
        print("4. Porcentaje del valor por categoria")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        # VER CATEGORIAS
        if opcion == "1":

            if len(categorias_unicas) == 0:

                print("No hay categorias registradas.")

            else:

                print("\n--- CATEGORIAS ---")

                for categoria in categorias_unicas:
                    print("-", categoria)

        # BUSCAR POR CATEGORIA
        elif opcion == "2":

            categoria = input(
                "Ingrese categoria: "
            )

            resultado = Reporte.buscar_por_categoria(
                productos_dic,
                categoria
            )

            if len(resultado) == 0:

                print("No se encontraron productos.")

            else:

                print("\nProductos encontrados:")

                for producto in resultado:
                    print(producto)

        # VALOR POR CATEGORIA
        elif opcion == "3":

            resultado = Reporte.valor_por_categoria(
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay productos.")

            else:

                print("\n--- VALOR POR CATEGORIA ---")

                for categoria in resultado:

                    print(
                        categoria,
                        ": $",
                        resultado[categoria]
                    )

        # PORCENTAJE
        elif opcion == "4":

            resultado = Reporte.porcentaje_valor_por_categoria(
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay datos.")

            else:

                print("\n--- PORCENTAJE POR CATEGORIA ---")

                for categoria in resultado:

                    print(
                        categoria,
                        ":",
                        resultado[categoria],
                        "%"
                    )

        elif opcion == "0":

            break

        else:

            print("Opcion invalida.")


# ==========================================================
# MENU DE REPORTES
# ==========================================================

def menu_reportes():

    while True:

        print("\n===== REPORTES =====")
        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Ventas totales")
        print("4. Top 3 mas vendidos")
        print("5. Top 3 menos vendidos")
        print("6. Recaudacion total")
        print("7. Producto mas caro")
        print("8. Producto menos caro")
        print("9. Valor total del stock")
        print("10. Valor por categoria")
        print("11. Porcentaje del valor por categoria")
        print("12. Buscar por proveedor")
        print("13. Buscar por categoria")
        print("14. Promedio de precio")
        print("15. Precios con IVA")
        print("16. Valor total con reduce")
        print("17. Productos sin stock")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        # REGISTRAR VENTA
        if opcion == "1":

            id_prod = input(
                "Ingrese ID del producto: "
            )

            while id_prod.isdigit() is False:
                print("El ID debe ser numerico.")
                id_prod = input(
                    "Ingrese ID del producto: "
                )

            cantidad = input(
                "Ingrese cantidad: "
            )

            while cantidad.isdigit() is False:
                print("La cantidad debe ser numerica.")
                cantidad = input(
                    "Ingrese cantidad: "
                )

            id_prod = int(id_prod)
            cantidad = int(cantidad)

            Reporte.registrar_venta(
                ventas_dic,
                productos_dic,
                id_prod,
                cantidad
            )

        # MOSTRAR VENTAS
        elif opcion == "2":

            Reporte.mostrar_ventas(
                ventas_dic,
                productos_dic
            )

        # VENTAS TOTALES
        elif opcion == "3":

            total = Reporte.ventas_totales(
                ventas_dic
            )

            print(
                "Ventas totales:",
                total
            )

        # TOP 3
        elif opcion == "4":

            resultado = Reporte.top_mas_vendidos(
                ventas_dic,
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay ventas registradas.")

            else:

                print("\nTop 3 mas vendidos:")

                for nombre in resultado:
                    print("-", nombre)

        # MENOS VENDIDOS
        elif opcion == "5":

            resultado = Reporte.menos_vendidos(
                ventas_dic,
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay ventas registradas.")

            else:

                print("\nTop 3 menos vendidos:")

                for nombre in resultado:
                    print("-", nombre)

        # RECAUDACION
        elif opcion == "6":

            total = Reporte.recaudacion_total(
                ventas_dic,
                productos_dic
            )

            print(
                "Recaudacion total: $",
                total
            )

        # MAS CARO
        elif opcion == "7":

            producto = Reporte.producto_mas_caro(
                productos_dic
            )

            if producto is None:

                print("No hay productos.")

            else:

                print("\nProducto mas caro:")
                print("Nombre:", producto["nombre"])
                print("Precio: $", producto["precio"])

        # MENOS CARO
        elif opcion == "8":

            producto = Reporte.producto_menos_caro(
                productos_dic
            )

            if producto is None:

                print("No hay productos.")

            else:

                print("\nProducto menos caro:")
                print("Nombre:", producto["nombre"])
                print("Precio: $", producto["precio"])

        # VALOR STOCK
        elif opcion == "9":

            total = Reporte.valor_total_stock(
                productos_dic
            )

            print(
                "Valor total del stock: $",
                total
            )

        # VALOR POR CATEGORIA
        elif opcion == "10":

            resultado = Reporte.valor_por_categoria(
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay productos.")

            else:

                for categoria in resultado:

                    print(
                        categoria,
                        ": $",
                        resultado[categoria]
                    )

        # PORCENTAJE
        elif opcion == "11":

            resultado = Reporte.porcentaje_valor_por_categoria(
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay datos.")

            else:

                for categoria in resultado:

                    print(
                        categoria,
                        ":",
                        resultado[categoria],
                        "%"
                    )

        # BUSCAR PROVEEDOR
        elif opcion == "12":

            proveedor = input(
                "Ingrese proveedor: "
            )

            resultado = Reporte.buscar_por_proveedor(
                productos_dic,
                proveedor
            )

            if len(resultado) == 0:

                print("No se encontraron productos.")

            else:

                for producto in resultado:
                    print(producto)

        # BUSCAR CATEGORIA
        elif opcion == "13":

            categoria = input(
                "Ingrese categoria: "
            )

            resultado = Reporte.buscar_por_categoria(
                productos_dic,
                categoria
            )

            if len(resultado) == 0:

                print("No se encontraron productos.")

            else:

                for producto in resultado:
                    print(producto)

        # PROMEDIO
        elif opcion == "14":

            promedio = Reporte.promedio_precio(
                productos_dic
            )

            print(
                "Promedio de precio: $",
                round(promedio, 2)
            )

        # IVA
        elif opcion == "15":

            resultado = Reporte.precios_con_iva(
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay productos.")

            else:

                for precio in resultado:

                    print(
                        "Precio con IVA: $",
                        round(precio, 2)
                    )

        # REDUCE
        elif opcion == "16":

            total = Reporte.valor_total_reduce(
                productos_dic
            )

            print(
                "Valor total del inventario: $",
                total
            )

        # SIN STOCK
        elif opcion == "17":

            resultado = Reporte.productos_sin_stock(
                productos_dic
            )

            if len(resultado) == 0:

                print("No hay productos sin stock.")

            else:

                print("\nProductos sin stock:")

                for producto in resultado:
                    print(producto)

        elif opcion == "0":

            break

        else:

            print("Opcion invalida.")


# ==========================================================
# MENU ADMINISTRADOR
# ==========================================================

def menu_admin():

    while True:

        print("\n==============================")
        print("      MENU ADMINISTRADOR")
        print("==============================")

        print("1. Gestion de productos")
        print("2. Stock y movimientos")
        print("3. Gestion de proveedores")
        print("4. Categorias")
        print("5. Reportes")
        print("0. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            menu_productos()

        elif opcion == "2":

            menu_movimientos()

        elif opcion == "3":

            menu_proveedores()

        elif opcion == "4":

            menu_categorias()

        elif opcion == "5":

            menu_reportes()

        elif opcion == "0":

            print("Sesion cerrada.")
            break

        else:

            print("Opcion invalida.")


# ==========================================================
# MENU USUARIO
# ==========================================================

def menu_usuario():

    while True:

        print("\n==============================")
        print("         MENU USUARIO")
        print("==============================")

        print("1. Productos")
        print("2. Stock y movimientos")
        print("3. Proveedores")
        print("4. Categorias")
        print("5. Reportes")
        print("0. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            menu_productos()

        elif opcion == "2":

            menu_movimientos()

        elif opcion == "3":

            menu_proveedores()

        elif opcion == "4":

            menu_categorias()

        elif opcion == "5":

            menu_reportes()

        elif opcion == "0":

            print("Sesion cerrada.")
            break

        else:

            print("Opcion invalida.")


# ==========================================================
# MAIN
# ==========================================================

def main():

    while True:

        print("\n==============================")
        print("    GESTION DE INVENTARIO")
        print("==============================")

        usuario = menu.iniciar_sesion()

        if usuario == "admin":

            menu_admin()

        elif usuario == "usuario":

            menu_usuario()

        else:

            print("No se pudo iniciar sesion.")


# ==========================================================
# EJECUTAR
# ==========================================================

if __name__ == "__main__":
    main()




