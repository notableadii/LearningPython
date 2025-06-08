a = 68  # this is a global variable


def fun():
    global a  # global keyword allows us to modify the global variable
    a = 5

    print(a)


fun()
print(a)
