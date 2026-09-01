def mostrar_autopartes(motor, encendido, refrigeracion, suspension):
    print("\n========== INVENTARIO COMPLETO ==========")
    matrices = [motor, encendido, refrigeracion, suspension]

    for matriz in matrices:
        for autoparte in matriz:
            print(
                "Categoría:", autoparte[0],
                "| Código:", autoparte[1],
                "| Autoparte:", autoparte[2],
                "| Marca:", autoparte[3],
                "| Modelo:", autoparte[4],
                "| Stock:", autoparte[5],
                "| Precio:", autoparte[6],
                "| Stock mínimo:", autoparte[7]
            )
            
    return matrices