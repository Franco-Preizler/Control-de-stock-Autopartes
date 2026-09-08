from Agregar_stock import agregar_autoparte
from Modificar_stock import *
from eliminarap import eliminar_autoparte
from Consulta_total import mostrar_autopartes
from validar_stock_minimo import validar_stock_minimo
from logs import *

alta=0
baja=0
modificacion=0
historial_alta=[]
historial_baja=[]
historial_modificacion=[]
motor = [
    ["Motor", 101, "Filtro de aceite", "BGK", "Volkswagen Polo", 6, 71000, 5],
    ["Motor", 102, "Correa de distribucion", "BGK", "Peugeot 208", 7, 40000, 5],
    ["Motor", 103, "Bomba de aceite", "BGK", "Volkswagen Polo", 9, 43000, 5],
    ["Motor", 104, "Junta de culata", "BGK", "Volkswagen Polo", 11, 59000, 5],
    ["Motor", 105, "Piston", "BGK", "Volkswagen Polo", 17, 56000, 5]
]

encendido = [
    ["Encendido", 201, "Bujia", "NGK", "Universal", 19, 18900, 5],
    ["Encendido", 202, "Bobina de encendido", "Bosch", "Universal", 25, 34800, 5],
    ["Encendido", 203, "Cables de bujia", "Bosch", "Universal", 30, 23600, 5],
    ["Encendido", 204, "Distribuidor", "Bosch", "Universal", 13, 23000, 5],
    ["Encendido", 205, "Motor de arranque", "Bosch", "Universal", 9, 32000, 5]
]

refrigeracion = [
    ["Refrigeracion", 301, "Radiador", "Valeo", "Universal", 17, 15900, 5],
    ["Refrigeracion", 302, "Bomba de agua", "SKF", "Universal", 24, 1090, 5],
    ["Refrigeracion", 303, "Termostato", "Gates", "Universal", 70, 9500, 5],
    ["Refrigeracion", 304, "Electroventilador", "Valeo", "Universal", 45, 9200, 5],
    ["Refrigeracion", 305, "Manguera de radiador", "Gates", "Universal", 80, 8900, 5]
]

suspension = [
    ["Suspension", 401, "Amortiguador delantero", "Monroe", "Universal", 22, 4500, 5],
    ["Suspension", 402, "Amortiguador trasero", "Monroe", "Universal", 25, 4800, 5],
    ["Suspension", 403, "Rotula", "TRW", "Universal", 28, 5800, 5],
    ["Suspension", 404, "Bieleta", "TRW", "Universal", 9, 5700, 5],
    ["Suspension", 405, "Bujes de suspension", "TRW", "Universal", 24, 5000, 5]
]
option = "-1"
while option!=0:
    print("⏤"*120)
    print(" "*45,"BIENVENIDO AL SISTEMA DE CONTROL DE STOCK DE AUTOPARTES PARTSCTRL\n")
    print("⏤"*120)
    print(""" \nSeleccione las siguientes opciones para comenzar con la carga del sistema\n
            * Ingrese 1 para registrar nuevas autopartes
            * Ingrese 2 para modificar informacion de autopartes
            * Ingrese 3 para eliminar autopartes
            * Ingrese 4 para mostrar el listado de autopartes
            * Ingrese 5 para consultar autopartes
            * Ingrese 6 para ver movimiento de stock de autopartes
        
            * Para finalizar ingrese 0 por teclado  """)

    option = input("\nIngrese la opcion para continuar: ")

    while option != "0" and option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6":
        print("\n > La opcion ingresada no es correcta")
        option = input("\nIngrese un valor correcto entre las opciones (0 a 6) para continuar: ")

    
    if option == "1":
        m,e,r,s,a= agregar_autoparte(motor,encendido,refrigeracion,suspension)
        alta+=1
        historial_alta.extend(a)


    elif option == "2":
         modi = modificar_autoparte(motor,encendido,refrigeracion,suspension )
         modificacion+=1
         historial_modificacion.append(modi.copy())
    elif option == "3":
        b = eliminar_autoparte(motor,encendido,refrigeracion,suspension)
        baja+=1
        historial_baja.extend(b)
    elif option == "4":
        h=mostrar_autopartes(
        motor,
        encendido,
        refrigeracion,
        suspension
    )
        minimo = validar_stock_minimo(h)
        

    elif option == "5":
        codigo = int(input("Ingrese el codigo de la autoparte: "))

        while codigo < 101 or codigo > 499:
            print("ERROR - Ingrese un codigo correctamente")
            codigo = int(input("Ingrese el codigo nuevamente: "))

        if codigo >= 101 and codigo <= 199:
            encontrada, final = mostrar_info(codigo, motor)

        elif codigo >= 201 and codigo <= 299:
            encontrada, final = mostrar_info(codigo, encendido)

        elif codigo >= 301 and codigo <= 399:
            encontrada, final = mostrar_info(codigo, refrigeracion)

        elif codigo >= 401 and codigo <= 499:
            encontrada, final = mostrar_info(codigo, suspension)

        if encontrada == True:
            print("\nAutoparte encontrada:")
            print(final)

        else:
            print("\nProducto no encontrado")

    elif option == "6":
        if alta>0:
            mostrar_logs_alta(historial_alta)
        else:
            print("No se dieron de alta productos")
        if modificacion>0:
            mostrar_logs_modificacion(historial_modificacion)
        else:
            print('No se registraron modificaciones')
        if baja>0:
            mostrar_logs_baja(historial_baja)
        else:
            print('No se dieron de baja productos')
            
    else:
        print("\n > Gracias por utilizar el sistema de control de stock de autopartes")
