import re
import validaciones

# La matriz de proveedores es una lista de listas:
# proveedor = [id, nombre, telefono, mail]


# Búsqueda recursiva por ID
def buscar_proveedor_recursivo(proveedores, id_prov, i=0):
    """Recorre la matriz de forma recursiva y devuelve la fila del proveedor.
    Caso base: se llegó al final de la matriz (no existe) o se encontró el ID."""

    if i == len(proveedores):
        return None

    if proveedores[i][0] == id_prov:
        return proveedores[i]

    return buscar_proveedor_recursivo(proveedores, id_prov, i + 1)


def buscar_proveedor_por_id(proveedores, id_prov):
    return buscar_proveedor_recursivo(proveedores, id_prov)


def nombre_proveedor(proveedores, id_prov):
    """Devuelve el nombre del proveedor o 'Sin proveedor' si no existe."""
    fila = buscar_proveedor_por_id(proveedores, id_prov)
    return fila[1] if fila is not None else "Sin proveedor"


def ids_proveedores(proveedores):
    """Conjunto con los IDs de todos los proveedores."""
    return {fila[0] for fila in proveedores}


# Alta
def agregar_proveedor(proveedores, id_prov, nombre, telefono, mail):
    """Agrega un proveedor a la matriz. Lanza ValueError si algún dato es inválido."""

    if id_prov in ids_proveedores(proveedores):
        raise ValueError("Ya existe un proveedor con ese ID.")

    if not validaciones.validar_texto(nombre):
        raise ValueError("El nombre del proveedor es inválido.")

    if not validaciones.validar_telefono(telefono):
        raise ValueError("El teléfono es inválido (ej: 11-45678901).")

    if not validaciones.validar_mail(mail):
        raise ValueError("El mail es inválido (ej: ventas@empresa.com).")

    proveedores.append([id_prov, validaciones.capitalizar(nombre), telefono.strip(), mail.strip().lower()])


# Búsqueda por nombre (parcial, sin distinguir mayúsculas)
def buscar_proveedor(proveedores, texto):
    texto = texto.strip().lower()
    return [fila for fila in proveedores if texto in fila[1].lower()]


# Modificación
def modificar_proveedor(proveedores, id_prov, nuevo_nombre=None, nuevo_telefono=None, nuevo_mail=None):
    """Modifica los datos indicados (los que llegan en None no se cambian).
    Como los productos guardan el ID del proveedor, no hace falta modificarlos."""

    fila = buscar_proveedor_por_id(proveedores, id_prov)

    if fila is None:
        raise ValueError("Proveedor no encontrado.")

    if nuevo_nombre is not None:
        if not validaciones.validar_texto(nuevo_nombre):
            raise ValueError("El nombre del proveedor es inválido.")
        fila[1] = validaciones.capitalizar(nuevo_nombre)

    if nuevo_telefono is not None:
        if not validaciones.validar_telefono(nuevo_telefono):
            raise ValueError("El teléfono es inválido.")
        fila[2] = nuevo_telefono.strip()

    if nuevo_mail is not None:
        if not validaciones.validar_mail(nuevo_mail):
            raise ValueError("El mail es inválido.")
        fila[3] = nuevo_mail.strip().lower()


# Baja
def eliminar_proveedor(proveedores, id_prov, productos):
    """Solo elimina si NO hay productos asociados al proveedor."""

    fila = buscar_proveedor_por_id(proveedores, id_prov)

    if fila is None:
        raise ValueError("Proveedor no encontrado.")

    if id_prov in ids_con_productos(productos):
        raise ValueError("No se puede eliminar: el proveedor tiene productos asociados.")

    proveedores.remove(fila)


# Relación proveedor (A) -> productos (B)
def ids_con_productos(productos):
    """Conjunto con los IDs de proveedores que tienen al menos un producto."""
    return {p["id_proveedor"] for p in productos.values()}


def proveedores_sin_productos(proveedores, productos):
    """Diferencia de conjuntos: proveedores registrados que no tienen productos."""
    return ids_proveedores(proveedores) - ids_con_productos(productos)


def buscar_productos_por_proveedor(productos, proveedores, texto):
    """Busca proveedores cuyo nombre contenga el texto y devuelve sus productos.
    Se escapa el texto para que caracteres como '(' o '*' no rompan el patrón."""

    patron = re.escape(texto.strip())
    ids = {fila[0] for fila in proveedores if re.search(patron, fila[1], re.IGNORECASE)}

    return {id_prod: p for id_prod, p in productos.items() if p["id_proveedor"] in ids}


def stock_por_proveedor(productos, id_prov):
    return sum(p["stock"] for p in productos.values() if p["id_proveedor"] == id_prov)


# Mostrar
def enmascarar_mail(mail):
    """Oculta parte del mail usando rebanadas: ventas@empresa.com -> ven***@empresa.com"""
    arroba = mail.find("@")
    return mail[:arroba][:3] + "***" + mail[arroba:]


def mostrar_proveedores(proveedores):
    if len(proveedores) == 0:
        print("No hay proveedores cargados.")
        return

    print("\n--- LISTA DE PROVEEDORES ---")
    print("-" * 75)
    print(f"{'ID':<6} {'Nombre':<20} {'Telefono':<16} {'Mail':<30}")
    print("-" * 75)

    for fila in proveedores:
        print(f"{fila[0]:<6} {fila[1][:20]:<20} {fila[2]:<16} {enmascarar_mail(fila[3]):<30}")

    print("-" * 75)
