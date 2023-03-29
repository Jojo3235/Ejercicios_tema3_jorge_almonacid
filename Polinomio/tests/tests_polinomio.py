import sys
sys.path.insert(0, "Polinomio")

from polinomio import Polinomio
import unittest

class TestPolinomio(unittest.TestCase):

    def test_agregar_terminos(self):
        polinomio1 = Polinomio()
        Polinomio.agregar_termino(polinomio1, 3, 5)
        self.assertEqual(Polinomio.mostrar(polinomio1),"+5x^3")
        Polinomio.agregar_termino(polinomio1, 2, 2)
        self.assertEqual(Polinomio.mostrar(polinomio1),"+5x^3+2x^2")
        Polinomio.agregar_termino(polinomio1, 1, 3)
        self.assertEqual(Polinomio.mostrar(polinomio1),"+5x^3+2x^2+3x^1")
        Polinomio.agregar_termino(polinomio1, 0, 4)
        self.assertEqual(Polinomio.mostrar(polinomio1),"+5x^3+2x^2+3x^1+4x^0")

    def test_obtener_valor(self):
        polinomio2 = Polinomio()
        Polinomio.agregar_termino(polinomio2, 3, 5)
        Polinomio.agregar_termino(polinomio2, 2, 2)
        Polinomio.agregar_termino(polinomio2, 1, 3)
        Polinomio.agregar_termino(polinomio2, 0, 4)
        self.assertEqual(Polinomio.obtener_valor(polinomio2, 3), 5)

    def test_modificar_terminos(self):
        Polinomio3 = Polinomio()
        Polinomio.agregar_termino(Polinomio3, 2, 5)
        Polinomio.agregar_termino(Polinomio3, 1, 6)
        Polinomio.agregar_termino(Polinomio3, 0, 7)
        Polinomio.modificar_termino(Polinomio3, 2, 10)
        self.assertEqual(Polinomio.mostrar(Polinomio3),"+10x^2+6x^1+7x^0")

    def test_eliminar_terminos(self):
        Polinomio4 = Polinomio()
        Polinomio.agregar_termino(Polinomio4, 2, 5)
        Polinomio.agregar_termino(Polinomio4, 1, 6)
        Polinomio.agregar_termino(Polinomio4, 0, 7)
        Polinomio.eliminar(Polinomio4, 2)
        self.assertEqual(Polinomio.mostrar(Polinomio4),"+6x^1+7x^0")

    def test_existe_terminos(self):
        Polinomio5 = Polinomio()
        Polinomio.agregar_termino(Polinomio5, 2, 5)
        Polinomio.agregar_termino(Polinomio5, 1, 6)
        Polinomio.agregar_termino(Polinomio5, 0, 7)
        self.assertTrue(Polinomio.existe_termino(Polinomio5, 2))

    def test_sumar(self):
        Polinomio6 = Polinomio()
        Polinomio.agregar_termino(Polinomio6, 2, 5)
        Polinomio.agregar_termino(Polinomio6, 1, 6)
        Polinomio.agregar_termino(Polinomio6, 0, 7)
        Polinomio7 = Polinomio()
        Polinomio.agregar_termino(Polinomio7, 2, 5)
        Polinomio.agregar_termino(Polinomio7, 1, 6)
        Polinomio.agregar_termino(Polinomio7, 0, 7)
        self.assertEqual(Polinomio.mostrar(Polinomio.sumar(Polinomio6, Polinomio7)), "+10x^2+12x^1+14x^0")

    def test_multiplicar(self):
        Polinomio8 = Polinomio()
        Polinomio.agregar_termino(Polinomio8, 2, 5)
        Polinomio.agregar_termino(Polinomio8, 1, 6)
        Polinomio.agregar_termino(Polinomio8, 0, 7)
        Polinomio9 = Polinomio()
        Polinomio.agregar_termino(Polinomio9, 2, 5)
        Polinomio.agregar_termino(Polinomio9, 1, 6)
        Polinomio.agregar_termino(Polinomio9, 0, 7)
        self.assertEqual(Polinomio.mostrar(Polinomio.multiplicar(Polinomio8, Polinomio9)), "+25x^4+60x^3+106x^2+84x^1+49x^0")