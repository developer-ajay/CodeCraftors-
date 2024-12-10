"""
5. Medium: Implement a class 'Vector3D' that represents a 3D vector.
Overload the following operators:
- + (addition of vectors)
- * (dot product with another vector)
- == (equality comparison)
- str (string representation)
"""
import unittest
import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    def __mul__(self, other):
        # Dot product
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)
    
    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class TestVector3D(unittest.TestCase):
    def test_operations(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(str(v1), "(1, 2, 3)")
        self.assertEqual(str(v1 + v2), "(5, 7, 9)")
        self.assertEqual(v1 * v2, 32)
        self.assertTrue(v1 == Vector3D(1, 2, 3))
        self.assertFalse(v1 == v2)

if __name__ == "__main__":
    unittest.main()