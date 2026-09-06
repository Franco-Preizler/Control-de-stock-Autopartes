# ==========================================
# MATRIZ DE AUTOPARTES
# [Categoría, Nombre, Stock]
# ==========================================

autopartes = [
    ["Motor", "Filtro de aceite", 0],
    ["Motor", "Correa de distribución", 0],
    ["Motor", "Bomba de aceite", 0],
    ["Motor", "Junta de culata", 0],
    ["Motor", "Pistón", 0],

    ["Encendido", "Bujía", 0],
    ["Encendido", "Bobina de encendido", 0],
    ["Encendido", "Cables de bujía", 0],
    ["Encendido", "Distribuidor", 0],
    ["Encendido", "Motor de arranque", 0],

    ["Refrigeración", "Radiador", 0],
    ["Refrigeración", "Bomba de agua", 0],
    ["Refrigeración", "Termostato", 0],
    ["Refrigeración", "Electroventilador", 0],
    ["Refrigeración", "Manguera de radiador", 0],

    ["Suspensión", "Amortiguador delantero", 0],
    ["Suspensión", "Amortiguador trasero", 0],
    ["Suspensión", "Rótula", 0],
    ["Suspensión", "Bieleta", 0],
    ["Suspensión", "Bujes de suspensión", 0]
]


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

opcion_categoria = -1

while opcion_categoria != 0:

    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Motor")
    print("2. Encendido")
    print("3. Refrigeración")
    print("4. Suspensión")
    print("5. Mostrar todo el inventario")
    print("0. Salir")

    opcion_categoria = int(input("Seleccione una opción: "))


    # ==========================================
    # MOSTRAR TODO EL INVENTARIO
    # ==========================================

    if opcion_categoria == 5:

        print("\n========== INVENTARIO COMPLETO ==========")

        for autoparte in autopartes:

            print(
                "Categoría:", autoparte[0],
                "| Autoparte:", autoparte[1],
                "| Stock:", autoparte[2]
            )

        # Esperamos que el usuario presione ENTER
        # antes de volver al menú principal

        input("\nPresione ENTER para volver al menú...")


    # ==========================================
    # DETERMINAR CATEGORÍA
    # ==========================================

    if opcion_categoria == 1:
        categoria = "Motor"

    elif opcion_categoria == 2:
        categoria = "Encendido"

    elif opcion_categoria == 3:
        categoria = "Refrigeración"

    elif opcion_categoria == 4:
        categoria = "Suspensión"


    # ==========================================
    # MENÚ DE AUTOPARTES
    # ==========================================

    if opcion_categoria >= 1 and opcion_categoria <= 4:

        # Lista que contiene solamente las
        # autopartes de la categoría seleccionada

        seleccionadas = []

        for autoparte in autopartes:

            if autoparte[0] == categoria:
                seleccionadas.append(autoparte)


        # Control del menú de autopartes

        opcion_autoparte = -1

        while opcion_autoparte != 0:

            print(f"\n========== {categoria.upper()} ==========")

            # Mostramos las autopartes y su stock actual

            for i in range(len(seleccionadas)):

                print(
                    i + 1,
                    "-",
                    seleccionadas[i][1],
                    "| Stock:",
                    seleccionadas[i][2]
                )

            print("0. Volver a categorías")


            # Pedimos al usuario que seleccione
            # una autoparte

            opcion_autoparte = int(
                input("\nSeleccione una autoparte: ")
            )


            # ==========================================
            # SELECCIONAR AUTOPARTE
            # ==========================================

            if opcion_autoparte >= 1 and opcion_autoparte <= len(seleccionadas):

                autoparte_elegida = seleccionadas[
                    opcion_autoparte - 1
                ]


                print(
                    f"\nAutoparte seleccionada: "
                    f"{autoparte_elegida[1]}"
                )

                print(
                    f"Stock actual: "
                    f"{autoparte_elegida[2]}"
                )


                # ==========================================
                # AGREGAR STOCK
                # ==========================================

                stock = int(
                    input("Ingrese cantidad a agregar: ")
                )


                # Actualizamos directamente el stock
                # dentro de la matriz

                autoparte_elegida[2] += stock


                print(
                    f"\nStock actualizado: "
                    f"{autoparte_elegida[2]}"
                )