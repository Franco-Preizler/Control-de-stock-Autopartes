if opcion_categoria == 4:
    print("\n========== INVENTARIO COMPLETO ==========")

    for autoparte in matriz:
        print(
            "Código:", autoparte[0],
            "| Autoparte:", autoparte[1],
            "| Marca:", autoparte[2]
            "| Modelo:", autoparte[3]
            "| Precio:", autoparte[4]
            "| Stock:", autoparte[5]
            "| stockMin:", autoparte[6]
            )
