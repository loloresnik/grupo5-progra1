import unittest

import gestion_productos
import proveedores
import Reporte
import empleados
import archivos
import validaciones as val

# "datos" es un diccionario con toda la información del sistema:
# {"productos": {...}, "proveedores": [[...]], "movimientos": [[...]], "ventas": {...}, "usuarios": {...}}

MAX_INTENTOS = 3


def guardar(datos):
    """Después de cada alta, baja o modificación se guarda en los archivos."""
    archivos.guardar_datos(datos)


# ============================
# LOGIN
# ============================

def iniciar_sesion(usuarios):
    """Devuelve la tupla (usuario, rol) o None si se agotan los intentos."""

    for intento in range(1, MAX_INTENTOS + 1):
        usuario = input("Ingrese usuario: ").strip()
        clave = input("Ingrese contraseña: ")

        if usuario in usuarios and usuarios[usuario]["clave"] == clave:
            print(f"\nBienvenido/a, {usuario}.")
            return (usuario, usuarios[usuario]["tipo"])

        print(f"Usuario o contraseña incorrectos. Intentos restantes: {MAX_INTENTOS - intento}")

    print("Se agotaron los intentos.")
    return None


# ============================
# MENÚ PRODUCTOS
# ============================

def mostrar_detalle_producto(datos, id_prod):
    """Muestra un producto y sus movimientos y ventas asociados."""

    producto = gestion_productos.buscar_producto_dic(datos["productos"], id_prod)

    if producto is None:
        print("Producto no encontrado.")
        return

    gestion_productos.mostrar_productos_dic({id_prod: producto}, datos["proveedores"])
    print(f"Unidades vendidas: {datos['ventas'].get(id_prod, 0)}")

    movimientos = gestion_productos.movimientos_de_producto(datos["movimientos"], id_prod)
    gestion_productos.mostrar_movimientos(movimientos, datos["productos"])


def menu_productos(datos):
    productos = datos["productos"]
    lista_prov = datos["proveedores"]

    while True:
        print("\n===== GESTION DE PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto (con sus movimientos)")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                if len(lista_prov) == 0:
                    print("Primero debe cargar al menos un proveedor.")
                    continue

                print("\n=== AGREGAR PRODUCTO ===")
                id_prod = val.pedir_entero("ID del producto: ", minimo=1)

                if id_prod in productos:
                    print("Error: el ID ya existe.")
                    continue

                nombre = val.pedir_texto("Nombre: ", error="Solo letras, números, espacios, puntos o guiones.")
                categoria = val.pedir_texto("Categoría: ", error="Solo letras, números, espacios, puntos o guiones.")
                proveedores.mostrar_proveedores(lista_prov)
                id_proveedor = val.pedir_entero("ID del proveedor: ", minimo=1)
                stock = val.pedir_entero("Stock inicial: ")
                precio = val.pedir_float("Precio: ")

                gestion_productos.alta_producto(productos, lista_prov, id_prod, nombre, categoria,
                                                id_proveedor, stock, precio)
                guardar(datos)
                print("Producto agregado correctamente.")

            elif opcion == "2":
                gestion_productos.mostrar_productos_dic(productos, lista_prov)

            elif opcion == "3":
                id_prod = val.pedir_entero("ID del producto: ", minimo=1)
                mostrar_detalle_producto(datos, id_prod)

            elif opcion == "4":
                id_prod = val.pedir_entero("ID del producto a modificar: ", minimo=1)

                if gestion_productos.buscar_producto_dic(productos, id_prod) is None:
                    print("Producto no encontrado.")
                    continue

                print("\nDeje vacio un campo si no desea modificarlo.")
                nuevo_nombre = val.pedir_texto("Nuevo nombre: ", error="Nombre inválido.", opcional=True)
                nueva_categoria = val.pedir_texto("Nueva categoria: ", error="Categoría inválida.", opcional=True)
                nuevo_proveedor = val.pedir_entero("Nuevo ID de proveedor: ", minimo=1, opcional=True)
                nuevo_precio = val.pedir_float("Nuevo precio: ", opcional=True)

                gestion_productos.modificar_producto_dic(productos, lista_prov, id_prod, nuevo_nombre,
                                                         nueva_categoria, nuevo_proveedor, nuevo_precio)
                guardar(datos)
                print("Producto modificado correctamente.")

            elif opcion == "5":
                id_prod = val.pedir_entero("ID del producto a eliminar: ", minimo=1)
                gestion_productos.eliminar_producto_dic(productos, id_prod)
                guardar(datos)
                print("Producto eliminado.")

            elif opcion == "0":
                break

            else:
                print("Opcion invalida.")

        except ValueError as error:
            print("Error:", error)


