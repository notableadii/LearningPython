friends = ["Alice", "Bob", "Charlie", 5, 0.5, True]

print(friends)

friends.append("Eve") # add to the end of the list
print(friends)


l1 = [5,6,23, 1, 2, 3]

l1.sort() # sort the list in place 
print(l1)

l1.sort(reverse=True) # sort the list in place in reverse order
print(l1)

friends.insert(1, "David") # insert function is used to insert an element at a specific index
print(friends)

friends.pop(1) # pop function is used to remove an element at a specific index
print(friends)

value = friends.pop() # pop function is used to remove the last element of the list
print(value) # it returns the value of the popped element