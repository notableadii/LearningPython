class Vector:
    def __init__(self, l):
        self.l = l
        
    def __len__(self):
        return len(self.l)
    
    
v1 = Vector([1, 2, 3, 4, 5])
print(len(v1))  # Output: 5
# this code defines a Vector class that takes a list as an argument and implements the __len__ method to return the length of that list. When len(v1) is called, it returns the length of the list stored in v1, which is 5 in this case.