# ============================
# MENÚ MOVIMIENTOS
# ============================

def menu_movimientos(datos):
    productos = datos["productos"]
    movimientos = datos["movimientos"]

    while True:
        print("\n===== STOCK Y MOVIMIENTOS =====")
        print("1. Registrar ingreso de stock")
        print("2. Mostrar movimientos")
        print("3. Movimientos de un producto")
        print("4. Cantidad de movimientos por tipo")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                id_prod = val.pedir_entero("ID del producto: ", minimo=1)

                if gestion_productos.buscar_producto_dic(productos, id_prod) is None:
                    print("Producto no encontrado.")
                    continue

                cantidad = val.pedir_entero("Cantidad: ", minimo=1)
                fecha = val.pedir_fecha()

                gestion_productos.ingreso_stock_dic(productos, movimientos, id_prod, cantidad, fecha)
                guardar(datos)
                print("Ingreso registrado. Nuevo stock:", productos[id_prod]["stock"])

            elif opcion == "2":
                gestion_productos.mostrar_movimientos(movimientos, productos)

            elif opcion == "3":
                id_prod = val.pedir_entero("ID del producto: ", minimo=1)
                resultado = gestion_productos.movimientos_de_producto(movimientos, id_prod)
                gestion_productos.mostrar_movimientos(resultado, productos)

            elif opcion == "4":
                for tipo in gestion_productos.TIPOS_MOVIMIENTO:
                    print(f"{tipo}: {gestion_productos.contar_movimientos_recursivo(movimientos, tipo)}")

            elif opcion == "0":
                break

            else:
                print("Opcion invalida.")

        except ValueError as error:
            print("Error:", error)


# ============================
# MENÚ PROVEEDORES
# ============================

