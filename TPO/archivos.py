import json
import os

# La carpeta "datos" se ubica al lado de este archivo, así el sistema funciona
# en cualquier computadora y desde cualquier carpeta (no se usan rutas absolutas fijas).
RUTA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos")

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_VENTAS = "ventas.json"
ARCHIVO_PROVEEDORES = "proveedores.txt"
ARCHIVO_MOVIMIENTOS = "movimientos.txt"

USUARIOS_INICIALES = {
    "admin": {"clave": "1234", "tipo": "admin"},
    "usuario": {"clave": "1234", "tipo": "usuario"}
}


def ruta(nombre_archivo, carpeta=RUTA_DATOS):
    return os.path.join(carpeta, nombre_archivo)


# ============================
# ARCHIVOS JSON
# ============================

def guardar_json(datos, nombre_archivo, carpeta=RUTA_DATOS):
    os.makedirs(carpeta, exist_ok=True)

    with open(ruta(nombre_archivo, carpeta), "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def leer_json(nombre_archivo, carpeta=RUTA_DATOS):
    """Lee un archivo JSON. Si no existe o está dañado devuelve un diccionario vacío."""

    try:
        with open(ruta(nombre_archivo, carpeta), "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print(f"Aviso: no existe el archivo {nombre_archivo}. Se empieza sin datos.")

    except json.JSONDecodeError:
        print(f"Aviso: el archivo {nombre_archivo} está dañado. Se empieza sin datos.")

    return {}


def claves_a_entero(diccionario):
    """JSON guarda las claves como texto: {"1001": ...} -> {1001: ...}"""

    resultado = {}

    for clave, valor in diccionario.items():
        try:
            resultado[int(clave)] = valor
        except ValueError:
            print(f"Aviso: se ignora el registro con ID inválido '{clave}'.")

    return resultado


def leer_productos(carpeta=RUTA_DATOS):
    return claves_a_entero(leer_json(ARCHIVO_PRODUCTOS, carpeta))


def leer_ventas(carpeta=RUTA_DATOS):
    return claves_a_entero(leer_json(ARCHIVO_VENTAS, carpeta))


def leer_usuarios(carpeta=RUTA_DATOS):
    usuarios = leer_json(ARCHIVO_USUARIOS, carpeta)

    # Si no hay usuarios guardados se crean los iniciales para poder ingresar
    if len(usuarios) == 0:
        usuarios = dict(USUARIOS_INICIALES)

    return usuarios


# ============================
# ARCHIVOS DE TEXTO (separados por ;)
# ============================

def guardar_proveedores_txt(proveedores, carpeta=RUTA_DATOS):
    os.makedirs(carpeta, exist_ok=True)

    with open(ruta(ARCHIVO_PROVEEDORES, carpeta), "w", encoding="utf-8") as archivo:
        for fila in proveedores:
            archivo.write(f"{fila[0]};{fila[1]};{fila[2]};{fila[3]}\n")


def leer_proveedores_txt(carpeta=RUTA_DATOS):
    """Lee la matriz de proveedores. Ignora líneas dañadas y IDs repetidos."""

    proveedores = []
    ids_leidos = set()

    try:
        with open(ruta(ARCHIVO_PROVEEDORES, carpeta), "r", encoding="utf-8") as archivo:
            for numero, linea in enumerate(archivo, start=1):
                linea = linea.strip()

                if linea == "":
                    continue

                try:
                    id_prov, nombre, telefono, mail = linea.split(";")
                    id_prov = int(id_prov)
                except ValueError:
                    print(f"Aviso: línea {numero} de {ARCHIVO_PROVEEDORES} dañada, se ignora.")
                    continue

                if id_prov in ids_leidos:
                    print(f"Aviso: proveedor {id_prov} repetido en el archivo, se ignora.")
                    continue

                ids_leidos.add(id_prov)
                proveedores.append([id_prov, nombre, telefono, mail])

    except FileNotFoundError:
        print(f"Aviso: no existe el archivo {ARCHIVO_PROVEEDORES}. Se empieza sin datos.")

    return proveedores


def guardar_movimientos_txt(movimientos, carpeta=RUTA_DATOS):
    os.makedirs(carpeta, exist_ok=True)

    with open(ruta(ARCHIVO_MOVIMIENTOS, carpeta), "w", encoding="utf-8") as archivo:
        for tipo, id_prod, cantidad, (dia, mes, anio) in movimientos:
            archivo.write(f"{tipo};{id_prod};{cantidad};{dia}/{mes}/{anio}\n")


def leer_movimientos_txt(carpeta=RUTA_DATOS):
    movimientos = []

    try:
        with open(ruta(ARCHIVO_MOVIMIENTOS, carpeta), "r", encoding="utf-8") as archivo:
            for numero, linea in enumerate(archivo, start=1):
                linea = linea.strip()

                if linea == "":
                    continue

                try:
                    tipo, id_prod, cantidad, fecha = linea.split(";")
                    dia, mes, anio = fecha.split("/")
                    movimientos.append([tipo, int(id_prod), int(cantidad), (int(dia), int(mes), int(anio))])
                except ValueError:
                    print(f"Aviso: línea {numero} de {ARCHIVO_MOVIMIENTOS} dañada, se ignora.")

    except FileNotFoundError:
        print(f"Aviso: no existe el archivo {ARCHIVO_MOVIMIENTOS}. Se empieza sin datos.")

    return movimientos


# ============================
# CARGAR Y GUARDAR TODO
# ============================

def cargar_datos(carpeta=RUTA_DATOS):
    """Devuelve un diccionario con toda la información del sistema."""

    return {
        "productos": leer_productos(carpeta),
        "proveedores": leer_proveedores_txt(carpeta),
        "movimientos": leer_movimientos_txt(carpeta),
        "ventas": leer_ventas(carpeta),
        "usuarios": leer_usuarios(carpeta)
    }


def guardar_datos(datos, carpeta=RUTA_DATOS):
    try:
        guardar_json(datos["productos"], ARCHIVO_PRODUCTOS, carpeta)
        guardar_json(datos["ventas"], ARCHIVO_VENTAS, carpeta)
        guardar_json(datos["usuarios"], ARCHIVO_USUARIOS, carpeta)
        guardar_proveedores_txt(datos["proveedores"], carpeta)
        guardar_movimientos_txt(datos["movimientos"], carpeta)
    except OSError as error:
        print("Error al guardar los datos:", error)
