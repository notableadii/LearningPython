# Type Function is used to check the type of an object

a = 10
b = 20.5
c = "Hello World"
d = True
e = None

f = type(a) # type function is used to check the type of an object

print(f) # f = <class 'int'> because a is an integer
print(type(b)) # <class 'float'> because b is a float
print(type(c)) # <class 'str'> because c is a string
print(type(d)) # <class 'bool'> because d is a boolean
print(type(e)) # <class 'NoneType'> because e is None


# float function is used to convert an object to a float
# int function is used to convert an object to an integer
g = "10.5" # g is a string

g = float(g) # g is converted to a float
print(type(g)) # <class 'float'> because g is a float

print(type(str(31.5))) # str function is used to convert an object to a string
print(type(int(31.5))) # int function is used to convert an object to an integer
print(type(float(31.5))) # float function is used to convert an object to a float
print(type(bool(31.5))) # bool function is used to convert an object to a boolean
print(type(complex(31.5))) # complex function is used to convert an object to a complex number