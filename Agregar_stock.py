import random
import re


def datos(rango_minimo, rango_maximo, lista):
    autoparte = input("Ingrese la autoparte que quiere agregar: ")
    while len(autoparte)<4:
        print('autoparte invalida')
        autoparte = input("Ingrese la autoparte que quiere agregar: ")


    codigo = random.randint(rango_minimo, rango_maximo)

    codigos = []

    for producto in lista:
        codigos.append(producto[1])
    
    if len(codigos) >= (rango_maximo - rango_minimo + 1):
        print("ERROR: No hay códigos disponibles")
    else:
        codigo = random.randint(rango_minimo, rango_maximo)

        while codigo in codigos:
            codigo = random.randint(rango_minimo, rango_maximo)
        marca = input("Ingrese la marca de la autoparte: ")
        while len(marca)<3 or re.search(r'\d', marca):
            print('marca invalida')
            marca = input("Ingrese la marca de la autoparte: ")
        modelo = input("Ingrese el modelo al que pertenece la autoparte: ")
        while len(modelo)<3:
            print('modelo ivalido')
            modelo = input("Ingrese el modelo al que pertenece la autoparte: ")
    
        precio = float(input("Ingrese el precio de la autoparte: "))
        while precio < 0:
            precio = float(input("Ingrese un precio valido: "))
    
        stock = int(input("Ingrese el stock existente: "))
        while stock < 0:
            stock = int(input("Ingrese un stock valido: "))
    
        stock_minimo = int(input(f"Indique el stock minimo del producto (menor o igual a {stock}): "))
        while stock_minimo < 0 or stock_minimo > stock:
            stock_minimo = int(input("Ingrese un stock minimo valido:"))
    
        return codigo, autoparte, marca, modelo, stock, precio, stock_minimo


def agregar_autoparte(motor,encendido,refrigeracion,suspension):
    alta = []
    agregar = input("Ingrese la categoria de producto que quiere agregar (Motor/Refrigeracion/Suspension/Encendido): ").lower()
    while agregar != 'motor' and agregar !='refrigeracion' and agregar != 'encendido' and agregar != 'suspension':
        print("Categoria no valida.")
        agregar = input("Ingrese la categoria de producto que quiere agregar (Motor/Refrigeracion/Suspension/Encendido): ").lower()


    if agregar == "motor":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(100, 199, motor)
        motor.append(["Motor", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
        alta.append(["Motor",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "encendido":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(200, 299, encendido)
        encendido.append(["Encendido", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
        alta.append(["Encendido",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "refrigeracion":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(300, 399, refrigeracion)
        refrigeracion.append(["Refrigeracion", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
        alta.append(["Refrigeracion",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "suspension":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(400, 499, suspension)
        suspension.append(["Suspension", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
        alta.append(["Suspension",codigo, autoparte, marca, modelo, stock, precio, stock_minimo])
    return motor,encendido,refrigeracion,suspension,alta
