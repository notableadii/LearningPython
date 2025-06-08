class Demo:
    a = 4

o = Demo()
print(o.a) # prints class attribute because instance attribute is not present


o.a = 0 # instance attribute is created
print(Demo.a) # prints class attribute
print(o.a) # prints instance attribute

# setting instance attribute does not change class attribute 