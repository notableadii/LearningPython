class Employee:
    a = 11

class Programmer(Employee):
    b = 12

class Manager(Programmer):
    c = 13

e = Employee()

print(e.a)
# print(e.b) #shows error because b is not present in Employee class
e = Programmer()
print(e.a)
print(e.b)
e = Manager()
print(e.a)
print(e.b)
print(e.c)