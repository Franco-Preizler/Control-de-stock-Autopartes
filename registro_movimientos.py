def registrar_movimiento(movimientos, tipo, detalle):
    movimientos.append({
        "tipo": tipo,
        "detalle": detalle
    })


def mostrar_movimientos(movimientos):
    print("\n" + "=" * 100)
    print("HISTORIAL DE MOVIMIENTOS")
    print("=" * 100)

    if len(movimientos) == 0:
        print("No se han realizado movimientos durante esta ejecución.")
    else:
        for i, movimiento in enumerate(movimientos, 1):
            print(f"{i}. [{movimiento['tipo']}] {movimiento['detalle']}")
