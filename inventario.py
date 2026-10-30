"""Operaciones sobre el inventario: alta, baja, modificacion, busqueda y movimientos de stock."""
import random

from Validaciones import (
    pedir_entero,
    pedir_decimal,
    pedir_texto,
    pedir_nombre,
    pedir_marca,
    pedir_modelo,
)

# Diccionario: asocia cada categoria con su rango de codigos.
# El rango es una tupla (minimo, maximo) porque es fijo y no debe cambiar durante la ejecucion.
CATEGORIAS = {
    "Motor": (100, 199),
    "Encendido": (200, 299),
    "Refrigeracion": (300, 399),
    "Suspension": (400, 499),
}

# Tupla con el nombre de cada posicion de una autoparte: producto[i] corresponde a CAMPOS[i].
CAMPOS = ("Codigo", "Producto", "Marca", "Modelo", "Stock", "Precio", "Stock minimo")

# Tupla con los tipos de movimiento de unidades (son opciones fijas).
TIPOS_MOVIMIENTO = ("ENTRADA", "SALIDA")


def inventario_vacio():
    return {categoria: [] for categoria in CATEGORIAS}


def inventario_inicial():
    """Datos de ejemplo. Solo se usan si no existe inventario.json o si esta danado."""
    inventario = inventario_vacio()
    inventario["Motor"] = [
        [101, "Filtro de aceite", "BGK", "Volkswagen Polo", 6, 71000, 5],
        [102, "Correa de distribucion", "BGK", "Peugeot 208", 7, 40000, 5],
        [103, "Bomba de aceite", "BGK", "Volkswagen Polo", 9, 43000, 5],
        [104, "Junta de culata", "BGK", "Volkswagen Polo", 11, 59000, 5],
        [105, "Piston", "BGK", "Volkswagen Polo", 17, 56000, 5],
    ]
    inventario["Encendido"] = [
        [201, "Bujia", "NGK", "Universal", 19, 18900, 5],
        [202, "Bobina de encendido", "Bosch", "Universal", 25, 34800, 5],
        [203, "Cables de bujia", "Bosch", "Universal", 30, 23600, 5],
        [204, "Distribuidor", "Bosch", "Universal", 13, 23000, 5],
        [205, "Motor de arranque", "Bosch", "Universal", 9, 32000, 5],
    ]
    inventario["Refrigeracion"] = [
        [301, "Radiador", "Valeo", "Universal", 17, 15900, 5],
        [302, "Bomba de agua", "SKF", "Universal", 24, 1090, 5],
        [303, "Termostato", "Gates", "Universal", 70, 9500, 5],
        [304, "Electroventilador", "Valeo", "Universal", 45, 9200, 5],
        [305, "Manguera de radiador", "Gates", "Universal", 80, 8900, 5],
    ]
    inventario["Suspension"] = [
        [401, "Amortiguador delantero", "Monroe", "Universal", 22, 4500, 5],
        [402, "Amortiguador trasero", "Monroe", "Universal", 25, 4800, 5],
        [403, "Rotula", "TRW", "Universal", 28, 5800, 5],
        [404, "Bieleta", "TRW", "Universal", 9, 5700, 5],
        [405, "Bujes de suspension", "TRW", "Universal", 24, 5000, 5],
    ]
    return inventario


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


def productos_registrados(categoria, inventario):
    # Conjunto de tuplas (nombre, marca, modelo): identifica cada autoparte de la categoria.
    # Se usan tuplas porque una lista no se puede guardar dentro de un conjunto.
    registrados = set()
    for producto in inventario[categoria]:
        registrados.add((producto[1].lower(), producto[2].lower(), producto[3].lower()))
    return registrados


def es_duplicado(categoria, nombre, marca, modelo, inventario):
    clave = (nombre.lower(), marca.lower(), modelo.lower())
    return clave in productos_registrados(categoria, inventario)


def pedir_categoria():
    nombres = list(CATEGORIAS)
    print("CATEGORIAS DE PRODUCTOS")
    for i in range(len(nombres)):
        print(f"  {i + 1}. {nombres[i]}")
    indice = pedir_entero("Ingrese el numero de categoria: ", 1, len(nombres))
    return nombres[indice - 1]


def datos(categoria, inventario):
    codigo = generar_codigo(categoria, inventario)
    if codigo is None:
        print("ERROR - No hay codigos disponibles en esa categoria.")
        return None

    nombre = pedir_nombre("Ingrese la autoparte que quiere agregar: ")
    marca = pedir_marca("Ingrese la marca de la autoparte: ")
    modelo = pedir_modelo("Ingrese el modelo al que pertenece la autoparte: ")
    if es_duplicado(categoria, nombre, marca, modelo, inventario):
        print(f"ERROR - Esa autoparte ya esta registrada en {categoria}.")
        print("Para sumar unidades use la opcion 7 (registrar entrada de stock).")
        return None

    precio = pedir_decimal("Ingrese el precio de la autoparte: ", 1)
    stock = pedir_entero("Ingrese el stock existente: ", 0)
    stock_minimo = pedir_entero(
        f"Indique el stock minimo del producto (0 a {stock}): ", 0, stock
    )
    return [codigo, nombre, marca, modelo, stock, precio, stock_minimo]


def agregar_autoparte(inventario):
    categoria = pedir_categoria()
    producto = datos(categoria, inventario)
    if producto is None:
        return None

    inventario[categoria].append(producto)
    print(f"Autoparte agregada con el codigo {producto[0]}.")
    return ("ALTA", categoria, producto, f"stock inicial {producto[4]}")


def mostrar_info(codigo, inventario):
    categoria = categoria_de_codigo(codigo)
    if categoria is None:
        return False, []

    for producto in inventario[categoria]:
        if producto[0] == codigo:
            return True, producto
    return False, []


