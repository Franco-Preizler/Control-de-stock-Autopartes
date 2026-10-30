"""Pruebas unitarias del sistema de control de stock de autopartes.

Se ejecutan sin abrir el menu del programa:

    python test_autopartes.py

Cada prueba muestra: la funcion que se prueba, la situacion, los datos usados,
el resultado esperado, el resultado obtenido y si fue aprobada.

Distribucion (consigna, seccion 9):
    VALIDO     pruebas 1 a 6   -> datos correctos
    INVALIDO   pruebas 7 a 10  -> datos incorrectos o situaciones no permitidas
    LIMITE     pruebas 11 a 13 -> valores extremos
    ADICIONAL  prueba 14       -> caso propio de un sistema de autopartes
"""
from inventario import (
    inventario_vacio,
    mostrar_info,
    generar_codigo,
    aplicar_movimiento,
    es_duplicado,
)
from reportes import valor_total_inventario, productos_bajo_minimo, resumen_por_categoria
from archivos import guardar_inventario, cargar_inventario, registrar_movimiento, leer_movimientos

# Archivos separados para que las pruebas no modifiquen los datos reales del sistema.
ARCHIVO_PRUEBA_JSON = "prueba_inventario.json"
ARCHIVO_PRUEBA_TXT = "prueba_movimientos.txt"


def encabezado(numero, tipo, funcion, situacion):
    print(f"Prueba {numero} [{tipo}] - Funcion: {funcion}")
    print("   Situacion:", situacion)


def verificar(datos, esperado, obtenido):
    print("   Datos:    ", datos)
    print("   Esperado: ", esperado)
    print("   Obtenido: ", obtenido)
    if esperado == obtenido:
        print("   Resultado: APROBADA\n")
        return True
    print("   Resultado: FALLIDA\n")
    return False


# ------------------------------------------------------------------ CASOS VALIDOS

def prueba_buscar_codigo_existente():
    encabezado(1, "VALIDO", "mostrar_info", "Buscar una autoparte por un codigo que existe")
    producto = [101, "Filtro de aceite", "BGK", "Volkswagen Polo", 6, 71000, 5]
    inventario = inventario_vacio()
    inventario["Motor"] = [producto]

    obtenido = mostrar_info(101, inventario)
    return verificar("codigo 101, Motor = [" + str(producto) + "]", (True, producto), obtenido)


def prueba_valor_total():
    encabezado(2, "VALIDO", "valor_total_inventario", "Calcular el valor del stock (stock x precio)")
    inventario = inventario_vacio()
    inventario["Motor"] = [[101, "Piston", "BGK", "Polo", 2, 100, 1]]
    inventario["Encendido"] = [[201, "Bujia", "NGK", "Universal", 3, 50, 1]]

    obtenido = valor_total_inventario(inventario)
    return verificar("2 unidades x $100 + 3 unidades x $50", 350, obtenido)


def prueba_entrada_de_stock():
    encabezado(3, "VALIDO", "aplicar_movimiento", "Registrar una ENTRADA de 5 unidades")
    producto = [201, "Bujia", "NGK", "Universal", 6, 18900, 5]

    exito = aplicar_movimiento(producto, "ENTRADA", 5)
    return verificar("stock 6, ENTRADA de 5", (True, 11), (exito, producto[4]))


def prueba_guardar_y_cargar_json():
    encabezado(4, "VALIDO", "guardar_inventario / cargar_inventario",
               "Guardar el inventario en JSON y volver a leerlo (como al reiniciar el programa)")
    inventario = inventario_vacio()
    inventario["Encendido"] = [[202, "Bobina de encendido", "Bosch", "Universal", 25, 34800.5, 5]]

    guardar_inventario(inventario, ARCHIVO_PRUEBA_JSON)
    obtenido = cargar_inventario(ARCHIVO_PRUEBA_JSON)
    return verificar("inventario con 1 autoparte en Encendido", inventario, obtenido)


def prueba_registrar_y_leer_movimiento():
    encabezado(5, "VALIDO", "registrar_movimiento / leer_movimientos",
               "Guardar un movimiento en el TXT y recuperarlo como diccionario")
    archivo = open(ARCHIVO_PRUEBA_TXT, "w", encoding="utf-8")   # deja el archivo vacio
    archivo.close()
    producto = [301, "Radiador", "Valeo", "Universal", 17, 15900, 5]

    registrar_movimiento("ALTA", "Refrigeracion", producto, "stock inicial 17", ARCHIVO_PRUEBA_TXT)
    obtenido = leer_movimientos(ARCHIVO_PRUEBA_TXT)
    esperado = [{"tipo": "ALTA", "categoria": "Refrigeracion", "codigo": 301,
                 "autoparte": "Radiador", "detalle": "stock inicial 17"}]
    return verificar("ALTA del Radiador 301", esperado, obtenido)


def prueba_resumen_marcas_unicas():
    encabezado(6, "VALIDO", "resumen_por_categoria",
               "Contar productos, unidades y marcas sin repetir de una categoria")
    inventario = inventario_vacio()
    inventario["Encendido"] = [
        [201, "Bujia", "NGK", "Universal", 10, 100, 1],
        [202, "Bobina", "Bosch", "Universal", 5, 200, 1],
        [203, "Cables", "Bosch", "Universal", 2, 300, 1],
    ]

    resumen = resumen_por_categoria(inventario)
    obtenido = (resumen["Encendido"]["productos"], resumen["Encendido"]["unidades"],
                resumen["Encendido"]["marcas"])
    return verificar("3 autopartes: NGK, Bosch, Bosch", (3, 17, {"NGK", "Bosch"}), obtenido)


