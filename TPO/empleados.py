import proveedores

# Los usuarios se guardan en un diccionario: {usuario: {"clave": ..., "tipo": ...}}


def alta_usuario(usuarios, nombre, clave, tipo="usuario"):
    """Crea un empleado. Lanza ValueError si el usuario ya existe o algún dato es inválido."""

    nombre = nombre.strip()

    if nombre in usuarios:
        raise ValueError("El usuario ya existe.")

    if not proveedores.validar_nombre(nombre):
        raise ValueError("El nombre de usuario es inválido.")

    if len(clave) < 4:
        raise ValueError("La contraseña debe tener al menos 4 caracteres.")

    # Tupla con los roles válidos
    if tipo not in ("admin", "usuario"):
        raise ValueError("Rol inválido.")

    usuarios[nombre] = {"clave": clave, "tipo": tipo}


def baja_usuario(usuarios, nombre):
    if nombre not in usuarios:
        raise ValueError("Empleado no encontrado.")

    if usuarios[nombre]["tipo"] == "admin":
        raise ValueError("No se puede eliminar al administrador.")

    del usuarios[nombre]


def cambiar_clave(usuarios, nombre, nueva_clave):
    if nombre not in usuarios:
        raise ValueError("Empleado no encontrado.")

    if len(nueva_clave) < 4:
        raise ValueError("La contraseña debe tener al menos 4 caracteres.")

    usuarios[nombre]["clave"] = nueva_clave


def mostrar_usuarios(usuarios):
    print("\n--- EMPLEADOS ---")
    print("-" * 35)
    print(f"{'Usuario':<20} {'Rol':<10}")
    print("-" * 35)

    for nombre, datos in usuarios.items():
        print(f"{nombre:<20} {datos['tipo']:<10}")

    print("-" * 35)
