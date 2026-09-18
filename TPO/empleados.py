def alta_usuario(usuarios):
    print("\n===== ALTA DE EMPLEADO =====")
    nombre = input("Ingrese nombre de usuario: ")

    for u in usuarios:
        if u["usuario"] == nombre:
            print("El usuario ya existe.")
            return

    clave = input("Ingrese contraseña: ")

    usuarios.append({
        "usuario": nombre,
        "clave": clave,
        "tipo": "usuario"
    })

    print("Empleado creado correctamente.")


def baja_usuario(usuarios):
    print("\n===== BAJA DE EMPLEADO =====")
    nombre = input("Ingrese usuario a eliminar: ")

    for i, u in enumerate(usuarios):
        if u["usuario"] == nombre:
            if u["tipo"] == "admin":
                print("No se puede eliminar el administrador.")
                return

            usuarios.pop(i)
            print("Empleado eliminado.")
            return

    print("Empleado no encontrado.")
