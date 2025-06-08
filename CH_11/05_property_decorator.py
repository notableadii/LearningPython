class Employee:
    a = 1
    @classmethod # This is a class method which is used to access class attributes it will not change the instance attributes
    def show(cls):
        print(f"The class value of a is {cls.a}")
    
    @property  # This is a property decorator which allows us to access instance attributes like class attributes
    def name(self):
        return f"{self.fname} and {self.lname}"
    @name.setter # This is a setter method for the name property which allows us to set the value of the name property
    
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
e = Employee()
e.a = 2  # This will change the instance variable 'a' for this instance only
e.name = "Aditya Shah"
print(e.name)  # Accessing the name property    
e.show()