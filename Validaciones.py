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
