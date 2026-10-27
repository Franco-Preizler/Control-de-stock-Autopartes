"""Pruebas unitarias con unittest, listas y comparaciones de resultados.
Ejecutar: python -m unittest discover -v
"""
import unittest
from Modificar_stock import mostrar_info
from validar_stock_minimo import validar_stock_minimo
from Consulta_total import mostrar_autopartes


class PruebasAutopartes(unittest.TestCase):

    def test_buscar_codigo_existente(self):
        producto = ['Motor', 101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        resultado = mostrar_info(101, [producto])
        self.assertEqual(resultado, (True, producto))

    def test_buscar_codigo_inexistente(self):
        producto = ['Motor', 101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        resultado = mostrar_info(102, [producto])
        self.assertEqual(resultado, (False, []))

    def test_buscar_en_lista_vacia(self):
        resultado = mostrar_info(101, [])
        self.assertEqual(resultado, (False, []))

    def test_buscar_producto_correcto_entre_varios(self):
        primero = ['Motor', 101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        segundo = ['Motor', 102, 'Bujia', 'NGK', 'Gol', 4, 200, 2]
        resultado = mostrar_info(102, [primero, segundo])
        self.assertEqual(resultado, (True, segundo))

    def test_detectar_stock_bajo(self):
        producto = ['Motor', 101, 'Filtro', 'Bosch', 'Polo', 2, 100, 5]
        resultado = validar_stock_minimo([[producto], [], [], []])
        self.assertEqual(resultado, [producto])

    def test_stock_igual_al_minimo_no_es_bajo(self):
        producto = ['Motor', 101, 'Filtro', 'Bosch', 'Polo', 5, 100, 5]
        resultado = validar_stock_minimo([[producto], [], [], []])
        self.assertEqual(resultado, [])

    def test_stock_bajo_en_distintas_categorias(self):
        motor = ['Motor', 101, 'Filtro', 'Bosch', 'Polo', 1, 100, 3]
        encendido = ['Encendido', 201, 'Bujia', 'NGK', 'Gol', 2, 200, 4]
        resultado = validar_stock_minimo([[motor], [encendido], [], []])
        self.assertEqual(resultado, [motor, encendido])

    def test_inventario_vacio(self):
        resultado = mostrar_autopartes([], [], [], [])
        self.assertEqual(resultado, [[], [], [], []])

    def test_consultar_inventario(self):
        motor = ['Motor', 101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        resultado = mostrar_autopartes([motor], [], [], [])
        self.assertEqual(resultado, [[motor], [], [], []])


if __name__ == '__main__':
    unittest.main()
