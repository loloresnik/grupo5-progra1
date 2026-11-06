def iniciar_sesion(usuarios, intentos_max=3):
    """Pide usuario y contraseña hasta intentos_max veces.
    Devuelve el tipo de usuario ("admin" o "usuario"),
    o "" si se agotaron los intentos."""

    intentos = 0

    while intentos < intentos_max:
        usuario = input("Ingrese usuario: ")
        contraseña = input("Ingrese contraseña: ")

        for u in usuarios:
            if u["usuario"] == usuario and u["clave"] == contraseña:
                return u["tipo"]

        intentos += 1
        print(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos_max - intentos}")

    print("Se agotaron los intentos.")
    return ""


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
