class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
            
            
p = Programmer("Aditya", 100000, 442701)
print(p.name, p.salary, p.pincode, p.company)

d = Programmer("Udit", 500, 122006)
print(d.name, d.salary, d.pincode, p.company)