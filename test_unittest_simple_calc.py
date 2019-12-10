import unittest
from simple_calc import simple_calc
class Calctest(unittest.TestCase):
    calc = simple_calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(4, 3), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(8, 2), 4)