import re
import os
import validaciones

ARCHIVO_PROVEEDORES = "proveedores.txt"
ARCHIVO_AUXILIAR = "proveedores_aux.txt"


def buscar_proveedor_recursivo(proveedores, id_prov, i=0):
    """Recorre la matriz de forma recursiva y devuelve la fila del proveedor."""

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

    if fila is None:
        return "Sin proveedor"

    return fila[1]


def ids_proveedores(proveedores):
    """Conjunto con los IDs de todos los proveedores."""
    ids = set()

    for fila in proveedores:
        ids.add(fila[0])

    return ids


def validar_nombre(nombre):
    """Letras (con tildes y ñ), números, espacios, puntos o guiones."""
    return re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü0-9 .\-]+$", nombre) is not None


def validar_telefono(telefono):
    """Característica de 2 a 4 dígitos, guion opcional y número de 6 a 8 dígitos. Ej: 11-45678901"""
    return re.match(r"^\d{2,4}-?\d{6,8}$", telefono) is not None


def validar_mail(mail):
    """usuario@dominio.com o usuario@dominio.com.ar"""
    return re.match(r"^[\w.\-]+@[\w\-]+(\.[a-z]{2,3}){1,2}$", mail, re.IGNORECASE) is not None


def agregar_proveedor(proveedores, id_prov, nombre, telefono, mail):
    """Agrega un proveedor a la matriz. Lanza ValueError si algún dato es inválido."""

    nombre = nombre.strip()
    telefono = telefono.strip()
    mail = mail.strip().lower()

    if id_prov in ids_proveedores(proveedores):
        raise ValueError("Ya existe un proveedor con ese ID.")

    if not validar_nombre(nombre):
        raise ValueError("El nombre del proveedor es inválido.")

    if not validar_telefono(telefono):
        raise ValueError("El teléfono es inválido (ej: 11-45678901).")

    if not validar_mail(mail):
        raise ValueError("El mail es inválido (ej: ventas@empresa.com).")

    proveedores.append([id_prov, nombre, telefono, mail])


def buscar_proveedor(proveedores, texto):
    texto = texto.strip()

    if texto == "":
        return []

    return [fila for fila in proveedores if texto.lower() in fila[1].lower()]


def modificar_proveedor(proveedores, id_prov, nuevo_nombre, nuevo_telefono, nuevo_mail):
    """Modifica los datos indicados, como los productos guardan el ID del proveedor, no hace falta modificarlos."""

    fila = buscar_proveedor_por_id(proveedores, id_prov)

    if fila is None:
        raise ValueError("Proveedor no encontrado.")

    if nuevo_nombre is not None:
        nuevo_nombre = nuevo_nombre.strip()

        if not validar_nombre(nuevo_nombre):
            raise ValueError("El nombre del proveedor es inválido.")

        fila[1] = nuevo_nombre

    if nuevo_telefono is not None:
        nuevo_telefono = nuevo_telefono.strip()

        if not validar_telefono(nuevo_telefono):
            raise ValueError("El teléfono es inválido.")

        fila[2] = nuevo_telefono

    if nuevo_mail is not None:
        nuevo_mail = nuevo_mail.strip().lower()

        if not validar_mail(nuevo_mail):
            raise ValueError("El mail es inválido.")

        fila[3] = nuevo_mail


def eliminar_proveedor(proveedores, id_prov, productos):
    """Solo elimina si NO hay productos asociados al proveedor."""

    fila = buscar_proveedor_por_id(proveedores, id_prov)

    if fila is None:
        raise ValueError("Proveedor no encontrado.")

    if id_prov in ids_con_productos(productos):
        raise ValueError("No se puede eliminar: el proveedor tiene productos asociados.")

    proveedores.remove(fila)


def ids_con_productos(productos):
    """Conjunto con los IDs de proveedores que tienen al menos un producto."""
    ids = set()

    for p in productos.values():
        ids.add(p["id_proveedor"])

    return ids


def proveedores_sin_productos(proveedores, productos):
    """Diferencia de conjuntos: proveedores registrados que no tienen productos."""
    return ids_proveedores(proveedores) - ids_con_productos(productos)


def buscar_productos_por_proveedor(productos, proveedores, texto):
    """Busca los proveedores cuyo nombre contiene el texto y devuelve sus productos."""

    texto = texto.strip()
    ids = set()

    if texto == "":
        return {}

    for fila in proveedores:
        if texto.lower() in fila[1].lower():
            ids.add(fila[0])

    resultado = {}

    for id_prod, p in productos.items():
        if p["id_proveedor"] in ids:
            resultado[id_prod] = p

    return resultado


