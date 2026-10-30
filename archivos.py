"""Persistencia del sistema.

- inventario.json  -> el inventario completo (diccionario de categorias con sus autopartes).
- movimientos.txt  -> historial de altas, bajas, modificaciones, entradas y salidas (una linea por movimiento).
"""
import json

from inventario import CATEGORIAS, inventario_vacio

ARCHIVO_INVENTARIO = "inventario.json"
ARCHIVO_MOVIMIENTOS = "movimientos.txt"


# ---------------------------------------------------------------- JSON

def guardar_inventario(inventario, nombre_archivo=ARCHIVO_INVENTARIO):
    """Convierte el diccionario de Python a formato JSON y lo escribe en el archivo.
    El modo "w" reemplaza el contenido anterior por el inventario actual."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)


def cargar_inventario(nombre_archivo=ARCHIVO_INVENTARIO):
    """Lee el archivo JSON y lo convierte otra vez en el diccionario del inventario.
    Devuelve None si el archivo no existe o si esta danado."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print(f"No se encontro el archivo '{nombre_archivo}'.")
        return None
    except ValueError:
        # json.load lanza ValueError (JSONDecodeError) si el contenido no es un JSON valido.
        print(f"ERROR - El archivo '{nombre_archivo}' esta danado y no se pudo leer.")
        return None

    # Se arma un inventario con todas las categorias del sistema
    # y se completa con lo que haya en el archivo.
    inventario = inventario_vacio()
    for categoria in CATEGORIAS:
        if categoria in datos:
            inventario[categoria] = datos[categoria]
    return inventario


# ---------------------------------------------------------------- TXT

def registrar_movimiento(tipo, categoria, producto, detalle, nombre_archivo=ARCHIVO_MOVIMIENTOS):
    """Agrega una linea al final del archivo de texto. El modo "a" no borra lo anterior.
    Formato de cada linea:  TIPO,categoria,codigo,autoparte,detalle"""
    linea = tipo + "," + categoria + "," + str(producto[0]) + "," + producto[1] + "," + detalle
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")


def leer_movimientos(nombre_archivo=ARCHIVO_MOVIMIENTOS):
    """Lee el archivo de texto y devuelve una lista de diccionarios (uno por movimiento).
    Las lineas danadas se ignoran y se avisa cuantas fueron."""
    movimientos = []
    lineas_invalidas = 0

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue

                datos = linea.split(",")
                if len(datos) != 5:
                    lineas_invalidas = lineas_invalidas + 1
                    continue

                try:
                    codigo = int(datos[2])
                except ValueError:
                    lineas_invalidas = lineas_invalidas + 1
                    continue

                movimientos.append({
                    "tipo": datos[0],
                    "categoria": datos[1],
                    "codigo": codigo,
                    "autoparte": datos[3],
                    "detalle": datos[4],
                })
    except FileNotFoundError:
        # Todavia no se registro ningun movimiento: el archivo se crea con el primero.
        return []

    if lineas_invalidas > 0:
        print(f"AVISO - Se ignoraron {lineas_invalidas} lineas danadas de '{nombre_archivo}'.")
    return movimientos
