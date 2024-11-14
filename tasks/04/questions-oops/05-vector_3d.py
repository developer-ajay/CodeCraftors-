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
    pass

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