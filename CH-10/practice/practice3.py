class Demo:
    a = 4

o = Demo()
print(o.a)
o.a = 0
print(Demo.a)
print(o.a)