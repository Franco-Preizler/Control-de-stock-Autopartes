def busquedaProducto(matriz):
    "Elija si desea buscar por nombre o codigo de producto"
    eleccion = int(input("Ingrese 1 para buscar por nombre o 2 para buscar por código: "))
    while eleccion <1 or eleccion>2:
        print("ERROR - SELECCIONE UNA OPCION VÁLIDA DEL 1 AL 2")
        eleccion = int(input("Ingrese una opción: "))

    if eleccion == 1:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        for fila in matriz:
            if fila[1] == nombre:
                print("El producto se encuentra en stock, con un total de: ", fila[4], "unidades")
    else:
        codigo = input("Ingrese el código del producto a buscar: ")
        for fila in matriz:
            if fila[0] == codigo:
                print("El producto se encuentra en stock, con un total de: ", fila[4], "unidades")
                
    