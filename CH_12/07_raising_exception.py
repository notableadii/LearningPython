
a = int(input("\nEnter a number: "))
b = int(input("\nEnter a second number: "))

if(b == 0):
    raise ZeroDivisionError("Division by zero is not allowed!") # raise is used to raise an exception explicitly and it will stop the program execution
else:
    print(f"The division of {a} and {b} is: {a/b}")