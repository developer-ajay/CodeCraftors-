"""
1. Easy: Create a class 'Shape' with a method 'area()' that returns 0. 
Create two derived classes 'Square' and 'Circle' that override the area method.
- Square takes side length as parameter
- Circle takes radius as parameter (use 3.14 for pi)
"""
import unittest
import math

class Shape:
    pass

class Square(Shape):
    pass

class Circle(Shape):
    pass

class TestShapes(unittest.TestCase):
    def test_shape_area(self):
        shape = Shape()
        self.assertEqual(shape.area(), 0)
    
    def test_square_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)
    
    def test_circle_area(self):
        circle = Circle(2)
        self.assertEqual(circle.area(), 12.56)

if __name__ == "__main__":
    unittest.main()