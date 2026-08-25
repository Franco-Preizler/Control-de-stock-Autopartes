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



       
