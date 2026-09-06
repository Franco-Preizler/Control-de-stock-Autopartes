from Agregar_stock import agregar_autoparte
from Modificar_stock import modificar_autoparte
from eliminarap import eliminar_autoparte
from Consulta_total import mostrar_autopartes
from Consulta_unidad import mostrar_info
from validar_stock_minimo import validar_stock_minimo
from registro_movimientos import registrar_movimiento, mostrar_movimientos


motor = [
    ["Motor", 101, "Filtro de aceite", "BGK", "Volkswagen Polo", 6, 71000, 5],
    ["Motor", 102, "Correa de distribución", "BGK", "Peugeot 208", 7, 40000, 5],
    ["Motor", 103, "Bomba de aceite", "BGK", "Volkswagen Polo", 9, 43000, 5],
    ["Motor", 104, "Junta de culata", "BGK", "Volkswagen Polo", 11, 59000, 5],
    ["Motor", 105, "Pistón", "BGK", "Volkswagen Polo", 17, 56000, 5]
]

encendido = [
    ["Encendido", 201, "Bujía", "NGK", "Universal", 19, 18900, 5],
    ["Encendido", 202, "Bobina de encendido", "Bosch", "Universal", 25, 34800, 5],
    ["Encendido", 203, "Cables de bujía", "Bosch", "Universal", 30, 23600, 5],
    ["Encendido", 204, "Distribuidor", "Bosch", "Universal", 13, 23000, 5],
    ["Encendido", 205, "Motor de arranque", "Bosch", "Universal", 9, 32000, 5]
]

refrigeracion = [
    ["Refrigeración", 301, "Radiador", "Valeo", "Universal", 17, 15900, 5],
    ["Refrigeración", 302, "Bomba de agua", "SKF", "Universal", 24, 1090, 5],
    ["Refrigeración", 303, "Termostato", "Gates", "Universal", 70, 9500, 5],
    ["Refrigeración", 304, "Electroventilador", "Valeo", "Universal", 45, 9200, 5],
    ["Refrigeración", 305, "Manguera de radiador", "Gates", "Universal", 80, 8900, 5]
]

suspension = [
    ["Suspensión", 401, "Amortiguador delantero", "Monroe", "Universal", 22, 4500, 5],
    ["Suspensión", 402, "Amortiguador trasero", "Monroe", "Universal", 25, 4800, 5],
    ["Suspensión", 403, "Rótula", "TRW", "Universal", 28, 5800, 5],
    ["Suspensión", 404, "Bieleta", "TRW", "Universal", 9, 5700, 5],
    ["Suspensión", 405, "Bujes de suspensión", "TRW", "Universal", 24, 5000, 5]
]


def consultar_autoparte():
    try:
        codigo = int(input("Ingrese el código de la autoparte: "))
    except ValueError:
        print("ERROR - El código debe ser numérico.")
        return

    while codigo < 101 or codigo > 499:
        print("ERROR - Ingrese un código entre 101 y 499.")
        try:
            codigo = int(input("Ingrese el código nuevamente: "))
        except ValueError:
            codigo = 0

    if 101 <= codigo <= 199:
        encontrada, final = mostrar_info(codigo, motor)
    elif 201 <= codigo <= 299:
        encontrada, final = mostrar_info(codigo, encendido)
    elif 301 <= codigo <= 399:
        encontrada, final = mostrar_info(codigo, refrigeracion)
    else:
        encontrada, final = mostrar_info(codigo, suspension)

    if encontrada:
        print("\nAutoparte encontrada:")
        print(final)
    else:
        print("\nProducto no encontrado.")


def main():
    # Este historial existe solamente mientras el programa está ejecutándose.
    movimientos = []

    while True:
        print("\n" + "═" * 100)
        print(" " * 30 + "PARTSCTRL")
        print(" " * 20 + "SISTEMA DE CONTROL DE STOCK DE AUTOPARTES")
        print("═" * 100)
        print("""
1. Registrar nuevas autopartes
2. Modificar información de autopartes
3. Eliminar autopartes
4. Mostrar listado de autopartes y verificar stock mínimo
5. Consultar una autoparte por código
6. Consultar historial de movimientos
0. Finalizar
""")

        option = input("Ingrese la opción para continuar: ").strip()

        while option not in ("0", "1", "2", "3", "4", "5", "6"):
            print("\n> La opción ingresada no es correcta.")
            option = input("Ingrese una opción entre 0 y 6: ").strip()

        if option == "1":
            resultado = agregar_autoparte(
                motor, encendido, refrigeracion, suspension
            )

            codigo, autoparte, marca, modelo, stock, precio, stock_minimo = resultado
            registrar_movimiento(
                movimientos,
                "ALTA",
                f"Se agregó la autoparte '{autoparte}' con código {codigo}, "
                f"marca '{marca}', modelo '{modelo}', stock {stock} y precio {precio}."
            )

        elif option == "2":
            exito, codigo, anterior, nuevo = modificar_autoparte(
                motor, encendido, refrigeracion, suspension
            )

            if exito:
                registrar_movimiento(
                    movimientos,
                    "MODIFICACIÓN",
                    f"Se modificó la autoparte con código {codigo}. "
                    f"Valores anteriores: {anterior}. Nuevos valores: {nuevo}."
                )

        elif option == "3":
            exito, eliminado = eliminar_autoparte(
                motor, encendido, refrigeracion, suspension
            )

            if exito:
                registrar_movimiento(
                    movimientos,
                    "BAJA",
                    f"Se eliminó la autoparte '{eliminado[2]}' con código {eliminado[1]}."
                )

        elif option == "4":
            matrices = mostrar_autopartes(
                motor, encendido, refrigeracion, suspension
            )
            validar_stock_minimo(matrices)

        elif option == "5":
            consultar_autoparte()

        elif option == "6":
            mostrar_movimientos(movimientos)

        elif option == "0":
            print("\n> Gracias por utilizar PARTSCTRL.")
            break


if __name__ == "__main__":
    main()