def modificar_info(producto):
    for i in range(1, len(CAMPOS)):
        print(f"{i}. {CAMPOS[i]}")
    campo = pedir_entero("Ingrese numero para modificar: ", 1, len(CAMPOS) - 1)
    anterior = producto[campo]

    if campo == 1:
        producto[1] = pedir_nombre("Ingrese Producto modificado: ")
    elif campo == 2:
        producto[2] = pedir_marca("Ingrese Marca modificada: ")
    elif campo == 3:
        producto[3] = pedir_modelo("Ingrese Modelo modificado: ")
    elif campo == 4:
        producto[4] = pedir_entero("Ingrese Stock modificado: ", 0)
    elif campo == 5:
        producto[5] = pedir_decimal("Ingrese Precio modificado: ", 1)
    else:
        producto[6] = pedir_entero(f"Ingrese Stock minimo modificado (0 a {producto[4]}): ", 0, producto[4])

    return f"{CAMPOS[campo]}: {anterior} -> {producto[campo]}"


def modificar_autoparte(inventario):
    codigo = pedir_entero("Ingresar codigo de producto: ", 100, 499)
    encontrada, producto = mostrar_info(codigo, inventario)

    if not encontrada:
        print("Producto no encontrado")
        return None

    print("Autoparte:", producto)
    detalle = modificar_info(producto)
    print("Dato modificado ->", detalle)
    return ("MODIFICACION", categoria_de_codigo(codigo), producto, detalle)


def buscar_por_nombre(nombre, productos):
    return list(filter(lambda producto: producto[1].lower() == nombre.lower(), productos))


def eliminar_autoparte(inventario):
    print("⏤" * 120)
    print(" " * 45, "ELIMINAR AUTOPARTE\n")
    print("⏤" * 120)
    print(""" \nSeleccione las siguientes opciones para eliminar una autoparte\n
            * Ingrese 1 para eliminar una autoparte por codigo
            * Ingrese 2 para eliminar una autoparte por nombre""")

    opcion = pedir_entero("Ingrese la opcion para continuar: ", 1, 2)

    if opcion == 1:
        codigo = pedir_entero("Ingrese el codigo de la autoparte a eliminar: ", 100, 499)
    else:
        categoria = pedir_categoria()
        nombre = pedir_texto("Ingrese el nombre de la autoparte: ")
        coincidencias = buscar_por_nombre(nombre, inventario[categoria])

        if len(coincidencias) == 0:
            print("No se encontro ninguna autoparte con ese nombre.")
            return None

        if len(coincidencias) == 1:
            codigo = coincidencias[0][0]
        else:
            # Puede haber varias con el mismo nombre (por ejemplo, distinta marca).
            print("Hay varias autopartes con ese nombre:")
            codigos_validos = set()
            for producto in coincidencias:
                print("  ", producto)
                codigos_validos.add(producto[0])
            codigo = pedir_entero("Ingrese el codigo de la que quiere eliminar: ", 100, 499)
            while codigo not in codigos_validos:
                print("ERROR - Ese codigo no esta entre las opciones mostradas.")
                codigo = pedir_entero("Ingrese el codigo de la que quiere eliminar: ", 100, 499)

    encontrada, producto = mostrar_info(codigo, inventario)
    if not encontrada:
        print("No se encontro ninguna autoparte con ese codigo.")
        return None

    categoria = categoria_de_codigo(codigo)
    inventario[categoria].remove(producto)
    print("Autoparte eliminada correctamente:", producto[1])
    return ("BAJA", categoria, producto, f"stock al eliminar {producto[4]}")


def aplicar_movimiento(producto, tipo, cantidad):
    """Suma (ENTRADA) o resta (SALIDA) unidades del stock.
    Devuelve False si el movimiento no es valido y en ese caso no cambia nada."""
    if cantidad <= 0:
        return False
    if tipo == "ENTRADA":
        producto[4] = producto[4] + cantidad
        return True
    if tipo == "SALIDA" and cantidad <= producto[4]:
        producto[4] = producto[4] - cantidad
        return True
    return False


def actualizar_stock(inventario):
    print("1. ENTRADA (reposicion de mercaderia)")
    print("2. SALIDA (venta o uso de unidades)")
    opcion = pedir_entero("Ingrese el tipo de movimiento: ", 1, len(TIPOS_MOVIMIENTO))
    tipo = TIPOS_MOVIMIENTO[opcion - 1]

    codigo = pedir_entero("Ingrese el codigo de la autoparte: ", 100, 499)
    encontrada, producto = mostrar_info(codigo, inventario)
    if not encontrada:
        print("Producto no encontrado")
        return None
    print(f"{producto[1]} ({producto[2]}) - stock actual: {producto[4]}")

    if tipo == "SALIDA" and producto[4] == 0:
        print("ERROR - No hay unidades en stock para registrar una salida.")
        return None

    if tipo == "ENTRADA":
        cantidad = pedir_entero("Cantidad de unidades que ingresan: ", 1)
    else:
        cantidad = pedir_entero(f"Cantidad de unidades que salen (1 a {producto[4]}): ", 1, producto[4])

    anterior = producto[4]
    if not aplicar_movimiento(producto, tipo, cantidad):
        print("ERROR - Movimiento invalido.")
        return None

    print(f"Stock actualizado: {anterior} -> {producto[4]}")
    if producto[4] < producto[6]:
        print(f"ATENCION - {producto[1]} quedo por debajo del stock minimo ({producto[6]}).")

    detalle = f"{cantidad} unidades: stock {anterior} -> {producto[4]}"
    return (tipo, categoria_de_codigo(codigo), producto, detalle)
