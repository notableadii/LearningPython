marks = {
    "Aditya": 90,
    "Rohan": 85,
    "Sita": 95,
    "list": [1, 2, 3, 4, 5],  # list as a value
    0: "zero",  # integer key
}

print(marks.items())  # items() returns a view object that displays a list of a dictionary's key-value tuple pairs

print(marks.keys())  # keys() returns a view object that displays a list of all the keys in the dictionary

print(marks.values())  # values() returns a view object that displays a list of all the values in the dictionary

marks.update({"Aditya": 95, "Rohan": 90, "Puta": 90})  # update() updates the value of the key if it exists, otherwise adds a new key-value pair
print(marks)

print(marks.get("Aditya"))  # get() returns the value of the key if it exists, otherwise returns None
print(marks.get("NonExistentKey"))  # get() returns None for a non-existent key

marks.pop("Aditya")  # pop() removes the key-value pair and returns the value
print(marks)

print("length", marks.__len__())  # __len__() returns the number of key-value pairs in the dictionary