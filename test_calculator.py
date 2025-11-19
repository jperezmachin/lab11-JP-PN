import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

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