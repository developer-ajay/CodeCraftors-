import unittest

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        return pi * (self.radius ** 2)


square = Square(4)  
circle = Circle(3)  

print(f"Square area: {square.area()}") 
print(f"Circle area: {circle.area()}")  

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
