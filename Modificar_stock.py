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
    print("1.Producto, 2.Precio, 3.Stock, 4.Precio, 5.Stock Minimo")
    modificar=int(input("Ingrese numero para modificar: "))
    while modificar<1 or modificar>5:
        print("ERROR - Ingrese un numero correctamente")
        modificar=int(input("Ingrese numero para modificar: "))

    if modificar==1:
        modificado=input("Ingrese Producto modificado: ")
        modi[2]=modificado
    elif modificar==2:
        modificado=input("Ingrese Precio modificado: ")
        modi[3]=modificado
    elif modificar==3:
        modificado=input("Ingrese Stock modificado: ")
        modi[4]=modificado
    elif modificar==4:
        modificado=input("Ingrese Precio modificado: ")
        modi[5]=modificado
    else:
        modificado=input("Ingrese Stock minimo modificado")
        modi[6]=modificado


def modificar_autoparte(motor, encendido, refrigeracion, suspension):

    codigo=int(input("Ingresar codigo de producto: "))

    while codigo<101 or codigo >499:
        print("ERROR - Ingresar codigo correctamente")
        codigo=int(input("Ingresar codigo de producto CORRECTAMENTE: "))

    if codigo >= 101 and codigo <= 199:
        final=mostrar_info(codigo,motor)
        modificar_info(final)
        print("Dato modificado")
        print(final)
        
    elif codigo >201 and codigo <299:
        final=mostrar_info(codigo,encendido)
        modificar_info(final)
        print("Dato modificado")
        print(final)

    elif codigo >301 and codigo < 399:
        final=mostrar_info(codigo,refrigeracion)
        modificar_info(final)
        print("Dato modificado")
        print(final)

    elif codigo >= 401 and codigo <= 499:
        final = mostrar_info(codigo, suspension)

    if encontrada == True:
        modificar_info(final)
        print("Dato modificado")
        print(final)

    else:
        print("Producto no encontrado")

