from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass  # Abstract method with no implementation
    
    def describe(self):
        """A concrete method common to all shapes"""
        return "This is a shape"

# Concrete class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Concrete class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Instantiate and use the concrete classes
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)

print(circle.describe())       # Output: This is a shape
print(f"Circle Area: {circle.area()}")  # Output: Circle Area: 78.5

print(rectangle.describe())    # Output: This is a shape
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 24
