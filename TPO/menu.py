import gestion_productos
import proveedores
import Reporte
import empleados

# ============================
# LOGIN
# ============================

def iniciar_sesion(usuarios):
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")

    for u in usuarios:
        if u["usuario"] == usuario and u["clave"] == contraseña:
            return u["tipo"]

    print("Usuario o contraseña incorrectos.")
    return ""


# ============================
# MENÚ PRODUCTOS
# ============================

def menu_productos(productos_dic, ids_unicos, categorias_unicas, proveedores_unicos):
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
            gestion_productos.agregar_producto_dic(
                productos_dic, ids_unicos, categorias_unicas, proveedores_unicos
            )

        elif opcion == "2":
            gestion_productos.mostrar_productos_dic(productos_dic)

        elif opcion == "3":
            id_prod = input("Ingrese ID del producto: ")
            while not id_prod.isdigit():
                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto: ")

            producto = gestion_productos.buscar_producto_dic(productos_dic, int(id_prod))
            print("Producto encontrado:" if producto else "Producto no encontrado.")
            if producto:
                print(producto)

        elif opcion == "4":
            id_prod = input("Ingrese ID del producto a modificar: ")
            while not id_prod.isdigit():
                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto a modificar: ")

            id_prod = int(id_prod)
            producto = gestion_productos.buscar_producto_dic(productos_dic, id_prod)

            if producto is None:
                print("Producto no encontrado.")
            else:
                print("\nDeje vacio un campo si no desea modificarlo.")
                nuevo_nombre = input("Nuevo nombre: ").strip() or None
                nueva_categoria = input("Nueva categoria: ").strip() or None
                nuevo_proveedor = input("Nuevo proveedor: ").strip() or None

                nuevo_precio = input("Nuevo precio: ").strip()
                if nuevo_precio == "":
                    nuevo_precio = None
                else:
                    while not nuevo_precio.isdigit():
                        print("El precio debe ser numerico.")
                        nuevo_precio = input("Nuevo precio: ").strip()
                    nuevo_precio = int(nuevo_precio)

                gestion_productos.modificar_producto_dic(
                    productos_dic, id_prod, nuevo_nombre, nueva_categoria,
                    nuevo_proveedor, nuevo_precio, categorias_unicas, proveedores_unicos
                )

        elif opcion == "5":
            id_prod = input("Ingrese ID del producto a eliminar: ")
            while not id_prod.isdigit():
                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto a eliminar: ")

            gestion_productos.eliminar_producto_dic(productos_dic, int(id_prod), ids_unicos)

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

            id_prod = input("Ingrese ID del producto: ")

            while not id_prod.isdigit():

                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto: ")

            cantidad = input("Ingrese cantidad: ")

            while not cantidad.isdigit():

                print("La cantidad debe ser numerica.")
                cantidad = input("Ingrese cantidad: ")

            id_prod = int(id_prod)
            cantidad = int(cantidad)

            ok = gestion_productos.ingreso_stock_dic(productos_dic, id_prod, cantidad)
            if ok:
                gestion_productos.agregar_movimiento(movimientos, "Ingreso", id_prod, cantidad, productos_dic)

        elif opcion == "2":
            gestion_productos.mostrar_movimientos(movimientos)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ PROVEEDORES
# ============================

