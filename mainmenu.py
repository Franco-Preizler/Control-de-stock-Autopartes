from Agregar_stock import agregar_autoparte
from Modificar_stock import modificar_autoparte
from eliminarap import eliminar_autoparte
from Consulta_total import mostrar_autopartes

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

        if option == "0":
            print("\n > Gracias por utilizar el sistema de control de stock de autopartes")
        elif option == "1":
            agregar_autoparte(
            motor,
            encendido,
            refrigeracion,
            suspension
        )

        elif option == "2":
            modificar_autoparte(
            motor,
            encendido,
            refrigeracion,
            suspension
        )
        elif option == "3":
            eliminar_autoparte(
            motor,
            encendido,
            refrigeracion,
            suspension
        )
        elif option == "4":
            mostrar_autopartes(
            motor,
            encendido,
            refrigeracion,
            suspension
        )
        elif option == "5":
            consultar_autoparte()
        elif option == "6":
            movimiento_stock()
        else:
            print("\n > La opcion ingresada no es correcta")
