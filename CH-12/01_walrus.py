# walrus operator := allows assignment within an expression
# This operator is used to assign a value to a variable as part of an expression.
# It is useful for reducing code duplication and improving readability.
# Example:

if(n:= len([1, 2, 3, 4, 5])) > 3:
    print(f"The length of the list is {n}, which is greater than 3.")
else:
    print(f"The length of the list is {n}, which is not greater than 3.")