def menu_proveedores(productos_dic, proveedores_lista, proveedores_unicos):
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

        if opcion == "1":
            id_prov = input("Ingrese ID del proveedor: ")
            while not id_prov.isdigit():
                print("El ID debe ser numerico.")
                id_prov = input("Ingrese ID del proveedor: ")

            nombre = input("Ingrese nombre del proveedor: ")
            telefono = input("Ingrese telefono: ")
            mail = input("Ingrese mail: ")

            proveedor = [int(id_prov), nombre, telefono, mail]
            proveedores.agregar_proveedor(proveedores_lista, proveedor)
            proveedores_unicos.add(nombre)

            print("Proveedor agregado correctamente.")

        elif opcion == "2":
            nombre = input("Ingrese nombre del proveedor: ")
            resultado = proveedores.buscar_proveedor(proveedores_lista, nombre)

            if len(resultado) == 0:
                print("Proveedor no encontrado.")
            else:
                print("\nProveedor encontrado:")
                for fila in resultado:
                    print(f"ID: {fila[0]} | Nombre: {fila[1]} | Tel: {fila[2]} | Mail: {fila[3]}")

        elif opcion == "3":
            nombre = input("Ingrese nombre actual: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo telefono: ")
            nuevo_mail = input("Nuevo mail: ")

            proveedores.modificar_proveedor(
                proveedores_lista, nombre, nuevo_nombre, nuevo_telefono, nuevo_mail, productos_dic
            )

            proveedores_unicos.add(nuevo_nombre)
            print("Proveedor modificado correctamente.")

        elif opcion == "4":
            nombre = input("Ingrese nombre del proveedor: ")
            proveedores.eliminar_proveedor(proveedores_lista, nombre, productos_dic)

        elif opcion == "5":
            nombre = input("Ingrese proveedor: ")
            resultado = proveedores.buscar_productos_por_proveedor(productos_dic, nombre)

            if len(resultado) == 0:
                print("No se encontraron productos.")
            else:
                print("\nProductos encontrados:")
                for p in resultado:
                    print(p)

        elif opcion == "6":
            nombre = input("Ingrese proveedor: ")
            total = proveedores.stock_por_proveedor(productos_dic, nombre)
            print("Stock total del proveedor:", total)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ CATEGORÍAS
# ============================

def menu_categorias(productos_dic, categorias_unicas):
    while True:
        print("\n===== CATEGORIAS =====")
        print("1. Ver categorias")
        print("2. Buscar productos por categoria")
        print("3. Valor por categoria")
        print("4. Porcentaje del valor por categoria")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            if len(categorias_unicas) == 0:
                print("No hay categorias registradas.")
            else:
                print("\n--- CATEGORIAS ---")
                for c in categorias_unicas:
                    print("-", c)

        elif opcion == "2":
            categoria = input("Ingrese categoria: ")
            resultado = Reporte.buscar_por_categoria(productos_dic, categoria)

            if len(resultado) == 0:
                print("No se encontraron productos.")
            else:
                print("\nProductos encontrados:")
                for p in resultado:
                    print(p)

        elif opcion == "3":
            valores = Reporte.valor_por_categoria(productos_dic)
            if len(valores) == 0:
                print("No hay productos.")
            else:
                print("\n--- VALOR POR CATEGORIA ---")
                for cat, val in valores.items():
                    print(f"{cat}: ${val}")

        elif opcion == "4":
            porcentajes = Reporte.porcentaje_valor_por_categoria(productos_dic)
            if len(porcentajes) == 0:
                print("No hay datos.")
            else:
                print("\n--- PORCENTAJE POR CATEGORIA ---")
                for cat, porc in porcentajes.items():
                    print(f"{cat}: {porc}%")

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ REPORTES
# ============================

