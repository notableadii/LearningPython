class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        return print(f"{self.i}, {self.j}")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)  # Call the constructor of the parent class
        self.k = k

    def show(self):
        return print(f"{self.i}, {self.j}, {self.k}")


o = TwoDVector(1, 2)
o.show()  # Output: (1, 2)
b = ThreeDVector(3, 4, 5)
b.show()  # Output: (3, 4, 5)
