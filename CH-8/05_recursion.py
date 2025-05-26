'''

factorial(1) = 1
factorial(2) = 2 X 1 = 2
factorial(3) = 3 X 2 X 1 = 6
factorial(4) = 4 X 3 X 2 X 1 = 24
factorial(5) = 5 X 4 X 3 X 2 X 1 = 120

factorial(n) = n X n-1 X.... 3 x 2 X 1
factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if (n==1 or n==0):
        return 1  # base case: factorial of 0 or 1 is 1
    return n*factorial(n-1) 

n= int(input("Enter a number: "))

print(f"factorial({n}) = {factorial(n)}")