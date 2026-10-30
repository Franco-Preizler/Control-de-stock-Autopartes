"""Programa principal: muestra el menu y coordina las operaciones, los reportes y el guardado."""
from inventario import (
    agregar_autoparte,
    modificar_autoparte,
    eliminar_autoparte,
    actualizar_stock,
    mostrar_info,
    inventario_inicial,
)
from reportes import (
    listar_inventario,
    validar_stock_minimo,
    mostrar_producto,
    resumen_por_categoria,
    mostrar_resumen,
    mostrar_movimientos,
)
from archivos import (
    cargar_inventario,
    guardar_inventario,
    registrar_movimiento,
    leer_movimientos,
)
from Validaciones import pedir_entero

OPCIONES_MENU = ("0", "1", "2", "3", "4", "5", "6", "7", "8")


def mostrar_menu():
    print("⏤" * 120)
    print(" " * 45, "BIENVENIDO AL SISTEMA DE CONTROL DE STOCK DE AUTOPARTES PARTSCTRL\n")
    print("⏤" * 120)
    print(""" \nSeleccione las siguientes opciones para comenzar con la carga del sistema\n
            * Ingrese 1 para registrar nuevas autopartes
            * Ingrese 2 para modificar informacion de autopartes
            * Ingrese 3 para eliminar autopartes
            * Ingrese 4 para mostrar el listado de autopartes
            * Ingrese 5 para consultar autopartes
            * Ingrese 6 para ver movimiento de stock de autopartes
            * Ingrese 7 para registrar entrada o salida de unidades
            * Ingrese 8 para ver el resumen por categoria

            * Para finalizar ingrese 0 por teclado  """)


def iniciar_inventario():
    """Recupera el inventario guardado. Si no hay archivo (o esta danado) usa los datos de ejemplo."""
    inventario = cargar_inventario()
    if inventario is None:
        print("Se carga el inventario inicial de ejemplo.")
        inventario = inventario_inicial()
        guardar_inventario(inventario)
    else:
        print("Inventario recuperado de inventario.json")
    return inventario


def guardar_cambios(inventario, resultado):
    """Si la operacion se realizo, guarda el inventario (JSON) y registra el movimiento (TXT).
    resultado es una tupla (tipo, categoria, producto, detalle) o None si se cancelo."""
    if resultado is None:
        return
    tipo, categoria, producto, detalle = resultado
    guardar_inventario(inventario)
    registrar_movimiento(tipo, categoria, producto, detalle)


def consultar_autoparte(inventario):
    codigo = pedir_entero("Ingrese el codigo de la autoparte: ", 100, 499)
    encontrada, producto = mostrar_info(codigo, inventario)

    if encontrada:
        print("\nAutoparte encontrada:")
        mostrar_producto(producto)
    else:
        print("\nProducto no encontrado")


def main():
    inventario = iniciar_inventario()

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("\nIngrese la opcion para continuar: ").strip()

        while opcion not in OPCIONES_MENU:
            print("\n > La opcion ingresada no es correcta")
            opcion = input("\nIngrese un valor correcto entre las opciones (0 a 8) para continuar: ").strip()

        if opcion == "1":
            guardar_cambios(inventario, agregar_autoparte(inventario))
        elif opcion == "2":
            guardar_cambios(inventario, modificar_autoparte(inventario))
        elif opcion == "3":
            guardar_cambios(inventario, eliminar_autoparte(inventario))
        elif opcion == "4":
            listar_inventario(inventario)
            validar_stock_minimo(inventario)
        elif opcion == "5":
            consultar_autoparte(inventario)
        elif opcion == "6":
            mostrar_movimientos(leer_movimientos())
        elif opcion == "7":
            guardar_cambios(inventario, actualizar_stock(inventario))
        elif opcion == "8":
            mostrar_resumen(resumen_por_categoria(inventario))

    print("\n > Gracias por utilizar el sistema de control de stock de autopartes")


if __name__ == "__main__":
    main()
