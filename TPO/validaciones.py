import re

PATRON_TEXTO = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+$"

# Pedir un número entero
def pedir_entero(mensaje, opcional=False):
    """Pide un número entero positivo hasta que el ingreso sea válido.
    Si opcional es True y se deja vacío, devuelve None."""

    valor = input(mensaje).strip()

    while re.match(r"^\d+$", valor) is None:

        if opcional and valor == "":

            return None

        print("Debe ingresar un número entero.")

        valor = input(mensaje).strip()

    return int(valor)

# Pedir un texto
def pedir_texto(mensaje, opcional=False):
    """Pide un texto que solo tenga letras (con tildes y ñ) y espacios.
    Si opcional es True y se deja vacío, devuelve None."""

    texto = input(mensaje).strip()

    while re.match(PATRON_TEXTO, texto) is None:

        if opcional and texto == "":

            return None

        print("Solo se permiten letras y espacios.")

        texto = input(mensaje).strip()

    return texto
