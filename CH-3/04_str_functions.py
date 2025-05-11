# length funciton (len) 

a = "hello"


print(len(a), a) # 5

# endswith function 

print(a.endswith("o")) # True
print(a.endswith("l")) # False

# starswith function

print(a.startswith("h")) # True
print(a.startswith("l")) # False

# find function

print(a.find("l")) # 2
print(a.find("o")) # 4

# replace function

print(a.replace("l", "L")) # heLLo
print(a.replace("l", "L", 1)) # heLlo

