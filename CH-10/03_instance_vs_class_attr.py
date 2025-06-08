class Employee: # class definition
    language = "Python" # class attribute
    salary = 100000 # class attribute
    
    
aditya = Employee() # here aditya is an object of class Employee
# Accessing attributes of the object
aditya.name = "Aditya" # instance attribute
aditya.language = "Javascript" # modifying class attribute for this instance
print(f"{aditya.name}, {aditya.language}, {aditya.salary}")
