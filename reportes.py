"""Listados, alertas de stock minimo, resumen por categoria e historial de movimientos."""
from functools import reduce

from inventario import CAMPOS


def valor_total_inventario(inventario):
    todas = []
    for productos in inventario.values():
        todas.extend(productos)
    valores = map(lambda producto: producto[4] * producto[5], todas)
    return reduce(lambda acumulado, valor: acumulado + valor, valores, 0)


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

    print(f"\nValor total del inventario: ${valor_total_inventario(inventario)}")
    return todas


def mostrar_producto(producto):
    for i in range(len(CAMPOS)):
        print(f"  {CAMPOS[i]}: {producto[i]}")


def productos_bajo_minimo(inventario):
    bajo_stock = []
    for categoria, productos in inventario.items():
        bajos = filter(lambda producto: producto[4] < producto[6], productos)
        for producto in bajos:
            bajo_stock.append([categoria] + producto)
    return bajo_stock


def validar_stock_minimo(inventario):
    bajo_stock = productos_bajo_minimo(inventario)

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


def resumen_por_categoria(inventario):
    """Devuelve un diccionario {categoria: datos}, donde datos es otro diccionario con
    la cantidad de productos, las unidades, el valor y el conjunto de marcas.
    Las marcas se guardan en un set para contar cada una una sola vez."""
    resumen = {}
    for categoria, productos in inventario.items():
        datos = {"productos": len(productos), "unidades": 0, "valor": 0, "marcas": set()}
        for producto in productos:
            datos["unidades"] = datos["unidades"] + producto[4]
            datos["valor"] = datos["valor"] + producto[4] * producto[5]
            datos["marcas"].add(producto[2])
        resumen[categoria] = datos
    return resumen


def mostrar_resumen(resumen):
    print("\n========== RESUMEN POR CATEGORIA ==========")
    for categoria, datos in resumen.items():
        print(f"\n{categoria}")
        print("  Productos distintos:", datos["productos"])
        print("  Unidades en stock:  ", datos["unidades"])
        print(f"  Valor en stock:      ${datos['valor']}")
        if len(datos["marcas"]) > 0:
            print(f"  Marcas ({len(datos['marcas'])}):", ", ".join(sorted(datos["marcas"])))
        else:
            print("  Marcas: no hay productos cargados")


def contar_movimientos(movimientos):
    """Diccionario que cuenta cuantos movimientos hay de cada tipo."""
    conteo = {}
    for movimiento in movimientos:
        tipo = movimiento["tipo"]
        if tipo in conteo:
            conteo[tipo] = conteo[tipo] + 1
        else:
            conteo[tipo] = 1
    return conteo


def mostrar_movimientos(movimientos):
    print("\n========== HISTORIAL DE MOVIMIENTOS ==========")
    if len(movimientos) == 0:
        print("Todavia no se registraron movimientos.")
        return

    for movimiento in movimientos:
        print(
            movimiento["tipo"],
            "| Categoria:", movimiento["categoria"],
            "| Codigo:", movimiento["codigo"],
            "| Autoparte:", movimiento["autoparte"],
            "|", movimiento["detalle"]
        )

    print("\nCantidad de movimientos por tipo:")
    conteo = contar_movimientos(movimientos)
    for tipo, cantidad in conteo.items():
        print(f"  {tipo}: {cantidad}")
