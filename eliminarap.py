def eliminar_autoparte(motor, encendido, refrigeracion, suspension):
    print("⏤" * 120)
    print(" " * 45, "ELIMINAR AUTOPARTE\n")
    print("⏤" * 120)
    print("""
Seleccione las siguientes opciones para eliminar una autoparte

    * Ingrese 1 para eliminar una autoparte por ID
    * Ingrese 2 para eliminar una autoparte por nombre
""")

    opcion = int(input("Ingrese la opcion para continuar: "))
    while opcion != 1 and opcion != 2:
        print("\n > La opcion ingresada no es correcta")
        opcion = int(input("\nIngrese un valor correcto entre las opciones (1 a 2) para continuar: "))

    if opcion == 1:
        codigo = int(input("ingrese ID del autoparte a eliminar: "))
        matrices = [motor, encendido, refrigeracion, suspension]

        for matriz in matrices:
            for i in range(len(matriz) - 1, -1, -1):
                if matriz[i][1] == codigo:
                    eliminado = matriz[i].copy()
                    del matriz[i]
                    print("Autoparte eliminada correctamente")
                    return True, eliminado

        print("No se encontró ninguna autoparte con ese ID.")

    else:
        print("""CATEGORIAS DE PRODUCTOS
* 1. Motor
* 2. Encendido
* 3. Refrigeracion
* 4. Suspension""")

        categoria = int(input("ingrese la categoria: "))
        while categoria < 1 or categoria > 4:
            print("Error - opcion inválida. Ingrese una opcion entre el 1 y el 4")
            categoria = int(input("ingrese la categoria: "))

        nombre = input("ingrese nombre de la autoparte: ").lower()
        matrices = [motor, encendido, refrigeracion, suspension]
        matriz = matrices[categoria - 1]

        for i in range(len(matriz) - 1, -1, -1):
            if matriz[i][2].lower() == nombre:
                eliminado = matriz[i].copy()
                del matriz[i]
                print("Autoparte eliminada correctamente")
                return True, eliminado

        print("No se encontró ninguna autoparte con ese nombre.")

    return False, []