def stock_por_proveedor(productos, id_prov):
    return sum(p["stock"] for p in productos.values() if p["id_proveedor"] == id_prov)


def mostrar_proveedores(proveedores):
    if len(proveedores) == 0:
        print("No hay proveedores cargados.")
        return

    print("\n--- LISTA DE PROVEEDORES ---")
    print("-" * 75)
    print(f"{'ID':<6} {'Nombre':<20} {'Telefono':<16} {'Mail':<30}")
    print("-" * 75)

    for fila in proveedores:
        print(f"{fila[0]:<6} {fila[1][:20]:<20} {fila[2]:<16} {fila[3]:<30}")

    print("-" * 75)


# Alta de proveedor (pide los datos)
def alta_proveedor(proveedores):
    """Pide los datos del proveedor y lo agrega a la matriz.
    Si algún dato es inválido, muestra el error y no lo agrega."""

    print("\n=== AGREGAR PROVEEDOR ===")

    id_prov = validaciones.pedir_entero("Ingrese ID del proveedor: ")

    nombre = input("Ingrese nombre del proveedor: ")

    telefono = input("Ingrese teléfono (ej: 11-45678901): ")

    mail = input("Ingrese mail: ")

    try:

        agregar_proveedor(proveedores, id_prov, nombre, telefono, mail)

    except ValueError as error:

        print("Error:", error)

        return 0

    agregar_proveedor_txt(buscar_proveedor_por_id(proveedores, id_prov))

    print("Proveedor agregado correctamente.")

    return 1


# Consultar proveedor por nombre
def consultar_proveedor(proveedores):
    """Pide un texto y muestra los proveedores cuyo nombre lo contiene."""

    print("\n=== BUSCAR PROVEEDOR ===")

    texto = input("Ingrese nombre o parte del nombre: ")

    resultado = buscar_proveedor(proveedores, texto)

    if len(resultado) == 0:

        print("Proveedor no encontrado.")

        return 0

    mostrar_proveedores(resultado)

    return 1


# Modificar proveedor (pide los datos)
def editar_proveedor(proveedores):
    """Pide el ID y los datos nuevos. Si un campo se deja vacío, no se modifica."""

    print("\n=== MODIFICAR PROVEEDOR ===")

    id_prov = validaciones.pedir_entero("Ingrese ID del proveedor a modificar: ")

    if buscar_proveedor_por_id(proveedores, id_prov) is None:

        print("Proveedor no encontrado.")

        return 0

    print("Deje vacío un campo si no desea modificarlo.")

    nuevo_nombre = input("Nuevo nombre: ").strip()

    nuevo_telefono = input("Nuevo teléfono: ").strip()

    nuevo_mail = input("Nuevo mail: ").strip()

    if nuevo_nombre == "":

        nuevo_nombre = None

    if nuevo_telefono == "":

        nuevo_telefono = None

    if nuevo_mail == "":

        nuevo_mail = None

    try:

        modificar_proveedor(proveedores, id_prov, nuevo_nombre, nuevo_telefono, nuevo_mail)

    except ValueError as error:

        print("Error:", error)

        return 0

    modificar_proveedor_txt(buscar_proveedor_por_id(proveedores, id_prov))

    print("Proveedor modificado correctamente.")

    return 1


# Baja de proveedor (pide el ID)
def baja_proveedor(proveedores, productos):
    """Pide el ID y elimina el proveedor si no tiene productos asociados."""

    print("\n=== ELIMINAR PROVEEDOR ===")

    id_prov = validaciones.pedir_entero("Ingrese ID del proveedor a eliminar: ")

    try:

        eliminar_proveedor(proveedores, id_prov, productos)

    except ValueError as error:

        print("Error:", error)

        return 0

    eliminar_proveedor_txt(id_prov)

    print("Proveedor eliminado.")

    return 1


# Productos de un proveedor
def mostrar_productos_de_proveedor(productos, proveedores):
    """Pide parte del nombre de un proveedor y muestra sus productos."""

    print("\n=== PRODUCTOS POR PROVEEDOR ===")

    texto = input("Ingrese nombre o parte del nombre del proveedor: ")

    resultado = buscar_productos_por_proveedor(productos, proveedores, texto)

    if len(resultado) == 0:

        print("No se encontraron productos.")

        return 0

    print("-" * 70)
    print(f"{'ID':<8} {'Producto':<20} {'Proveedor':<20} {'Stock':>8}")
    print("-" * 70)

    for id_prod, p in resultado.items():

        nombre_prov = nombre_proveedor(proveedores, p["id_proveedor"])

        print(f"{id_prod:<8} {p['nombre'][:20]:<20} {nombre_prov[:20]:<20} {p['stock']:>8}")

    print("-" * 70)

    return 1


