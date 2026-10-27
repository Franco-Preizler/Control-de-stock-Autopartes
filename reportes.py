"""Listados, alertas de stock minimo e historial de movimientos del inventario."""
from functools import reduce


def listar_inventario(inventario):
    print("\n========== INVENTARIO COMPLETO ==========")

    todas = []
    for categoria, productos in inventario.items():
        for producto in productos:
            todas.append([categoria] + producto)
    todas.sort(key=lambda item: item[1])

    for item in todas:
        print(
            "Categoria:", item[0],
            "| Codigo:", item[1],
            "| Autoparte:", item[2],
            "| Marca:", item[3],
            "| Modelo:", item[4],
            "| Stock:", item[5],
            "| Precio:", item[6],
            "| Stock minimo:", item[7]
        )

    valores = map(lambda item: item[5] * item[6], todas)
    valor_total = reduce(lambda acumulado, valor: acumulado + valor, valores, 0)
    print(f"\nValor total del inventario: ${valor_total}")

    return todas


def validar_stock_minimo(inventario):
    bajo_stock = []
    for categoria, productos in inventario.items():
        bajos = filter(lambda producto: producto[4] < producto[6], productos)
        bajo_stock.extend([categoria] + producto for producto in bajos)

    print("\nLos productos con stock debajo del minimo son:")
    if bajo_stock:
        for item in bajo_stock:
            print(
                "Categoria:", item[0],
                "| Codigo:", item[1],
                "| Autoparte:", item[2],
                "| Stock actual:", item[5],
                "| Stock minimo:", item[7]
            )
    else:
        print("No hay productos por debajo del stock minimo.")

    return bajo_stock


def mostrar_logs_alta(alta):
    print("""==================================
                           ALTA
    ==================================""")
    print(alta)
    print()


def mostrar_logs_baja(baja):
    print("""==================================
                      BAJA
        ==================================""")
    print(baja)
    print()


def mostrar_logs_modificacion(modificacion):
    print("""==================================
                        MODIFICACION
    ==================================""")
    print(modificacion)
