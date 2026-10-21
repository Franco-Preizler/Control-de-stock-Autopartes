import random
import re
from Validaciones import pedir_entero, pedir_decimal


def datos(rango_minimo, rango_maximo, lista):
    autoparte = input("Ingrese la autoparte que quiere agregar: ")
    while len(autoparte)<4:
        print('autoparte invalida')
        autoparte = input("Ingrese la autoparte que quiere agregar: ")


    codigos = []

    for producto in lista:
        codigos.append(producto[1])
    
    codigo = random.randint(rango_minimo, rango_maximo)
    
    while codigo in codigos:
        codigo = random.randint(rango_minimo, rango_maximo)
    marca = input("Ingrese la marca de la autoparte: ")
    while len(marca) < 3 or re.search(r'^\s*$|\d', marca):
        print('marca invalida')
        marca = input("Ingrese la marca de la autoparte: ")
    modelo = input("Ingrese el modelo al que pertenece la autoparte: ")
    while len(modelo)<3:
        print('modelo ivalido')
        modelo = input("Ingrese el modelo al que pertenece la autoparte: ")

    precio = pedir_decimal("Ingrese el precio de la autoparte: ", 0)
    stock = pedir_entero("Ingrese el stock existente: ", 0)
    stock_minimo = pedir_entero(f"Indique el stock minimo del producto (menor o igual a {stock}): ", 0, stock)

    return codigo, autoparte, marca, modelo, stock, precio, stock_minimo


def agregar_autoparte(motor,encendido,refrigeracion,suspension):
    alta = []
    agregar = input("Ingrese la categoria de producto que quiere agregar (Motor/Refrigeracion/Suspension/Encendido): ").lower()
    while agregar != 'motor' and agregar !='refrigeracion' and agregar != 'encendido' and agregar != 'suspension':
        print("Categoria no valida.")
        agregar = input("Ingrese la categoria de producto que quiere agregar (Motor/Refrigeracion/Suspension/Encendido): ").lower()


    if agregar == "motor":
        if len(motor) >= 100:
            print("ERROR: No hay códigos disponibles")
        else:
            codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(100, 199, motor)
            motor.append(["Motor", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
            alta.append(["Motor",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "encendido":
        if len(encendido) >= 100:
            print("ERROR: No hay códigos disponibles")
        else:
            codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(200, 299, encendido)
            encendido.append(["Encendido", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
            alta.append(["Encendido",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "refrigeracion":
        if len(refrigeracion) >= 100:
            print("ERROR: No hay códigos disponibles")
        else:
            codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(300, 399, refrigeracion)
            refrigeracion.append(["Refrigeracion", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
            alta.append(["Refrigeracion",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "suspension":
        if len(suspension) >= 100:
            print("ERROR: No hay códigos disponibles")
        else:
            codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(400, 499, suspension)
            suspension.append(["Suspension", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
            alta.append(["Suspension",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
    return motor,encendido,refrigeracion,suspension,alta
