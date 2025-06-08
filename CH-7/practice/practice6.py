# what is factorial of a number?
# Factorial of a number n is the product of all positive integers less than or equal to n.

n = int(input("Enter a number: "))

product = 1
for i in range(1, n + 1):
    product = product * i
print(f"Factorial of {n} is {product}")