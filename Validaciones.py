"""Funciones para pedir datos por teclado y validarlos hasta que sean correctos."""
import re

# Patrones de caracteres NO permitidos (se buscan con re.search).
# Ninguno permite comas porque la coma separa los campos en movimientos.txt.
PATRON_NOMBRE = r'[^\w ]'   # solo letras (incluye tildes y ñ), numeros y espacios
PATRON_MARCA = r'[\d,]'     # no se permiten numeros ni comas
PATRON_MODELO = r','        # no se permiten comas


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("ERROR - Ingrese un numero entero.")
            continue

        if minimo is not None and valor < minimo:
            print(f"ERROR - El valor no puede ser menor a {minimo}.")
        elif maximo is not None and valor > maximo:
            print(f"ERROR - El valor no puede ser mayor a {maximo}.")
        else:
            return valor


def pedir_decimal(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("ERROR - Ingrese un numero valido.")
            continue

        if valor != valor or valor in (float("inf"), float("-inf")):
            print("ERROR - Ingrese un numero valido.")
        elif minimo is not None and valor < minimo:
            print(f"ERROR - El valor no puede ser menor a {minimo}.")
        else:
            return valor


def pedir_texto(mensaje, longitud_minima=1, patron_invalido=None, mensaje_error="Valor invalido"):
    while True:
        # strip() quita los espacios de los extremos: "    " cuenta como dato vacio.
        valor = input(mensaje).strip()
        if len(valor) < longitud_minima:
            print(mensaje_error)
            continue
        if patron_invalido and re.search(patron_invalido, valor):
            print(mensaje_error)
            continue
        return valor


# Validaciones de cada campo de texto de una autoparte.
# Se usan igual en el alta y en la modificacion, asi la regla es la misma en los dos casos.
def pedir_nombre(mensaje):
    return pedir_texto(mensaje, 4, PATRON_NOMBRE,
                       "ERROR - Minimo 4 caracteres. Solo letras, numeros y espacios.")


def pedir_marca(mensaje):
    return pedir_texto(mensaje, 3, PATRON_MARCA,
                       "ERROR - Minimo 3 caracteres. No puede tener numeros ni comas.")


def pedir_modelo(mensaje):
    return pedir_texto(mensaje, 3, PATRON_MODELO,
                       "ERROR - Minimo 3 caracteres. No puede tener comas.")
