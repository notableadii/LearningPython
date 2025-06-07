class Employee: # class definition
    language = "Python" # class attribute
    salary = 100000 # class attribute
    
    
aditya = Employee() # here aditya is an object of class Employee
# Accessing attributes of the object
aditya.name = "Aditya" # instance attribute
print(f"{aditya.name}, {aditya.language}, {aditya.salary}")


rohan = Employee() # another object of class Employee
rohan.name = "Rohan" # instance attribute
print(f"{rohan.name}, {rohan.language}, {rohan.salary}")

# here name is instance attribute
# and salary and language are class attributes