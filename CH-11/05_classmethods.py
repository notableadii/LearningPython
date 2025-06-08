class Employee:
    a = 1
    @classmethod # This is a class method which is used to access class attributes it will not change the instance attributes
    def show(cls):
        print(f"The class value of a is {cls.a}")
        
a = Employee()
a.a = 2  # This will change the instance variable 'a' for this instance only

a.show()