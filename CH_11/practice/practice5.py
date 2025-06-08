class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other): 
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 2
v6 = v2 / 2
print(v3)  # Output: Vector(6, 8)
print(v4)  # Output: Vector(-2, -2)
print(v5)  # Output: Vector(4, 6)
print(v6)  # Output: Vector(2.0, 2.5)
print(v1)  # Output: Vector(2, 3)
print(v2)  # Output: Vector(4, 5)