# Stock total de un proveedor
def mostrar_stock_por_proveedor(productos, proveedores):
    """Pide el ID de un proveedor y muestra la suma del stock de sus productos."""

    print("\n=== STOCK POR PROVEEDOR ===")

    id_prov = validaciones.pedir_entero("Ingrese ID del proveedor: ")

    if buscar_proveedor_por_id(proveedores, id_prov) is None:

        print("Proveedor no encontrado.")

        return 0

    total = stock_por_proveedor(productos, id_prov)

    print(f"Stock total de {nombre_proveedor(proveedores, id_prov)}: {total}")

    return 1


# Proveedores sin productos (diferencia de conjuntos)
def mostrar_proveedores_sin_productos(proveedores, productos):
    """Muestra los proveedores registrados que no tienen ningún producto."""

    ids = proveedores_sin_productos(proveedores, productos)

    if len(ids) == 0:

        print("Todos los proveedores tienen productos.")

        return

    print("\n--- PROVEEDORES SIN PRODUCTOS ---")

    for id_prov in sorted(ids):

        print(f"{id_prov:<6} {nombre_proveedor(proveedores, id_prov)}")


# ============================
# ARCHIVO DE TEXTO (proveedores.txt)
# Formato de cada línea: id;nombre;telefono;mail
# ============================

# Armar la línea de un proveedor
def linea_proveedor(fila):
    """Convierte una fila de la matriz en una línea del archivo."""

    return f"{fila[0]};{fila[1]};{fila[2]};{fila[3]}\n"


# Cargar proveedores
def cargar_proveedores_txt():
    """Lee proveedores.txt línea por línea y arma la matriz.
    Si el archivo no existe, devuelve una matriz vacía.
    Las líneas con datos inválidos se informan y se saltean."""

    proveedores = []

    try:

        with open(ARCHIVO_PROVEEDORES, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                datos = linea.strip().split(";")

                try:

                    proveedores.append([int(datos[0]), datos[1], datos[2], datos[3]])

                except (ValueError, IndexError):

                    print("Se ignora una línea inválida de proveedores.txt:", linea.strip())

    except FileNotFoundError:

        return []

    except OSError as error:

        print("Error al leer proveedores:", error)

    return proveedores


# Alta en el archivo (modo append)
def agregar_proveedor_txt(fila):
    """Agrega el proveedor al final de proveedores.txt."""

    try:

        with open(ARCHIVO_PROVEEDORES, "a", encoding="utf-8") as archivo:

            archivo.write(linea_proveedor(fila))

        return 1

    except OSError as error:

        print("Error al guardar el proveedor:", error)

        return 0


# Modificación en el archivo (con archivo auxiliar)
def modificar_proveedor_txt(fila_nueva):
    """Copia proveedores.txt en un archivo auxiliar reemplazando la línea
    del proveedor modificado, y después el auxiliar pasa a ser el original."""

    try:

        with open(ARCHIVO_PROVEEDORES, "r", encoding="utf-8") as original:

            with open(ARCHIVO_AUXILIAR, "w", encoding="utf-8") as auxiliar:

                for linea in original:

                    datos = linea.strip().split(";")

                    if datos[0] == str(fila_nueva[0]):

                        auxiliar.write(linea_proveedor(fila_nueva))

                    else:

                        auxiliar.write(linea)

        os.remove(ARCHIVO_PROVEEDORES)

        os.rename(ARCHIVO_AUXILIAR, ARCHIVO_PROVEEDORES)

        return 1

    except OSError as error:

        print("Error al modificar el archivo de proveedores:", error)

        return 0


# Baja en el archivo (con archivo auxiliar)
def eliminar_proveedor_txt(id_prov):
    """Copia proveedores.txt en un archivo auxiliar salteando la línea
    del proveedor eliminado, y después el auxiliar pasa a ser el original."""

    try:

        with open(ARCHIVO_PROVEEDORES, "r", encoding="utf-8") as original:

            with open(ARCHIVO_AUXILIAR, "w", encoding="utf-8") as auxiliar:

                for linea in original:

                    datos = linea.strip().split(";")

                    if datos[0] != str(id_prov):

                        auxiliar.write(linea)

        os.remove(ARCHIVO_PROVEEDORES)

        os.rename(ARCHIVO_AUXILIAR, ARCHIVO_PROVEEDORES)

        return 1

    except OSError as error:

        print("Error al eliminar del archivo de proveedores:", error)

        return 0
