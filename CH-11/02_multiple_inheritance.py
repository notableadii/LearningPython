class Employee:
    company = "Google"
    name = "Rohan"
    salary = 100000
    def Show(self):
        print(f"The name is {self.name} and salary is {self.salary}")
        
class coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language is {self.language}")


class Programmer(Employee, coder):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The employee is {self.name} and the language is {self.language}")
# a = Employee()
b = Programmer()

b.showLanguage()
b.Show()
b.printLanguage()