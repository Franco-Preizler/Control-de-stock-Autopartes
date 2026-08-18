def validarNum(opcion):
    while opcion<1 or opcion>4:
        print("ERROR - SELECCIONE UNA OPCION VÁLIDA DEL 1 AL 4")
        opcion = int(input("Ingrese una opción: "))
    return opcion