def mostrar_info(cod,mat):
    for fila in mat:
        if fila[1]==cod:
            print(fila)
            return fila
    

def modificar_info(modi):
    print("1.Producto, 2.Precio, 3.Stock, 4.Precio, 5.Stock Minimo")
    modificar=int(input("Ingrese numero para modificar: "))
    if modificar==1:
        modificado=input("Ingrese informacion nueva: ")
        modi[2]=modificado

opcion_gestion=2
motor = [["Motor", 101,"Filtro de aceite", 0],
        ["Motor", 102 ,"Correa de distribución", 0],
        ["Motor", 103 ,"Bomba de aceite", 0],
        ["Motor", 104,"Junta de culata", 0],
        ["Motor", 105,"Pistón", 0]]

encendido = [["Encendido", 201,"Bujía", 0],
    ["Encendido", 202,"Bobina de encendido", 0],
    ["Encendido", 203, "Cables de bujía", 0],
    ["Encendido", 204, "Distribuidor", 0],
    ["Encendido", 205, "Motor de arranque", 0]]

refrigeracion = [["Refrigeración", 301, "Radiador", 0],
        ["Refrigeración", 302,  "Bomba de agua", 0],
        ["Refrigeración", 303, "Termostato", 0],
        ["Refrigeración", 304, "Electroventilador", 0],
        ["Refrigeración", 305, "Manguera de radiador", 0]]

suspension = [["Suspensión", 401, "Amortiguador delantero", 0],
        ["Suspensión", 402, "Amortiguador trasero", 0],
        ["Suspensión", 403, "Rótula", 0],
        ["Suspensión", 404, "Bieleta", 0],
        ["Suspensión", 405, "Bujes de suspensión", 0]]
if opcion_gestion == 2:
    codigo=int(input("Ingresar codigo de producto: "))
    while codigo<100 or codigo >500:
        print("ERROR - Ingresar codigo correctamente")
        codigo=int(input("Ingresar codigo de producto CORRECTAMENTE: "))

    if codigo > 100 and codigo < 200:
        final=mostrar_info(codigo,motor)
        modificar_info(final)
        print("Dato modificado")
        print(final)
        
    elif codigo >200 and codigo <300:
        final=mostrar_info(codigo,encendido)
        modificar_info(final)
        print("Dato modificado")
        print(final)

    elif codigo >300 and codigo < 400:
        final=mostrar_info(codigo,refrigeracion)
        modificar_info(final)
        print("Dato modificado")
        print(final)
    else:
        final=mostrar_info(codigo,suspension)
        modificar_info(final)
        print("Dato modificado")
        print(final)



       