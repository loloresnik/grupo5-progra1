def mostrar_menu_inicio():
    print("\n===== GESTIÓN DE INVENTARIO =====")
    print("1. Iniciar sesión")
    print("2. Salir")


def mostrar_menu_admin():
    print("\n===== MENÚ ADMIN =====")
    print("1. Alta de empleado")
    print("2. Baja de empleado")
    print("3. Cambiar precio de producto")
    print("4. Ver estadísticas")
    print("5. Cerrar sesión")


def mostrar_menu_usuario():
    print("\n===== MENÚ USUARIO =====")
    print("1. Productos")
    print("2. Stock")
    print("3. Proveedores")
    print("4. Categorías")
    print("5. Reportes")
    print("6. Cerrar sesión")


def iniciar_sesion():
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")

    if usuario == "admin" and contraseña == "1234":
        return "admin"
    elif usuario == "usuario" and contraseña == "1234":
        return "usuario"
    else:
        print("Usuario o contraseña incorrectos.")
        return ""


def menu_admin():
    opcion = 0

    while opcion != 5:
        mostrar_menu_admin()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print("Alta de empleado")
        elif opcion == 2:
            print("Baja de empleado")
        elif opcion == 3:
            print("Cambiar precio de producto")
        elif opcion == 4:
            print("Ver estadísticas")
        elif opcion == 5:
            print("Cerrando sesión...")
        else:
            print("Opción inválida")


def menu_usuario():
    opcion = 0

    while opcion != 6:
        mostrar_menu_usuario()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print("Productos")
        elif opcion == 2:
            print("Stock")
        elif opcion == 3:
            print("Proveedores")
        elif opcion == 4:
            print("Categorías")
        elif opcion == 5:
            print("Reportes")
        elif opcion == 6:
            print("Cerrando sesión...")
        else:
            print("Opción inválida")


def main():
    opcion = 0

    while opcion != 2:
        mostrar_menu_inicio()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            tipo_usuario = iniciar_sesion()

            if tipo_usuario == "admin":
                menu_admin()
            elif tipo_usuario == "usuario":
                menu_usuario()

        elif opcion == 2:
            print("Saliendo del sistema...")
        else:
            print("Opción inválida")


main()