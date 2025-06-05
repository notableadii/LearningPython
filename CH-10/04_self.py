class Employee: # class definition
    language = "Python" # class attribute
    salary = 100000 # class attribute
    
    def getInfo(self): # self is a reference to the instance of the class it is called on we use self to access instance attributes
        print(f"The language is {self.language} and salary is {self.salary}")
# This code snippet demonstrates the use of class attributes and instance attributes in Python.
    
aditya = Employee() # here aditya is an object of class Employee
# Accessing attributes of the object
aditya.name = "Aditya" # instance attribute
aditya.language = "Javascript" # modifying class attribute for this instance
# print(f"{aditya.name}, {aditya.language}, {aditya.salary}")

# aditya.getInfo() # calling the instance method to get instance attributes
Employee.getInfo(aditya) # calling the class method to get class attributes