def menu_reportes(productos_dic, ventas_dic):
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
        print("11. Porcentaje por categoria")
        print("12. Buscar por proveedor")
        print("13. Buscar por categoria")
        print("14. Promedio de precio")
        print("15. Precios con IVA")
        print("16. Valor total")
        print("17. Productos sin stock")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            id_prod = input("Ingrese ID del producto: ")
            while not id_prod.isdigit():
                print("El ID debe ser numerico.")
                id_prod = input("Ingrese ID del producto: ")

            cantidad = input("Ingrese cantidad: ")
            while not cantidad.isdigit():
                print("La cantidad debe ser numerica.")
                cantidad = input("Ingrese cantidad: ")

            Reporte.registrar_venta(ventas_dic, productos_dic, int(id_prod), int(cantidad))

        elif opcion == "2":
            Reporte.mostrar_ventas(ventas_dic, productos_dic)

        elif opcion == "3":
            print("Ventas totales:", Reporte.ventas_totales(ventas_dic))

        elif opcion == "4":
            resultado = Reporte.top_mas_vendidos(ventas_dic, productos_dic)
            print("\nTop 3 más vendidos:")
            for r in resultado:
                print("-", r)

        elif opcion == "5":
            resultado = Reporte.menos_vendidos(ventas_dic, productos_dic)
            print("\nTop 3 menos vendidos:")
            for r in resultado:
                print("-", r)

        elif opcion == "6":
            print("Recaudación total: $", Reporte.recaudacion_total(ventas_dic, productos_dic))

        elif opcion == "7":
            p = Reporte.producto_mas_caro(productos_dic)
            print("Producto más caro:", p["nombre"], "- $", p["precio"]) if p else print("No hay productos.")

        elif opcion == "8":
            p = Reporte.producto_menos_caro(productos_dic)
            print("Producto menos caro:", p["nombre"], "- $", p["precio"]) if p else print("No hay productos.")

        elif opcion == "9":
            print("Valor total del stock: $", Reporte.valor_total_stock(productos_dic))

        elif opcion == "10":
            valores = Reporte.valor_por_categoria(productos_dic)
            for cat, val in valores.items():
                print(f"{cat}: ${val}")

        elif opcion == "11":
            porcentajes = Reporte.porcentaje_valor_por_categoria(productos_dic)
            for cat, porc in porcentajes.items():
                print(f"{cat}: {porc}%")

        elif opcion == "12":
            prov = input("Ingrese proveedor: ")
            resultado = Reporte.buscar_por_proveedor(productos_dic, prov)
            for p in resultado:
                print(p)

        elif opcion == "13":
            cat = input("Ingrese categoria: ")
            resultado = Reporte.buscar_por_categoria(productos_dic, cat)
            for p in resultado:
                print(p)

        elif opcion == "14":
            print("Promedio de precio: $", round(Reporte.promedio_precio(productos_dic), 2))

        elif opcion == "15":
            precios = Reporte.precios_con_iva(productos_dic)
            for p in precios:
                print("Precio con IVA: $", round(p, 2))

        elif opcion == "16":
            print("Valor total del inventario: $", Reporte.valor_total_reduce(productos_dic))

        elif opcion == "17":
            resultado = Reporte.productos_sin_stock(productos_dic)
            print("\nProductos sin stock:")
            for p in resultado:
                print(p)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ ADMIN
# ============================

def menu_admin(usuarios, productos_dic, movimientos, ventas_dic,
               proveedores_lista, ids_unicos, categorias_unicas, proveedores_unicos):

    while True:
        print("\n==============================")
        print("      MENU ADMINISTRADOR")
        print("==============================")

        print("1. Gestion de productos")
        print("2. Stock y movimientos")
        print("3. Gestion de proveedores")
        print("4. Categorias")
        print("5. Reportes")
        print("6. Alta de empleado")
        print("7. Baja de empleado")
        print("0. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_productos(productos_dic, ids_unicos, categorias_unicas, proveedores_unicos)

        elif opcion == "2":
            menu_movimientos(productos_dic, movimientos)

        elif opcion == "3":
            menu_proveedores(productos_dic, proveedores_lista, proveedores_unicos)

        elif opcion == "4":
            menu_categorias(productos_dic, categorias_unicas)

        elif opcion == "5":
            menu_reportes(productos_dic, ventas_dic)

        elif opcion == "6":
            empleados.alta_usuario(usuarios)

        elif opcion == "7":
            empleados.baja_usuario(usuarios)

        elif opcion == "0":
            print("Sesion cerrada.")
            break

        else:
            print("Opcion invalida.")



def menu_usuario(productos_dic, movimientos, ventas_dic,
                 proveedores_lista, ids_unicos, categorias_unicas, proveedores_unicos):

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
            menu_productos(productos_dic, ids_unicos, categorias_unicas, proveedores_unicos)

        elif opcion == "2":
            menu_movimientos(productos_dic, movimientos)

        elif opcion == "3":
            menu_proveedores(productos_dic, proveedores_lista, proveedores_unicos)

        elif opcion == "4":
            menu_categorias(productos_dic, categorias_unicas)

        elif opcion == "5":
            menu_reportes(productos_dic, ventas_dic)

        elif opcion == "0":
            print("Sesion cerrada.")
            break

        else:
            print("Opcion invalida.")