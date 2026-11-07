import json

ARCHIVO_USUARIOS = "usuarios.json"

# Usuarios iniciales: se usan solo si todavía no existe usuarios.json
USUARIOS_INICIALES = [
    {"usuario": "admin", "clave": "1234", "tipo": "admin"},
    {"usuario": "usuario", "clave": "1234", "tipo": "usuario"}
]

# Guardar usuarios
def guardar_usuarios_json(usuarios):
    """Guarda la lista de diccionarios de usuarios en usuarios.json."""

    try:

        archivo = open(ARCHIVO_USUARIOS, "w", encoding="utf-8")

        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

        archivo.close()

        return 1

    except (OSError, TypeError) as error:

        print("Error al guardar usuarios:", error)

        return 0

# Cargar usuarios
def cargar_usuarios_json():
    """Carga usuarios.json. Si todavía no existe, lo crea con los usuarios iniciales."""

    try:

        archivo = open(ARCHIVO_USUARIOS, "r", encoding="utf-8")

        usuarios = json.load(archivo)

        archivo.close()

        return usuarios

    except FileNotFoundError:

        usuarios = USUARIOS_INICIALES.copy()

        guardar_usuarios_json(usuarios)

        return usuarios

    except (OSError, json.JSONDecodeError) as error:

        print("Error al cargar usuarios:", error)

        print("Se usan los usuarios iniciales.")

        return USUARIOS_INICIALES.copy()


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

    guardar_usuarios_json(usuarios)

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
            guardar_usuarios_json(usuarios)
            print("Empleado eliminado.")
            return

    print("Empleado no encontrado.")