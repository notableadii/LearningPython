class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, c):
        return Complex(self.r + c.r, self.i + c.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"
# This code defines a Complex class with methods for addition and string representation.
# It allows for the addition of two complex numbers using the + operator and prints them in a readable format.

    
    
c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1 +c2)  # This will call the __add__ method of the Complex class