#https://github.com/jperezmachin/lab11-JP-PN
#Partner 1: Prisha Narne
#Partner 2: Julio Perez
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(3, 5), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(2, 8), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(-2, 8)
        with self.assertRaises(ValueError):
            log(10, -5)

 
# Do not touch this
import unittest
import calculator

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4,3),12)
        self.assertEqual(calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2),5)
        self.assertEqual(calculator.divide(5,0), "Error: Division by zero")

    def test_log_invalid_argument(self):
        self.assertEqual(calculator.logarithm(0,0), "Logarithm inputs must be positive")
        self.assertEqual(calculator.logarithm(2, 2),4)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(2,2), math.sqrt(8))

    def test_square_root(self):
        self.assertEqual(calculator.square_root(-4), "Square root inputs must be positive")
        self.assertEqual(calculator.square_root(4), 2)




if __name__ == "__main__":
    unittest.main()