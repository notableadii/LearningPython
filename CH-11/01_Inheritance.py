class Employee:
    company = "Google"
    def Show(self):
        print(f"The name is {self.name} and salary is {self.salary}")
        

# class Programmer():
#     company = "Microsoft"
    
#     def Show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")
        
#     def ShowLanguage(self):
#          print(f"the name is {self.name} and the language is {self.language}")
         

class Programmer(Employee):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The employee is {self.name} and the language is {self.language}")
a = Employee()
b = Programmer()

print(a.company, b.company)