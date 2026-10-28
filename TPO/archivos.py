import json

# Los archivos se guardan en la misma carpeta desde donde se ejecuta el programa.
# Se usa solo el nombre del archivo (ej: "productos.json"), nunca una ruta como C:/Users/...


# ============================
# ARCHIVOS JSON
# ============================

def guardar_json(datos, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def leer_json(nombre_archivo):
    """Lee un archivo JSON. Si no existe o está dañado devuelve un diccionario vacío."""

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print(f"Aviso: no existe el archivo {nombre_archivo}. Se empieza sin datos.")

    except ValueError:
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


def leer_productos():
    return claves_a_entero(leer_json("productos.json"))


def leer_ventas():
    return claves_a_entero(leer_json("ventas.json"))


def leer_usuarios():
    usuarios = leer_json("usuarios.json")

    # Si no hay usuarios guardados se crean los iniciales para poder ingresar
    if len(usuarios) == 0:
        usuarios = {
            "admin": {"clave": "1234", "tipo": "admin"},
            "usuario": {"clave": "1234", "tipo": "usuario"}
        }

    return usuarios


# ============================
# ARCHIVOS DE TEXTO (separados por ;)
# ============================

def guardar_proveedores_txt(proveedores):
    with open("proveedores.txt", "w", encoding="utf-8") as archivo:
        for fila in proveedores:
            archivo.write(f"{fila[0]};{fila[1]};{fila[2]};{fila[3]}\n")


def leer_proveedores_txt():
    """Lee la matriz de proveedores. Ignora líneas dañadas y IDs repetidos."""

    proveedores = []
    ids_leidos = set()

    try:
        with open("proveedores.txt", "r", encoding="utf-8") as archivo:
            numero = 0

            for linea in archivo:
                numero += 1
                linea = linea.strip()

                if linea == "":
                    continue

                try:
                    id_prov, nombre, telefono, mail = linea.split(";")
                    id_prov = int(id_prov)
                except ValueError:
                    print(f"Aviso: línea {numero} de proveedores.txt dañada, se ignora.")
                    continue

                if id_prov in ids_leidos:
                    print(f"Aviso: proveedor {id_prov} repetido en el archivo, se ignora.")
                    continue

                ids_leidos.add(id_prov)
                proveedores.append([id_prov, nombre, telefono, mail])

    except FileNotFoundError:
        print("Aviso: no existe el archivo proveedores.txt. Se empieza sin datos.")

    return proveedores


def guardar_movimientos_txt(movimientos):
    with open("movimientos.txt", "w", encoding="utf-8") as archivo:
        for tipo, id_prod, cantidad, (dia, mes, anio) in movimientos:
            archivo.write(f"{tipo};{id_prod};{cantidad};{dia}/{mes}/{anio}\n")


def leer_movimientos_txt():
    movimientos = []

    try:
        with open("movimientos.txt", "r", encoding="utf-8") as archivo:
            numero = 0

            for linea in archivo:
                numero += 1
                linea = linea.strip()

                if linea == "":
                    continue

                try:
                    tipo, id_prod, cantidad, fecha = linea.split(";")
                    dia, mes, anio = fecha.split("/")
                    movimientos.append([tipo, int(id_prod), int(cantidad), (int(dia), int(mes), int(anio))])
                except ValueError:
                    print(f"Aviso: línea {numero} de movimientos.txt dañada, se ignora.")

    except FileNotFoundError:
        print("Aviso: no existe el archivo movimientos.txt. Se empieza sin datos.")

    return movimientos


# ============================
# CARGAR Y GUARDAR TODO
# ============================

def cargar_datos():
    """Devuelve un diccionario con toda la información del sistema."""

    return {
        "productos": leer_productos(),
        "proveedores": leer_proveedores_txt(),
        "movimientos": leer_movimientos_txt(),
        "ventas": leer_ventas(),
        "usuarios": leer_usuarios()
    }


def guardar_datos(datos):
    try:
        guardar_json(datos["productos"], "productos.json")
        guardar_json(datos["ventas"], "ventas.json")
        guardar_json(datos["usuarios"], "usuarios.json")
        guardar_proveedores_txt(datos["proveedores"])
        guardar_movimientos_txt(datos["movimientos"])
    except OSError as error:
        print("Error al guardar los datos:", error)
