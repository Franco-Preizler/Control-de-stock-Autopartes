from Validaciones import pedir_entero


def eliminar_autoparte(motor,encendido,refrigeracion,suspension):
    baja = []
    print("⏤"*120)
    print(" "*45,"ELIMINAR AUTOPARTE\n")
    print("⏤"*120)
    print(""" \nSeleccione las siguientes opciones para eliminar una autoparte\n
            * Ingrese 1 para eliminar una autoparte por ID
            * Ingrese 2 para eliminar una autoparte por nombre""")

    opcion = pedir_entero("Ingrese la opcion para continuar: ", 1, 2)
    
    if opcion == 1:
        codigo = pedir_entero("ingrese ID del autoparte a eliminar: ", 100, 499)
        eliminado = False
        
        if 100 <= codigo < 200:
            for i in range(len(motor) - 1, -1, -1):
                if motor[i][1] == codigo:
                    print(motor[i])
                    baja.append(motor[i].copy())
                    del motor[i]
                    eliminado = True
                    break
                    
                    
                    
        elif 200 <= codigo < 300:
            for i in range(len(encendido) - 1, -1, -1):
                if encendido[i][1] == codigo:
                    baja.append(encendido[i].copy())
                    del encendido[i]
                    eliminado = True
                    break
                    
        elif 300 <= codigo < 400:
            for i in range(len(refrigeracion) - 1, -1, -1):
                if refrigeracion[i][1] == codigo:
                    baja.append(refrigeracion[i].copy())
                    del refrigeracion[i]
                    eliminado = True
                    break
                
                    
        elif 400 <= codigo < 500:
            for i in range(len(suspension) - 1, -1, -1):
                if suspension[i][1] == codigo:
                    baja.append(suspension[i].copy())
                    del suspension[i]
                    eliminado = True
                    break
                
                    
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
        categoria = pedir_entero("ingrese la categoria: ", 1, 4)
            
        nombre = input("ingrese nombre de la autoparte: ").lower()
        eliminado = False
        
        if categoria == 1:
            for i in range(len(motor) - 1, -1, -1):
                if motor[i][2].lower() == nombre:
                    baja.append(motor[i].copy())
                    del motor[i]
                    eliminado = True
                    break
                    
        elif categoria == 2:
            for i in range(len(encendido) - 1, -1, -1):
                if encendido[i][2].lower() == nombre:
                    baja.append(encendido[i].copy())
                    del encendido[i]
                    eliminado = True
                    break
                    
        elif categoria == 3:
            for i in range(len(refrigeracion) - 1, -1, -1):
                if refrigeracion[i][2].lower() == nombre:
                    baja.append(refrigeracion[i].copy())
                    del refrigeracion[i]
                    eliminado = True
                    break
                    
        elif categoria == 4:
            for i in range(len(suspension) - 1, -1, -1):
                if suspension[i][2].lower() == nombre:
                    baja.append(suspension[i].copy())
                    del suspension[i]
                    eliminado = True
                    break
                
                    
        if eliminado:
            print("Autoparte eliminada correctamente")
        else:
            print("No se encontro ninguna autoparte con ese nombre.")
            
    return baja

