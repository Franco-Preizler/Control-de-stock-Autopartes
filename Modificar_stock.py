import re


def mostrar_info(cod, mat):
    encontrada = False
    fila_encontrada = []

    for fila in mat:
        if fila[1] == cod:
            fila_encontrada = fila
            encontrada = True

    return encontrada, fila_encontrada
    
def modificar_info(modi):

    print("1.Producto, 2.Marca, 3.Modelo, 4.Stock, 5.Precio, 6.Stock Minimo")

    modificar = int(input("Ingrese numero para modificar: "))

    while modificar < 1 or modificar > 6:
        print("ERROR - Ingrese un numero correctamente")
        modificar = int(input("Ingrese numero para modificar: "))

    if modificar == 1:
        modificado = input("Ingrese Producto modificado: ")
        while len(modificado) < 4 or re.search(r'^\s*$|[^a-zA-Z0-9 ]', modificado):
            print("Producto invalido")
            modificado = input("Ingrese Producto modificado: ")
        modi[2] = modificado

    elif modificar == 2:
        modificado = input("Ingrese Marca modificada: ")
        while len(modificado) < 3 or re.search(r'\d', modificado):
            print("Marca invalida")
            modificado = input("Ingrese Marca modificada: ")
        modi[3] = modificado

    elif modificar == 3:
        modificado = input("Ingrese Modelo modificado: ")
        while len(modificado) < 3:
            print("Modelo invalido")
            modificado = input("Ingrese Modelo modificado: ")
        modi[4] = modificado

    elif modificar == 4:
        modificado = int(input("Ingrese Stock modificado: "))
        while modificado < 0:
            print("El stock no puede ser negativo")
            modificado = int(input("Ingrese Stock modificado: "))
        modi[5] = modificado

    elif modificar == 5:
        modificado = float(input("Ingrese Precio modificado: "))
        while modificado < 0:
            print("ERROR - El precio no puede ser negativo")
            modificado = float(input("Ingrese Precio modificado: "))
        modi[6] = modificado

    else:
        modificado = int(input("Ingrese Stock minimo modificado: "))
        while modificado < 0 or modificado > modi[5]:
            print("ERROR - El stock minimo no puede ser negativo")
            modificado = int(input("Ingrese Stock minimo modificado: "))
        modi[7] = modificado

def modificar_autoparte(motor, encendido, refrigeracion, suspension):

    codigo = int(input("Ingresar codigo de producto: "))

    while codigo < 100 or codigo > 499:
        print("ERROR - Ingresar codigo correctamente")
        codigo = int(input("Ingresar codigo de producto CORRECTAMENTE: "))

    encontrada = False
    final = []

    if codigo >= 100 and codigo < 200:
        encontrada, final = mostrar_info(codigo, motor)

    elif codigo >= 200 and codigo < 300:
        encontrada, final = mostrar_info(codigo, encendido)

    elif codigo >= 300 and codigo < 400:
        encontrada, final = mostrar_info(codigo, refrigeracion)

    elif codigo >= 400 and codigo < 500:
        encontrada, final = mostrar_info(codigo, suspension)

    if encontrada == True:

        antes = final.copy()
        modificar_info(final)

        print("Dato modificado")
        print("Antes:", antes)
        print("Despues:", final)
    else:

        print("Producto no encontrado")
    return final
