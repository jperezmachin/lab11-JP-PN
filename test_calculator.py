#https://github.com/jperezmachin/lab11-JP-PN
#Partner 1: Prisha Narne
#Partner 2: Julio Perez
import math
import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(3, 5), -2)

    def test_divide_by_zero(self):
        self.assertEqual(calculator.div(10, 0), "Error: Division by zero")
        self.assertEqual(calculator.div(5, 0), "Error: Division by zero")

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        self.assertEqual(calculator.logarithm(0, 10), "Logarithm inputs must be positive")
        self.assertEqual(calculator.logarithm(-2, 8), "Logarithm inputs must be positive")
        self.assertEqual(calculator.logarithm(10, -5), "Logarithm inputs must be positive")

 
# Do not touch this


    def test_multiply(self):
        self.assertEqual(calculator.mul(4,3),12)
        self.assertEqual(calculator.mul(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2),5)
        self.assertEqual(calculator.div(5,0), "Error: Division by zero")

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