class Calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n*self.n}")
    
    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
    
    def square_root(self):
        print(f"The square is {self.n**1/2}")
        
    @staticmethod # stattic method is used to create a function inside a class without self parameter
    def greet():
        print("Hello, how are you?")
        
        
        
a = Calculator(5)
a.greet()
a.square()
a.cube()
a.square_root()