def menu_proveedores(datos):
    productos = datos["productos"]
    lista_prov = datos["proveedores"]

    while True:
        print("\n===== GESTION DE PROVEEDORES =====")
        print("1. Agregar proveedor")
        print("2. Mostrar proveedores")
        print("3. Buscar proveedor por nombre")
        print("4. Modificar proveedor")
        print("5. Eliminar proveedor")
        print("6. Productos de un proveedor")
        print("7. Stock por proveedor")
        print("8. Proveedores sin productos")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                id_prov = val.pedir_entero("ID del proveedor: ", minimo=1)

                if proveedores.buscar_proveedor_por_id(lista_prov, id_prov) is not None:
                    print("Error: ya existe un proveedor con ese ID.")
                    continue

                nombre = val.pedir_texto("Nombre: ", error="Nombre inválido.")
                telefono = val.pedir_texto("Teléfono (ej: 11-45678901): ", val.validar_telefono,
                                           "Teléfono inválido.")
                mail = val.pedir_texto("Mail: ", val.validar_mail, "Mail inválido (ej: ventas@empresa.com).")

                proveedores.agregar_proveedor(lista_prov, id_prov, nombre, telefono, mail)
                guardar(datos)
                print("Proveedor agregado correctamente.")

            elif opcion == "2":
                proveedores.mostrar_proveedores(lista_prov)

            elif opcion == "3":
                texto = input("Nombre (o parte del nombre): ")
                resultado = proveedores.buscar_proveedor(lista_prov, texto)
                proveedores.mostrar_proveedores(resultado)

            elif opcion == "4":
                id_prov = val.pedir_entero("ID del proveedor a modificar: ", minimo=1)

                if proveedores.buscar_proveedor_por_id(lista_prov, id_prov) is None:
                    print("Proveedor no encontrado.")
                    continue

                print("\nDeje vacio un campo si no desea modificarlo.")
                nuevo_nombre = val.pedir_texto("Nuevo nombre: ", error="Nombre inválido.", opcional=True)
                nuevo_telefono = val.pedir_texto("Nuevo teléfono: ", val.validar_telefono,
                                                 "Teléfono inválido.", opcional=True)
                nuevo_mail = val.pedir_texto("Nuevo mail: ", val.validar_mail, "Mail inválido.", opcional=True)

                proveedores.modificar_proveedor(lista_prov, id_prov, nuevo_nombre, nuevo_telefono, nuevo_mail)
                guardar(datos)
                print("Proveedor modificado correctamente.")

            elif opcion == "5":
                id_prov = val.pedir_entero("ID del proveedor a eliminar: ", minimo=1)
                proveedores.eliminar_proveedor(lista_prov, id_prov, productos)
                guardar(datos)
                print("Proveedor eliminado.")

            elif opcion == "6":
                texto = input("Nombre del proveedor: ")
                resultado = proveedores.buscar_productos_por_proveedor(productos, lista_prov, texto)
                gestion_productos.mostrar_productos_dic(resultado, lista_prov)

            elif opcion == "7":
                id_prov = val.pedir_entero("ID del proveedor: ", minimo=1)
                print("Stock total del proveedor:", proveedores.stock_por_proveedor(productos, id_prov))

            elif opcion == "8":
                ids = proveedores.proveedores_sin_productos(lista_prov, productos)
                sin_productos = [fila for fila in lista_prov if fila[0] in ids]
                proveedores.mostrar_proveedores(sin_productos)

            elif opcion == "0":
                break

            else:
                print("Opcion invalida.")

        except ValueError as error:
            print("Error:", error)


# ============================
# MENÚ CATEGORÍAS
# ============================

def menu_categorias(datos):
    productos = datos["productos"]

    while True:
        print("\n===== CATEGORIAS =====")
        print("1. Ver categorias")
        print("2. Buscar productos por categoria")
        print("3. Categorias sin ventas")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            categorias = gestion_productos.categorias_unicas(productos)
            if len(categorias) == 0:
                print("No hay categorias registradas.")
            for c in sorted(categorias):
                print("-", c)

        elif opcion == "2":
            categoria = input("Ingrese categoria: ")
            resultado = Reporte.buscar_por_categoria(productos, categoria)
            gestion_productos.mostrar_productos_dic(resultado, datos["proveedores"])

        elif opcion == "3":
            sin_ventas = Reporte.categorias_sin_ventas(datos["ventas"], productos)
            if len(sin_ventas) == 0:
                print("Todas las categorias tuvieron ventas.")
            for c in sorted(sin_ventas):
                print("-", c)

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ VENTAS
# ============================

