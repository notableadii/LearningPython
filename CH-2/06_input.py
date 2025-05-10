# input() function is used to take input from the user

a = input("Enter a number: ") # a is a string
b = input("Enter a number: ") # b is a string

print("Number a = ", a) # Input of the user is taken as a string
print("Number b = ", b) # Input of the user is taken as a string

print("Sum of a and b = ", a + b) # and b are strings so they will be concatenated

print("Type of a = ", type(a)) # <class 'str'> because a is a string
print("Type of b = ", type(b)) # <class 'str'> because b is a string

# after taking input from the user we need to convert the string to an integer

c = int(a) # a is converted to an integer
d = int(b) # b is converted to an integer

print("Type of a after converting = ", type(c)) # <class 'str'> because a is a string
print("Type of b after converting = ", type(d)) # <class 'str'> because b is a string

print("Sum of a and b = ", c + d) # sum of a and b