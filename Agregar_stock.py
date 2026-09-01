import random


def datos(rango_minimo, rango_maximo, lista):
    autoparte = input("Ingrese la autoparte que quiere agregar: ")
    while len(autoparte)<4:
        print('autoparte invalida')
        autoparte = input("Ingrese la autoparte que quiere agregar: ")


    codigo = random.randint(rango_minimo, rango_maximo)

    codigos = [producto[1] for producto in lista]

    while codigo in codigos:
        codigo = random.randint(rango_minimo, rango_maximo)

    marca = input("Ingrese la marca de la autoparte: ")
    while len(marca)<3:
        print('marca invalida')
        marca = input("Ingrese la marca de la autoparte: ")
    modelo = input("Ingrese el modelo al que pertenece la autoparte: ")
    while len(modelo)<3:
        print('modelo ivalido')
        modelo = input("Ingrese el modelo al que pertenece la autoparte: ")

    precio = float(input("Ingrese el precio de la autoparte: "))
    while precio < 0:
        precio = float(input("Ingrese un precio válido: "))

    stock = int(input("Ingrese el stock existente: "))
    while stock < 0:
        stock = int(input("Ingrese un stock válido: "))

    stock_minimo = int(input(f"Indique el stock mínimo del producto (mayor o igual a {stock}): "))
    while stock_minimo > stock:
        stock_minimo = int(input("Ingrese un stock minimo valido:"))

    return codigo, autoparte, marca, modelo, stock, precio, stock_minimo


def agregar_autoparte(motor,encendido,refrigeracion,suspension):

    agregar = input("Ingrese la categoría de producto que quiere agregar: ").lower()
    while agregar != 'motor' and agregar !='refrigeracion' and agregar != 'encendido' and agregar != 'suspension':
        print("Categoría no válida.")
        agregar = input("Ingrese la categoría de producto que quiere agregar: ").lower()


    if agregar == "motor":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(101, 199, motor)
        motor.append(["Motor", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "encendido":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(201, 299, encendido)
        encendido.append(["Encendido", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "refrigeracion":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(301, 399, refrigeracion)
        refrigeracion.append(["Refrigeración", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "suspension":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(401, 499, suspension)
        suspension.append(
            ["Suspensión", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])