def menu_ventas(datos):
    productos = datos["productos"]
    ventas = datos["ventas"]

    while True:
        print("\n===== VENTAS =====")
        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Unidades vendidas en total")
        print("4. Top 3 mas vendidos")
        print("5. Top 3 menos vendidos")
        print("6. Recaudacion total")
        print("7. Productos vendidos que se quedaron sin stock")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                id_prod = val.pedir_entero("ID del producto: ", minimo=1)

                if gestion_productos.buscar_producto_dic(productos, id_prod) is None:
                    print("Producto no encontrado.")
                    continue

                cantidad = val.pedir_entero("Cantidad: ", minimo=1)
                fecha = val.pedir_fecha()

                Reporte.registrar_venta(ventas, productos, datos["movimientos"], id_prod, cantidad, fecha)
                guardar(datos)
                print("Venta registrada correctamente.")

            elif opcion == "2":
                Reporte.mostrar_ventas(ventas, productos)

            elif opcion == "3":
                print("Unidades vendidas:", Reporte.ventas_totales(ventas))

            elif opcion == "4":
                print("\nTop 3 más vendidos:")
                for nombre in Reporte.top_mas_vendidos(ventas, productos):
                    print("-", nombre)

            elif opcion == "5":
                print("\nTop 3 menos vendidos:")
                for nombre in Reporte.menos_vendidos(ventas, productos):
                    print("-", nombre)

            elif opcion == "6":
                print(f"Recaudación total: ${Reporte.recaudacion_total(ventas, productos):.2f}")

            elif opcion == "7":
                ids = Reporte.productos_vendidos_sin_stock(ventas, productos)
                if len(ids) == 0:
                    print("No hay productos vendidos sin stock.")
                for id_prod in ids:
                    print(f"- {id_prod}: {productos[id_prod]['nombre']}")

            elif opcion == "0":
                break

            else:
                print("Opcion invalida.")

        except ValueError as error:
            print("Error:", error)


# ============================
# MENÚ ESTADÍSTICAS
# ============================

def mostrar_producto_simple(titulo, producto, clave):
    if producto is None:
        print("No hay productos.")
    else:
        print(f"{titulo}: {producto['nombre']} ({clave}: {producto[clave]})")


def menu_estadisticas(datos):
    productos = datos["productos"]

    while True:
        print("\n===== ESTADISTICAS =====")
        print("1. Resumen estadistico")
        print("2. Promedio de precio general y por categoria")
        print("3. Cantidad de productos total y por categoria")
        print("4. Cantidad de productos por proveedor")
        print("5. Porcentaje de productos por categoria")
        print("6. Valor y porcentaje del valor por categoria")
        print("7. Productos mas caro y mas barato")
        print("8. Productos con mayor y menor stock")
        print("9. Valor total del inventario")
        print("10. Precios con IVA")
        print("11. Productos sin stock")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            Reporte.mostrar_resumen(productos)

        elif opcion == "2":
            print(f"Promedio general: ${Reporte.promedio_precio(productos):.2f}")
            Reporte.mostrar_tabla("PROMEDIO POR CATEGORIA", Reporte.promedio_precio_por_categoria(productos),
                                  "Promedio", "${:.2f}")

        elif opcion == "3":
            print("Total de productos:", Reporte.total_registros(productos))
            Reporte.mostrar_tabla("PRODUCTOS POR CATEGORIA", Reporte.conteo_por_categoria(productos), "Cantidad")

        elif opcion == "4":
            Reporte.mostrar_tabla("PRODUCTOS POR PROVEEDOR",
                                  Reporte.conteo_por_proveedor(productos, datos["proveedores"]), "Cantidad")

        elif opcion == "5":
            Reporte.mostrar_tabla("% DE PRODUCTOS POR CATEGORIA",
                                  Reporte.porcentaje_cantidad_por_categoria(productos), "Porcentaje", "{}%")

        elif opcion == "6":
            Reporte.mostrar_tabla("VALOR POR CATEGORIA", Reporte.valor_por_categoria(productos),
                                  "Valor", "${:.2f}")
            Reporte.mostrar_tabla("% DEL VALOR POR CATEGORIA", Reporte.porcentaje_valor_por_categoria(productos),
                                  "Porcentaje", "{}%")

        elif opcion == "7":
            mostrar_producto_simple("Mas caro", Reporte.producto_mas_caro(productos), "precio")
            mostrar_producto_simple("Mas barato", Reporte.producto_menos_caro(productos), "precio")

        elif opcion == "8":
            mostrar_producto_simple("Mayor stock", Reporte.producto_mayor_stock(productos), "stock")
            mostrar_producto_simple("Menor stock", Reporte.producto_menor_stock(productos), "stock")

        elif opcion == "9":
            print(f"Valor total (for):       ${Reporte.valor_total_stock(productos):.2f}")
            print(f"Valor total (reduce):    ${Reporte.valor_total_reduce(productos):.2f}")
            print(f"Valor total (recursivo): ${Reporte.valor_total_recursivo(list(productos.values())):.2f}")

        elif opcion == "10":
            for nombre, precio in Reporte.precios_con_iva(productos):
                print(f"{nombre[:20]:<20} ${precio:>10.2f}")

        elif opcion == "11":
            gestion_productos.mostrar_productos_dic(Reporte.productos_sin_stock(productos), datos["proveedores"])

        elif opcion == "0":
            break

        else:
            print("Opcion invalida.")


