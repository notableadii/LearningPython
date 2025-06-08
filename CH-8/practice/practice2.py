# c/5 = f-32/9 

def f_to_c(f):
    return round(5/9*(f-32), 2)



f = float(input("Enter temperature in F: "))

print(f"{f_to_c(f)} Degree C")