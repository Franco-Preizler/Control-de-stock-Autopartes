def eliminar_autoparte(motor,encendido,refrigeracion,suspension):
    baja = []
    print("⏤"*120)
    print(" "*45,"ELIMINAR AUTOPARTE\n")
    print("⏤"*120)
    print(""" \nSeleccione las siguientes opciones para eliminar una autoparte\n
            * Ingrese 1 para eliminar una autoparte por ID
            * Ingrese 2 para eliminar una autoparte por nombre""")

    opcion = int(input("Ingrese la opcion para continuar: "))
    while opcion != 1 and opcion != 2:
        print("\n > La opcion ingresada no es correcta")
        opcion = int(input("\nIngrese un valor correcto entre las opciones (1 a 2) para continuar: "))
    
    if opcion == 1:
        codigo = int(input("ingrese ID del autoparte a eliminar: "))
        eliminado = False
        
        if 200 > codigo > 100:
            for i in range(len(motor) - 1, -1, -1):
                if motor[i][1] == codigo:
                    print(motor[i])
                    baja.append(motor[i].copy())
                    del motor[i]
                    eliminado = True
                    
                    
                    
        elif 300 > codigo > 200:
            for i in range(len(encendido) - 1, -1, -1):
                if encendido[i][1] == codigo:
                    baja.append(encendido[i].copy())
                    del encendido[i]
                    eliminado = True
                    
        elif 400 > codigo > 300:
            for i in range(len(refrigeracion) - 1, -1, -1):
                if refrigeracion[i][1] == codigo:
                    baja.append(refrigeracion[i].copy())
                    del refrigeracion[i]
                    eliminado = True
                
                    
        elif 500 > codigo > 400:
            for i in range(len(suspension) - 1, -1, -1):
                if suspension[i][1] == codigo:
                    baja.append(suspension[i].copy())
                    del suspension[i]
                    eliminado = True
                
                    
        if eliminado:
            print("Autoparte eliminada correctamente")
        else:
            print("No se encontro ninguna autoparte con ese ID.")

    elif opcion == 2:
        print("""CATEGORIAS DE PRODUCTOS
* 1. Motor
* 2. Encendido
* 3. Refrigeracion
* 4. Suspension""")
        categoria = int(input("ingrese la categoria: "))
        while categoria < 1 or categoria > 4:
            print("Error - opcion invalida. Ingrese una opcion entre el 1 y el 4")
            categoria = int(input("ingrese la categoria: "))
            
        nombre = input("ingrese nombre de la autoparte: ").lower()
        eliminado = False
        
        if categoria == 1:
            for i in range(len(motor) - 1, -1, -1):
                if motor[i][2].lower() == nombre:
                    baja.append(motor[i].copy())
                    del motor[i]
                    eliminado = True
                    
        elif categoria == 2:
            for i in range(len(encendido) - 1, -1, -1):
                if encendido[i][2].lower() == nombre:
                    baja.append(encendido[i].copy())
                    del encendido[i]
                    eliminado = True
                    
        elif categoria == 3:
            for i in range(len(refrigeracion) - 1, -1, -1):
                if refrigeracion[i][2].lower() == nombre:
                    baja.append(refrigeracion[i].copy())
                    del refrigeracion[i]
                    eliminado = True
                    
        elif categoria == 4:
            for i in range(len(suspension) - 1, -1, -1):
                if suspension[i][2].lower() == nombre:
                    baja.append(suspension[i].copy())
                    del suspension[i]
                    eliminado = True
                
                    
        if eliminado:
            print("Autoparte eliminada correctamente")
        else:
            print("No se encontro ninguna autoparte con ese nombre.")
            
    return baja

