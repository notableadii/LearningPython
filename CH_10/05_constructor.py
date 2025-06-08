
class Employee: # class definition

    language = "Python" # class attribute
    salary = 100000 # class attribute

    def __init__(self, name, language, salary): # dunder method which is automatically called when an instance of the class is created
        self.name = name # instance attribute
        self.salary = salary
        self.language = language
        print(f"Employee {self.name} created with salary {self.salary} and language {self.language}")
        
    def getInfo(self): # self is a reference to the instance of the class it is called on we use self to access instance attributes
        print(f"The language is {self.language} and salary is {self.salary}")    
    
    def greet(self):
        print("Hello welcome to the company!")    

# This code snippet demonstrates the use of class attributes and instance attributes in Python.

aditya = Employee("Aditya", "Python", 10000000000) # here aditya is an object of class Employee
# aditya.name = "Aditya" # instance attribute
# aditya.language = "Javascript" # modifying class attribute for this instance
# rohan = Employee() # another object of class Employee