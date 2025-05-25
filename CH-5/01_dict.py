d = {} # Creating an empty dictionary

marks = {
    "Aditya": 90,
    "Rohan": 85,
    "Sita": 95,
    "list": [1, 2, 3, 4, 5],  # list as a value
}

print(marks, type(marks))  # <class 'dict'>
print(marks["list"]) # Accessing the list value
print("marks of aditya", marks["Aditya"])  # Accessing value by key