# there are three types of strings in python

a = "hello world"  # single quotes
b = 'hello world'  # double quotes
c = """hello world"""  # triple quotes

# strings are immutable meanning they cannot be changed

# strings are indexed meaning each character in the string has an index

name = "John Doe"
# indexing starts from 0
nameshort = name[0:4]  # slicing the string from index 0 to 4
character1 = name[0]  # getting the first character of the string
character2 = name[1]  # getting the second character of the string

print(nameshort)  # prints John
print(character1)  # prints J
print(character2)  # prints o
