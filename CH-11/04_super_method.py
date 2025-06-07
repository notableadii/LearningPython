class Employee:
    def __init__(self):
        print("constructor of employee")
    a = 11

class Programmer(Employee):
    def __init__(self):
      print("constructor of programmer")
    b = 12

class Manager(Programmer):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        print("constructor of manager")
    c = 13

# e = Employee()

# print(e.a)

# e = Programmer()
# print(e.a)
# print(e.b)
e = Manager()
# print(e.a)
# print(e.b)
# print(e.c)