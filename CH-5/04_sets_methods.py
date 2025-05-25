s = {1, 3, 5, 63, 5, 5, 5, "Aditya"} # Creating a set with integers and a string

print(s, type(s))  # <class 'set'>

s.add(100)  # add() adds an element to the set

print(s)

s.remove(100)  # remove() removes an element from the set, raises KeyError if not found
print(s)

s.clear()  # clear() removes all elements from the set
print(s)