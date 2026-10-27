import io
import unittest
from contextlib import redirect_stdout

from inventario import mostrar_info, inventario_vacio
from reportes import validar_stock_minimo, listar_inventario


class PruebasAutopartes(unittest.TestCase):

    def test_buscar_codigo_existente(self):
        producto = [101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        inventario = inventario_vacio()
        inventario["Motor"] = [producto]
        resultado = mostrar_info(101, inventario)
        self.assertEqual(resultado, (True, producto))

    def test_buscar_codigo_inexistente(self):
        producto = [101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        inventario = inventario_vacio()
        inventario["Motor"] = [producto]
        resultado = mostrar_info(102, inventario)
        self.assertEqual(resultado, (False, []))

    def test_buscar_en_lista_vacia(self):
        inventario = inventario_vacio()
        resultado = mostrar_info(101, inventario)
        self.assertEqual(resultado, (False, []))

    def test_buscar_producto_correcto_entre_varios(self):
        primero = [101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        segundo = [102, 'Bujia', 'NGK', 'Gol', 4, 200, 2]
        inventario = inventario_vacio()
        inventario["Motor"] = [primero, segundo]
        resultado = mostrar_info(102, inventario)
        self.assertEqual(resultado, (True, segundo))

    def test_detectar_stock_bajo(self):
        producto = [101, 'Filtro', 'Bosch', 'Polo', 2, 100, 5]
        inventario = inventario_vacio()
        inventario["Motor"] = [producto]
        with redirect_stdout(io.StringIO()):
            resultado = validar_stock_minimo(inventario)
        self.assertEqual(resultado, [['Motor'] + producto])

    def test_stock_igual_al_minimo_no_es_bajo(self):
        producto = [101, 'Filtro', 'Bosch', 'Polo', 5, 100, 5]
        inventario = inventario_vacio()
        inventario["Motor"] = [producto]
        with redirect_stdout(io.StringIO()):
            resultado = validar_stock_minimo(inventario)
        self.assertEqual(resultado, [])

    def test_stock_bajo_en_distintas_categorias(self):
        motor = [101, 'Filtro', 'Bosch', 'Polo', 1, 100, 3]
        encendido = [201, 'Bujia', 'NGK', 'Gol', 2, 200, 4]
        inventario = inventario_vacio()
        inventario["Motor"] = [motor]
        inventario["Encendido"] = [encendido]
        with redirect_stdout(io.StringIO()):
            resultado = validar_stock_minimo(inventario)
        self.assertEqual(resultado, [['Motor'] + motor, ['Encendido'] + encendido])

    def test_inventario_vacio(self):
        inventario = inventario_vacio()
        with redirect_stdout(io.StringIO()):
            resultado = listar_inventario(inventario)
        self.assertEqual(resultado, [])

    def test_consultar_inventario(self):
        motor = [101, 'Filtro', 'Bosch', 'Polo', 6, 100, 3]
        inventario = inventario_vacio()
        inventario["Motor"] = [motor]
        with redirect_stdout(io.StringIO()):
            resultado = listar_inventario(inventario)
        self.assertEqual(resultado, [['Motor'] + motor])


if __name__ == '__main__':
    unittest.main()

