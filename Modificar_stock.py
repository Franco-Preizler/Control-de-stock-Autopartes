def mostrar_info(cod, mat):
    encontrada = False
    fila_encontrada = []

    for fila in mat:
        if fila[1] == cod:
            print(fila)
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
        modi[2] = modificado

    elif modificar == 2:
        modificado = input("Ingrese Marca modificada: ")
        modi[3] = modificado

    elif modificar == 3:
        modificado = input("Ingrese Modelo modificado: ")
        modi[4] = modificado

    elif modificar == 4:
        modificado = int(input("Ingrese Stock modificado: "))
        modi[5] = modificado

    elif modificar == 5:
        modificado = float(input("Ingrese Precio modificado: "))
        modi[6] = modificado

    else:
        modificado = int(input("Ingrese Stock minimo modificado: "))
        modi[7] = modificado

def modificar_autoparte(motor, encendido, refrigeracion, suspension):

    codigo = int(input("Ingresar codigo de producto: "))

    while codigo < 101 or codigo > 499:
        print("ERROR - Ingresar codigo correctamente")
        codigo = int(input("Ingresar codigo de producto CORRECTAMENTE: "))

    encontrada = False
    final = []

    if codigo >= 101 and codigo <= 199:
        encontrada, final = mostrar_info(codigo, motor)

    elif codigo >= 201 and codigo <= 299:
        encontrada, final = mostrar_info(codigo, encendido)

    elif codigo >= 301 and codigo <= 399:
        encontrada, final = mostrar_info(codigo, refrigeracion)

    elif codigo >= 401 and codigo <= 499:
        encontrada, final = mostrar_info(codigo, suspension)

    if encontrada == True:

        modificar_info(final)

        print("Dato modificado")
        print(final)

    else:

        print("Producto no encontrado")

