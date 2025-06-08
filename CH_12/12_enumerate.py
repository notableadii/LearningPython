l = [2, 43, 5, 3, 1, 6, 7, 8, 9, 10]
# index = 0
# for i in l:
#     print(f"the item number {index} is {i}")
#     index += 1
# Using enumerate to achieve the same result
for index, item in enumerate(l):
    print(f"The item number {index} is {item}")
