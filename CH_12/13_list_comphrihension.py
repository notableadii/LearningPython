myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# squaredList = []
# for item in myList:
#     squaredList.append(item * item)

squaredList = [item * item for item in myList]  # List comprehension to square each item

print(squaredList)
