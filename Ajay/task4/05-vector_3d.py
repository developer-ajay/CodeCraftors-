class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Addition only supported between two Vector3D objects")
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Dot product only supported between two Vector3D objects")
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __eq__(self, other):
        if not isinstance(other, Vector3D):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"



v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)


v3 = v1 + v2
print(v3)  


dot_product = v1 * v2
print(dot_product)  


print(v1 == v2)  
print(v1 == Vector3D(1, 2, 3))  


print(str(v1)) 
