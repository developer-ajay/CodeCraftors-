
"""
3. Easy: Create a class 'Calculator' with static methods 'add' and 'multiply'.
These methods should take variable number of arguments (*args) and return their sum and product respectively.
If no arguments are provided, return 0 for add and 1 for multiply.
"""
import unittest
import math
class Calculator:
    pass

class TestCalculator(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(Calculator.add(), 0)
        self.assertEqual(Calculator.multiply(), 1)
    
    def test_single_arg(self):
        self.assertEqual(Calculator.add(5), 5)
        self.assertEqual(Calculator.multiply(5), 5)
    
    def test_multiple_args(self):
        self.assertEqual(Calculator.add(1, 2, 3), 6)
        self.assertEqual(Calculator.multiply(2, 3, 4), 24)

if __name__ == '__main__':
    unittest.main()