# ============================
# MENÚ EMPLEADOS (solo admin)
# ============================

def menu_empleados(datos):
    usuarios = datos["usuarios"]

    while True:
        print("\n===== EMPLEADOS =====")
        print("1. Alta de empleado")
        print("2. Baja de empleado")
        print("3. Mostrar empleados")
        print("4. Cambiar contraseña")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                nombre = val.pedir_texto("Nombre de usuario: ", error="Nombre inválido.")
                clave = input("Contraseña (mínimo 4 caracteres): ")
                empleados.alta_usuario(usuarios, nombre, clave)
                guardar(datos)
                print("Empleado creado correctamente.")

            elif opcion == "2":
                nombre = input("Usuario a eliminar: ").strip()
                empleados.baja_usuario(usuarios, nombre)
                guardar(datos)
                print("Empleado eliminado.")

            elif opcion == "3":
                empleados.mostrar_usuarios(usuarios)

            elif opcion == "4":
                nombre = input("Usuario: ").strip()
                clave = input("Nueva contraseña: ")
                empleados.cambiar_clave(usuarios, nombre, clave)
                guardar(datos)
                print("Contraseña actualizada.")

            elif opcion == "0":
                break

            else:
                print("Opcion invalida.")

        except ValueError as error:
            print("Error:", error)


# ============================
# ARCHIVOS Y PRUEBAS
# ============================

def leer_archivos(datos):
    """Vuelve a cargar los datos desde los archivos (se reemplaza lo que hay en memoria)."""
    datos.update(archivos.cargar_datos())
    print("Datos leídos desde los archivos.")


def ejecutar_pruebas():
    import test_inventario

    pruebas = unittest.TestLoader().loadTestsFromModule(test_inventario)
    unittest.TextTestRunner(verbosity=2).run(pruebas)


# ============================
# MENÚ PRINCIPAL (admin y usuario)
# ============================

def menu_principal(datos, rol):
    while True:
        print("\n==============================")
        print("      MENU ADMINISTRADOR" if rol == "admin" else "         MENU USUARIO")
        print("==============================")

        print("1. Gestion de productos")
        print("2. Stock y movimientos")
        print("3. Gestion de proveedores")
        print("4. Categorias")
        print("5. Ventas")
        print("6. Estadisticas")
        print("7. Guardar datos en archivos")
        print("8. Leer datos desde archivos")
        print("9. Ejecutar pruebas")
        if rol == "admin":
            print("10. Empleados")
        print("0. Cerrar sesion")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            menu_productos(datos)

        elif opcion == "2":
            menu_movimientos(datos)

        elif opcion == "3":
            menu_proveedores(datos)

        elif opcion == "4":
            menu_categorias(datos)

        elif opcion == "5":
            menu_ventas(datos)

        elif opcion == "6":
            menu_estadisticas(datos)

        elif opcion == "7":
            guardar(datos)
            print("Datos guardados.")

        elif opcion == "8":
            leer_archivos(datos)

        elif opcion == "9":
            ejecutar_pruebas()

        elif opcion == "10" and rol == "admin":
            menu_empleados(datos)

        elif opcion == "0":
            guardar(datos)
            print("Sesion cerrada.")
            break

        else:
            print("Opcion invalida.")