# ------------------------------------------------------------------ CASOS INVALIDOS

def prueba_buscar_codigo_inexistente():
    encabezado(7, "INVALIDO", "mostrar_info", "Buscar un codigo que no esta cargado")
    inventario = inventario_vacio()
    inventario["Motor"] = [[101, "Filtro de aceite", "BGK", "Polo", 6, 71000, 5]]

    obtenido = mostrar_info(150, inventario)
    return verificar("codigo 150 (no existe)", (False, []), obtenido)


def prueba_salida_mayor_al_stock():
    encabezado(8, "INVALIDO", "aplicar_movimiento", "Intentar sacar mas unidades de las que hay")
    producto = [201, "Bujia", "NGK", "Universal", 6, 18900, 5]

    exito = aplicar_movimiento(producto, "SALIDA", 10)
    return verificar("stock 6, SALIDA de 10", (False, 6), (exito, producto[4]))


def prueba_cargar_archivo_inexistente():
    encabezado(9, "INVALIDO", "cargar_inventario", "Abrir un archivo JSON que no existe")

    obtenido = cargar_inventario("archivo_que_no_existe.json")
    return verificar("archivo 'archivo_que_no_existe.json'", None, obtenido)


def prueba_movimientos_con_lineas_danadas():
    encabezado(10, "INVALIDO", "leer_movimientos",
               "El TXT tiene lineas mal escritas: se ignoran sin cortar el programa")
    archivo = open(ARCHIVO_PRUEBA_TXT, "w", encoding="utf-8")
    archivo.write("BAJA,Motor,105,Piston,stock al eliminar 17\n")
    archivo.write("esta linea no tiene el formato correcto\n")
    archivo.write("ALTA,Motor,abc,Filtro,stock inicial 3\n")
    archivo.close()

    obtenido = leer_movimientos(ARCHIVO_PRUEBA_TXT)
    esperado = [{"tipo": "BAJA", "categoria": "Motor", "codigo": 105,
                 "autoparte": "Piston", "detalle": "stock al eliminar 17"}]
    return verificar("1 linea correcta + 2 lineas danadas", esperado, obtenido)


# ------------------------------------------------------------------ CASOS LIMITE

def prueba_salida_igual_al_stock():
    encabezado(11, "LIMITE", "aplicar_movimiento", "Sacar exactamente todas las unidades")
    producto = [201, "Bujia", "NGK", "Universal", 6, 18900, 5]

    exito = aplicar_movimiento(producto, "SALIDA", 6)
    return verificar("stock 6, SALIDA de 6", (True, 0), (exito, producto[4]))


def prueba_stock_igual_al_minimo():
    encabezado(12, "LIMITE", "productos_bajo_minimo",
               "Stock igual al minimo: todavia NO esta por debajo")
    inventario = inventario_vacio()
    inventario["Motor"] = [[101, "Filtro de aceite", "BGK", "Polo", 5, 71000, 5]]

    obtenido = productos_bajo_minimo(inventario)
    return verificar("stock 5, stock minimo 5", [], obtenido)


def prueba_categoria_sin_codigos_libres():
    encabezado(13, "LIMITE", "generar_codigo",
               "La categoria ya usa los 100 codigos posibles (100 a 199)")
    inventario = inventario_vacio()
    for codigo in range(100, 200):
        inventario["Motor"].append([codigo, "Pieza", "BGK", "Polo", 1, 100, 0])

    obtenido = generar_codigo("Motor", inventario)
    return verificar("Motor con los codigos 100 a 199 ocupados", None, obtenido)


# ------------------------------------------------------------------ CASO ADICIONAL

def prueba_autoparte_duplicada():
    encabezado(14, "ADICIONAL", "es_duplicado",
               "Detectar una autoparte ya cargada aunque se escriba con otras mayusculas")
    inventario = inventario_vacio()
    inventario["Encendido"] = [[201, "Bujia", "NGK", "Universal", 19, 18900, 5]]

    obtenido = es_duplicado("Encendido", "BUJIA", "ngk", "universal", inventario)
    return verificar("ya existe ('Bujia','NGK','Universal'); se ingresa ('BUJIA','ngk','universal')",
                     True, obtenido)


def ejecutar_pruebas():
    resultados = [
        prueba_buscar_codigo_existente(),
        prueba_valor_total(),
        prueba_entrada_de_stock(),
        prueba_guardar_y_cargar_json(),
        prueba_registrar_y_leer_movimiento(),
        prueba_resumen_marcas_unicas(),
        prueba_buscar_codigo_inexistente(),
        prueba_salida_mayor_al_stock(),
        prueba_cargar_archivo_inexistente(),
        prueba_movimientos_con_lineas_danadas(),
        prueba_salida_igual_al_stock(),
        prueba_stock_igual_al_minimo(),
        prueba_categoria_sin_codigos_libres(),
        prueba_autoparte_duplicada(),
    ]
    aprobadas = resultados.count(True)
    print("=" * 60)
    print(f"RESULTADO FINAL: {aprobadas} de {len(resultados)} pruebas aprobadas")
    print("=" * 60)


if __name__ == "__main__":
    ejecutar_pruebas()
