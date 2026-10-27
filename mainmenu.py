from inventario import (
    agregar_autoparte,
    modificar_autoparte,
    eliminar_autoparte,
    mostrar_info,
    inventario_vacio,
)
from reportes import (
    listar_inventario,
    validar_stock_minimo,
    mostrar_logs_alta,
    mostrar_logs_baja,
    mostrar_logs_modificacion,
)
from Validaciones import pedir_entero

alta = 0
baja = 0
modificacion = 0
historial_alta = []
historial_baja = []
historial_modificacion = []

inventario = inventario_vacio()
inventario["Motor"] = [
    [101, "Filtro de aceite", "BGK", "Volkswagen Polo", 6, 71000, 5],
    [102, "Correa de distribucion", "BGK", "Peugeot 208", 7, 40000, 5],
    [103, "Bomba de aceite", "BGK", "Volkswagen Polo", 9, 43000, 5],
    [104, "Junta de culata", "BGK", "Volkswagen Polo", 11, 59000, 5],
    [105, "Piston", "BGK", "Volkswagen Polo", 17, 56000, 5],
]
inventario["Encendido"] = [
    [201, "Bujia", "NGK", "Universal", 19, 18900, 5],
    [202, "Bobina de encendido", "Bosch", "Universal", 25, 34800, 5],
    [203, "Cables de bujia", "Bosch", "Universal", 30, 23600, 5],
    [204, "Distribuidor", "Bosch", "Universal", 13, 23000, 5],
    [205, "Motor de arranque", "Bosch", "Universal", 9, 32000, 5],
]
inventario["Refrigeracion"] = [
    [301, "Radiador", "Valeo", "Universal", 17, 15900, 5],
    [302, "Bomba de agua", "SKF", "Universal", 24, 1090, 5],
    [303, "Termostato", "Gates", "Universal", 70, 9500, 5],
    [304, "Electroventilador", "Valeo", "Universal", 45, 9200, 5],
    [305, "Manguera de radiador", "Gates", "Universal", 80, 8900, 5],
]
inventario["Suspension"] = [
    [401, "Amortiguador delantero", "Monroe", "Universal", 22, 4500, 5],
    [402, "Amortiguador trasero", "Monroe", "Universal", 25, 4800, 5],
    [403, "Rotula", "TRW", "Universal", 28, 5800, 5],
    [404, "Bieleta", "TRW", "Universal", 9, 5700, 5],
    [405, "Bujes de suspension", "TRW", "Universal", 24, 5000, 5],
]

option = -1
while option != 0:
    print("⏤" * 120)
    print(" " * 45, "BIENVENIDO AL SISTEMA DE CONTROL DE STOCK DE AUTOPARTES PARTSCTRL\n")
    print("⏤" * 120)
    print(""" \nSeleccione las siguientes opciones para comenzar con la carga del sistema\n
            * Ingrese 1 para registrar nuevas autopartes
            * Ingrese 2 para modificar informacion de autopartes
            * Ingrese 3 para eliminar autopartes
            * Ingrese 4 para mostrar el listado de autopartes
            * Ingrese 5 para consultar autopartes
            * Ingrese 6 para ver movimiento de stock de autopartes

            * Para finalizar ingrese 0 por teclado  """)

    option = input("\nIngrese la opcion para continuar: ")

    while option not in ("0", "1", "2", "3", "4", "5", "6"):
        print("\n > La opcion ingresada no es correcta")
        option = input("\nIngrese un valor correcto entre las opciones (0 a 6) para continuar: ")

    if option == "1":
        a = agregar_autoparte(inventario)
        if a:
            alta += 1
            historial_alta.append(a)

    elif option == "2":
        modi = modificar_autoparte(inventario)
        if modi:
            modificacion += 1
            historial_modificacion.append(modi)

    elif option == "3":
        b = eliminar_autoparte(inventario)
        if b:
            baja += 1
            historial_baja.extend(b)

    elif option == "4":
        listar_inventario(inventario)
        validar_stock_minimo(inventario)

    elif option == "5":
        codigo = pedir_entero("Ingrese el codigo de la autoparte: ", 100, 499)
        encontrada, final = mostrar_info(codigo, inventario)

        if encontrada:
            print("\nAutoparte encontrada:")
            print(final)
        else:
            print("\nProducto no encontrado")

    elif option == "6":
        if alta > 0:
            mostrar_logs_alta(historial_alta)
        else:
            print("No se dieron de alta productos")
        if modificacion > 0:
            mostrar_logs_modificacion(historial_modificacion)
        else:
            print('No se registraron modificaciones')
        if baja > 0:
            mostrar_logs_baja(historial_baja)
        else:
            print('No se dieron de baja productos')

    else:
        print("\n > Gracias por utilizar el sistema de control de stock de autopartes")
        option = 0

