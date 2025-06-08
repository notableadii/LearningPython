l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# map example

squre = lambda x: x * x

sqList = list(
    map(squre, l)
)  # Using map to apply the squre function to each element in l
print(sqList)  # This will print the list of squared numbers


# filter example
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


onlyEven = list(filter(is_even, l))  # Using filter to get only even numbers from l
print(onlyEven)  # This will print the list of even numbers


# reduce example
from functools import reduce


def sum(x, y):
    return x + y


print(reduce(sum, l))  # Using reduce to sum all elements in l
# This will print the sum of all numbers in the list
# Output: 45
