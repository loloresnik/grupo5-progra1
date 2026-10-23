import re

# ============================
# PATRONES (EXPRESIONES REGULARES)
# ============================

# Letras (con tildes y ñ), números, espacios, puntos y guiones
PATRON_TEXTO = r"^[A-Za-zÁÉÍÓÚÜáéíóúüÑñ0-9 .\-]+$"

# usuario@dominio.com / usuario@dominio.com.ar  -> grupos: usuario, dominio, extensión
PATRON_MAIL = r"^([\w.\-]+)@([\w\-]+)((\.[a-z]{2,3}){1,2})$"

# 11-45678901 / 1145678901 / 0221-4567890  -> grupos: característica y número
PATRON_TELEFONO = r"^(\d{2,4})-?(\d{6,8})$"

# dd/mm/aaaa -> grupos: día, mes y año
PATRON_FECHA = r"^(\d{1,2})/(\d{1,2})/(\d{4})$"

# Tupla inmutable con la cantidad de días de cada mes
DIAS_POR_MES = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


# ============================
# VALIDACIONES (sin input, se pueden probar con unittest)
# ============================

def validar_texto(texto):
    """Devuelve True si el texto no está vacío y solo tiene caracteres permitidos."""
    return re.fullmatch(PATRON_TEXTO, texto.strip()) is not None


def validar_mail(mail):
    """Devuelve True si el mail tiene un formato válido."""
    return re.fullmatch(PATRON_MAIL, mail.strip().lower()) is not None


def validar_telefono(telefono):
    """Devuelve True si el teléfono tiene un formato válido."""
    return re.fullmatch(PATRON_TELEFONO, telefono.strip()) is not None


def capitalizar(texto):
    """Pone en mayúscula solo la primera letra usando rebanadas: 'ssd 1TB' -> 'Ssd 1TB'"""
    texto = texto.strip()
    return texto[:1].upper() + texto[1:]


def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def convertir_fecha(texto):
    """Convierte 'dd/mm/aaaa' en la tupla (dia, mes, anio).
    Lanza ValueError si el formato o la fecha no son válidos."""

    coincidencia = re.match(PATRON_FECHA, texto.strip())

    if coincidencia is None:
        raise ValueError("La fecha debe tener el formato dd/mm/aaaa.")

    dia, mes, anio = map(int, coincidencia.groups())

    if mes < 1 or mes > 12:
        raise ValueError("Mes inválido (debe estar entre 1 y 12).")

    dias_del_mes = DIAS_POR_MES[mes - 1]

    if mes == 2 and es_bisiesto(anio):
        dias_del_mes = 29

    if dia < 1 or dia > dias_del_mes:
        raise ValueError(f"Día inválido (el mes {mes} tiene {dias_del_mes} días).")

    return (dia, mes, anio)


def convertir_entero(texto, minimo=0):
    """Convierte un texto en entero. Lanza ValueError si está vacío,
    tiene letras o es menor al mínimo permitido."""

    texto = texto.strip()

    if texto == "":
        raise ValueError("El dato no puede estar vacío.")

    try:
        numero = int(texto)
    except ValueError:
        raise ValueError("Debe ingresar un número entero (sin letras).")

    if numero < minimo:
        raise ValueError(f"El valor no puede ser menor a {minimo}.")

    return numero


def convertir_float(texto, minimo=0):
    """Igual que convertir_entero pero para números con decimales."""

    texto = texto.strip().replace(",", ".")

    if texto == "":
        raise ValueError("El dato no puede estar vacío.")

    try:
        numero = float(texto)
    except ValueError:
        raise ValueError("Debe ingresar un número (sin letras).")

    if numero < minimo:
        raise ValueError(f"El valor no puede ser menor a {minimo}.")

    return numero


# ============================
# INGRESO DE DATOS POR TECLADO
# ============================

def pedir_entero(mensaje, minimo=0, opcional=False):
    """Pide un entero hasta que sea válido.
    Si opcional es True y se deja vacío, devuelve None."""

    while True:
        texto = input(mensaje)

        if opcional and texto.strip() == "":
            return None

        try:
            return convertir_entero(texto, minimo)
        except ValueError as error:
            print("Error:", error)


def pedir_float(mensaje, minimo=0, opcional=False):
    """Pide un número decimal hasta que sea válido."""

    while True:
        texto = input(mensaje)

        if opcional and texto.strip() == "":
            return None

        try:
            return convertir_float(texto, minimo)
        except ValueError as error:
            print("Error:", error)


def pedir_texto(mensaje, validador=validar_texto, error="Dato inválido.", opcional=False):
    """Pide un texto hasta que cumpla con la función validadora."""

    while True:
        texto = input(mensaje).strip()

        if opcional and texto == "":
            return None

        if texto == "":
            print("Error: el dato no puede estar vacío.")
        elif not validador(texto):
            print("Error:", error)
        else:
            return texto


def pedir_fecha(mensaje="Fecha (dd/mm/aaaa): "):
    """Pide una fecha y la devuelve como tupla (dia, mes, anio)."""

    while True:
        try:
            return convertir_fecha(input(mensaje))
        except ValueError as error:
            print("Error:", error)
