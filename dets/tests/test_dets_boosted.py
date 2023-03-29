import sys
sys.path.insert(0, "dets")

import unittest
from dets_boosted import Matrix

class TestMatrix(unittest.TestCase):

    def test_insert(self):
        matrix = Matrix(3, 3)
        matrix.set_value(0, 0, 1)
        matrix.set_value(0, 1, 2)
        matrix.set_value(0, 2, 3)
        matrix.set_value(1, 0, 4)
        matrix.set_value(1, 1, 5)
        matrix.set_value(1, 2, 6)
        matrix.set_value(2, 0, 7)
        matrix.set_value(2, 1, 8)
        matrix.set_value(2, 2, 9)
        self.assertEqual(matrix.get_value(0, 0), 1)
        self.assertEqual(matrix.get_value(0, 1), 2)
        self.assertEqual(matrix.get_value(0, 2), 3)
        self.assertEqual(matrix.get_value(1, 0), 4)
        self.assertEqual(matrix.get_value(1, 1), 5)
        self.assertEqual(matrix.get_value(1, 2), 6)
        self.assertEqual(matrix.get_value(2, 0), 7)
        self.assertEqual(matrix.get_value(2, 1), 8)
        self.assertEqual(matrix.get_value(2, 2), 9)

    def test_strassen_determinante(self):
        matrix = Matrix(3, 3)
        matrix.set_value(0, 0, 1)
        matrix.set_value(0, 1, 2)
        matrix.set_value(0, 2, 3)
        matrix.set_value(1, 0, 4)
        matrix.set_value(1, 1, 5)
        matrix.set_value(1, 2, 6)
        matrix.set_value(2, 0, 7)
        matrix.set_value(2, 1, 8)
        matrix.set_value(2, 2, 9)
        self.assertEqual(matrix.strassen_determinante(), 0)
        
        matrix2 = Matrix(3, 3)
        matrix2.set_value(0, 0, 1)
        matrix2.set_value(0, 1, 2)
        matrix2.set_value(0, 2, 9)
        matrix2.set_value(1, 0, 4)
        matrix2.set_value(1, 1, 2)
        matrix2.set_value(1, 2, 6)
        matrix2.set_value(2, 0, 4)
        matrix2.set_value(2, 1, 1)
        matrix2.set_value(2, 2, 3)
        self.assertEqual(matrix2.strassen_determinante(), -12)

    def test_get_value(self):
        matrix = Matrix(3, 3)
        matrix.set_value(0, 0, 1)
        matrix.set_value(0, 1, 2)
        matrix.set_value(0, 2, 3)
        matrix.set_value(1, 0, 4)
        matrix.set_value(1, 1, 5)
        matrix.set_value(1, 2, 6)
        matrix.set_value(2, 0, 7)
        matrix.set_value(2, 1, 8)
        matrix.set_value(2, 2, 9)
        self.assertEqual(matrix.get_value(0, 0), 1)