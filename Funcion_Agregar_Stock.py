
import random


def datos(rango_minimo, rango_maximo, lista):
    autoparte = input("Ingrese la autoparte que quiere agregar: ")

    codigo = random.randint(rango_minimo, rango_maximo)

    codigos = [producto[1] for producto in lista]

    while codigo in codigos:
        codigo = random.randint(rango_minimo, rango_maximo)

    marca = input("Ingrese la marca de la autoparte: ")
    modelo = input("Ingrese el modelo al que pertenece la autoparte: ")

    precio = float(input("Ingrese el precio de la autoparte: "))
    while precio < 0:
        precio = float(input("Ingrese un precio válido: "))

    stock = int(input("Ingrese el stock existente: "))
    while stock < 0:
        stock = int(input("Ingrese un stock válido: "))

    stock_minimo = int(input("Indique el stock mínimo del producto: "))
    while stock_minimo < 0:
        stock_minimo = int(input("Ingrese un stock mínimo válido: "))

    return codigo, autoparte, marca, modelo, stock, precio, stock_minimo


def agregar_autoparte():

    motor = [
        ["Motor", 101, "Filtro de aceite", "BGK", "Volkswagen Polo", 6, 71000, 5],
        ["Motor", 102, "Correa de distribución", "BGK", "Peugeot 208", 7, 40000, 5],
        ["Motor", 103, "Bomba de aceite", "BGK", "Volkswagen Polo", 9, 43000, 5],
        ["Motor", 104, "Junta de culata", "BGK", "Volkswagen Polo", 11, 59000, 5],
        ["Motor", 105, "Pistón", "BGK", "Volkswagen Polo", 17, 56000, 5]
    ]

    encendido = [
        ["Encendido", 201, "Bujía", "NGK", "Universal", 19, 18900, 5],
        ["Encendido", 202, "Bobina de encendido", "Bosch", "Universal", 25, 34800, 5],
        ["Encendido", 203, "Cables de bujía", "Bosch", "Universal", 30, 23600, 5],
        ["Encendido", 204, "Distribuidor", "Bosch", "Universal", 13, 23000, 5],
        ["Encendido", 205, "Motor de arranque", "Bosch", "Universal", 9, 32000, 5]
    ]

    refrigeracion = [
        ["Refrigeración", 301, "Radiador", "Valeo", "Universal", 17, 15900, 5],
        ["Refrigeración", 302, "Bomba de agua", "SKF", "Universal", 24, 1090, 5],
        ["Refrigeración", 303, "Termostato", "Gates", "Universal", 70, 9500, 5],
        ["Refrigeración", 304, "Electroventilador", "Valeo", "Universal", 45, 9200, 5],
        ["Refrigeración", 305, "Manguera de radiador", "Gates", "Universal", 80, 8900, 5]
    ]

    suspension = [
        ["Suspensión", 401, "Amortiguador delantero", "Monroe", "Universal", 22, 4500, 5],
        ["Suspensión", 402, "Amortiguador trasero", "Monroe", "Universal", 25, 4800, 5],
        ["Suspensión", 403, "Rótula", "TRW", "Universal", 28, 5800, 5],
        ["Suspensión", 404, "Bieleta", "TRW", "Universal", 9, 5700, 5],
        ["Suspensión", 405, "Bujes de suspensión", "TRW", "Universal", 24, 5000, 5]
    ]

    agregar = input(
        "Ingrese la categoría de producto que quiere agregar: "
    ).lower()

    if agregar == "motor":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(100, 200, motor)
        motor.append(["Motor", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "encendido":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(200, 300, encendido)
        encendido.append(["Encendido", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "refrigeracion":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(300, 400, refrigeracion)
        refrigeracion.append(["Refrigeración", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    elif agregar == "suspension":
        codigo, autoparte, marca, modelo, stock, precio, stock_minimo = datos(400, 500, suspension)
        suspension.append(
            ["Suspensión", codigo, autoparte, marca, modelo, stock, precio, stock_minimo])

    else:
        print("Categoría no válida.")

