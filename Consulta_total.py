from functools import reduce


def mostrar_autopartes(motor, encendido, refrigeracion, suspension):
    print("\n========== INVENTARIO COMPLETO ==========")
    matrices = [motor, encendido, refrigeracion, suspension]

    todas = []
    for matriz in matrices:
        todas.extend(matriz)
    todas.sort(key=lambda autoparte: autoparte[1])

    for autoparte in todas:
        print(
            "Categoria:", autoparte[0],
            "| Codigo:", autoparte[1],
            "| Autoparte:", autoparte[2],
            "| Marca:", autoparte[3],
            "| Modelo:", autoparte[4],
            "| Stock:", autoparte[5],
            "| Precio:", autoparte[6],
            "| Stock minimo:", autoparte[7]
        )

    valores = map(lambda autoparte: autoparte[5] * autoparte[6], todas)
    valor_total = reduce(lambda acumulado, valor: acumulado + valor, valores, 0)
    print(f"\nValor total del inventario: ${valor_total}")

    return matrices