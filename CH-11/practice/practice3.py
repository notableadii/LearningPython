class Employee:
    salary = 1000
    incriment = 20
    @property
    def salaryAfterIncriment(self):
        return print(self.salary + self.salary * (self.incriment / 100))
    @salaryAfterIncriment.setter
    def salaryAfterIncriment(self, salary):
        self.incriment = ((salary/self.salary) -1)* 100
    
e = Employee()
# print(e.salary)
e.salaryAfterIncriment = 1200  # This will call the setter method
print(e.incriment)  # This will print the updated increment percentage
