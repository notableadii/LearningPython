from typing import List, Tuple, Dict, Any, Union

# This code demonstrates the use of type hints in Python.
# Type hints are used to indicate the expected data types of variables, function parameters, and return values.
# They help improve code readability and can be used by static type checkers to catch potential errors.


# Type hints for variables

numbers: List[int] = [1, 2, 3, 4, 5]
coordinates: Tuple[float, float] = (10.5, 20.3)
user = Dict[str, Union[str, int]]
user = {"name": "Alice", "age": 30}
# Type hints for function parameters and return types


n : int = 5

name : str = "John Doe"

def sum(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b
def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"
def is_even(n: int) -> bool:
    """Checks if a number is even."""
    return n % 2 == 0
def factorial(n: int) -> int:
    """Calculates the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def main():
    print(f"Sum of 3 and 4: {sum(3, 4)}")
    print(greet(name))
    print(f"Is {n} even? {'Yes' if is_even(n) else 'No'}")
    print(f"Factorial of {n}: {factorial(n)}")
# if __name__ == "__main__":

main()
# This code demonstrates the use of type hints in Python.