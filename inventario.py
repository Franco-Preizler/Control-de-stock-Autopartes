"""Altas, bajas, modificaciones y consultas puntuales sobre el inventario.

El inventario se representa como un diccionario: cada categoria (Motor,
Encendido, Refrigeracion, Suspension) es una clave, y su valor es la lista
de autopartes de esa categoria. Cada autoparte es una lista:
[codigo, nombre, marca, modelo, stock, precio, stock_minimo].

Antes, estos datos se manejaban como 4 listas sueltas (motor, encendido,
refrigeracion, suspension) que había que pasar como 4 parametros separados
a cada funcion del sistema. Usar un unico diccionario evita esa dependencia
de estructuras compartidas y reduce la repeticion de codigo por categoria.
"""
import random

from Validaciones import pedir_entero, pedir_decimal, pedir_texto

CATEGORIAS = {
    "Motor": (100, 199),
    "Encendido": (200, 299),
    "Refrigeracion": (300, 399),
    "Suspension": (400, 499),
}


def inventario_vacio():
    return {categoria: [] for categoria in CATEGORIAS}


def categoria_de_codigo(codigo):
    for categoria, (minimo, maximo) in CATEGORIAS.items():
        if minimo <= codigo <= maximo:
            return categoria
    return None


def codigos_usados(categoria, inventario):
    # Conjunto: solo interesa saber que codigos ya existen, sin duplicados ni orden.
    return {producto[0] for producto in inventario[categoria]}


def generar_codigo(categoria, inventario):
    minimo, maximo = CATEGORIAS[categoria]
    usados = codigos_usados(categoria, inventario)
    if len(usados) > (maximo - minimo):
        return None

    codigo = random.randint(minimo, maximo)
    while codigo in usados:
        codigo = random.randint(minimo, maximo)
    return codigo


def datos(categoria, inventario):
    codigo = generar_codigo(categoria, inventario)
    if codigo is None:
        return None

    nombre = pedir_texto("Ingrese la autoparte que quiere agregar: ", 4, mensaje_error="autoparte invalida")
    marca = pedir_texto("Ingrese la marca de la autoparte: ", 3, r'\d', "marca invalida")
    modelo = pedir_texto("Ingrese el modelo al que pertenece la autoparte: ", 3, mensaje_error="modelo invalido")
    precio = pedir_decimal("Ingrese el precio de la autoparte: ", 0)
    stock = pedir_entero("Ingrese el stock existente: ", 0)
    stock_minimo = pedir_entero(
        f"Indique el stock minimo del producto (menor o igual a {stock}): ", 0, stock
    )
    return [codigo, nombre, marca, modelo, stock, precio, stock_minimo]


def agregar_autoparte(inventario):
    opciones = "/".join(CATEGORIAS)
    categoria = input(f"Ingrese la categoria de producto que quiere agregar ({opciones}): ").title()
    while categoria not in CATEGORIAS:
        print("Categoria no valida.")
        categoria = input(f"Ingrese la categoria de producto que quiere agregar ({opciones}): ").title()

    producto = datos(categoria, inventario)
    if producto is None:
        print("ERROR: No hay codigos disponibles en esa categoria")
        return []

    inventario[categoria].append(producto)
    return [categoria] + producto


def mostrar_info(codigo, inventario):
    categoria = categoria_de_codigo(codigo)
    if categoria is None:
        return False, []

    for producto in inventario[categoria]:
        if producto[0] == codigo:
            return True, producto
    return False, []


def modificar_info(producto):
    print("1.Producto, 2.Marca, 3.Modelo, 4.Stock, 5.Precio, 6.Stock Minimo")
    campo = pedir_entero("Ingrese numero para modificar: ", 1, 6)

    if campo == 1:
        producto[1] = pedir_texto("Ingrese Producto modificado: ", 4, r'[^a-zA-Z0-9 ]', "Producto invalido")
    elif campo == 2:
        producto[2] = pedir_texto("Ingrese Marca modificada: ", 3, r'\d', "Marca invalida")
    elif campo == 3:
        producto[3] = pedir_texto("Ingrese Modelo modificado: ", 3, mensaje_error="Modelo invalido")
    elif campo == 4:
        producto[4] = pedir_entero("Ingrese Stock modificado: ", 0)
    elif campo == 5:
        producto[5] = pedir_decimal("Ingrese Precio modificado: ", 0)
    else:
        producto[6] = pedir_entero("Ingrese Stock minimo modificado: ", 0, producto[4])


def modificar_autoparte(inventario):
    codigo = pedir_entero("Ingresar codigo de producto: ", 100, 499)
    categoria = categoria_de_codigo(codigo)
    encontrada, producto = mostrar_info(codigo, inventario)

    if not encontrada:
        print("Producto no encontrado")
        return []

    antes = producto.copy()
    modificar_info(producto)
    print("Dato modificado")
    print("Antes:", antes)
    print("Despues:", producto)
    return [categoria] + producto


def eliminar_autoparte(inventario):
    baja = []
    print("⏤" * 120)
    print(" " * 45, "ELIMINAR AUTOPARTE\n")
    print("⏤" * 120)
    print(""" \nSeleccione las siguientes opciones para eliminar una autoparte\n
            * Ingrese 1 para eliminar una autoparte por ID
            * Ingrese 2 para eliminar una autoparte por nombre""")

    opcion = pedir_entero("Ingrese la opcion para continuar: ", 1, 2)

    if opcion == 1:
        codigo = pedir_entero("ingrese ID del autoparte a eliminar: ", 100, 499)
        categoria = categoria_de_codigo(codigo)
        eliminado = False

        if categoria:
            for i in range(len(inventario[categoria]) - 1, -1, -1):
                if inventario[categoria][i][0] == codigo:
                    baja.append([categoria] + inventario[categoria][i].copy())
                    del inventario[categoria][i]
                    eliminado = True
                    break

        print("Autoparte eliminada correctamente" if eliminado else "No se encontro ninguna autoparte con ese ID.")

    elif opcion == 2:
        listado = "\n".join(f"* {i}. {categoria}" for i, categoria in enumerate(CATEGORIAS, start=1))
        print(f"CATEGORIAS DE PRODUCTOS\n{listado}")
        indice = pedir_entero("ingrese la categoria: ", 1, len(CATEGORIAS))
        categoria = list(CATEGORIAS)[indice - 1]

        nombre = input("ingrese nombre de la autoparte: ").lower()
        codigo = pedir_entero("Ingrese el codigo de la autoparte a eliminar: ", 100, 499)
        eliminado = False

        for i in range(len(inventario[categoria]) - 1, -1, -1):
            producto = inventario[categoria][i]
            if producto[0] == codigo and producto[1].lower() == nombre:
                baja.append([categoria] + producto.copy())
                del inventario[categoria][i]
                eliminado = True
                break

        print("Autoparte eliminada correctamente" if eliminado else "No se encontro ninguna autoparte con ese nombre.")

    return baja
