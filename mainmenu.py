from Agregar_stock import agregar_autoparte
from Modificar_stock import modificar_autoparte
from eliminarap import eliminar_autoparte
from Consulta_total import mostrar_autopartes

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
            agregar_autoparte()
        elif option == "2":
            modificar_autoparte()
        elif option == "3":
            eliminar_autoparte()
        elif option == "4":
            mostrar_autopartes()
        elif option == "5":
            consultar_autoparte()
        elif option == "6":
            movimiento_stock()
        else:
            print("\n > La opcion ingresada no es correcta")
