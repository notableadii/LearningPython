# practice 1

# write a program that creates a dictionary of hindi words and there english translations.

words = {
    "madad": "help",
    "kursi": "chair",
    "billi": "cat",
}



word = input("Enter a Hindi word to translate to English: ") # Prompt user for input
print("The English translation is:", words.get(word, "Translation not found.")) # Use get() to safely retrieve the translation, providing a default message if not found

#practice 2

# write a progtam to input a list of numbers and print all the unique numbers in the list.

s = set()  # Initialize an empty set to store unique numbers
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set
n = input("Enter numbers: ")  # Prompt user for input
s.add(int(n))  # Convert input to an integer and add it to the set

print("Unique numbers in the list are:", s)  # Print the unique numbers stored in the set


# practice 3

s = set()  # Initialize an empty set to store unique numbers

s.add(1)  # Add the number 1 to the set
s.add("1")  # Add the string "hello" to the set
print(s)  # Print the contents of the set


s = set()  # Initialize an empty set to store unique numbers
s.add(1)  # Add the number 1 to the set
s.add("1")  # Add the string "1" to the set
s.add(1.0)  # Add the float 1.0 to the set
print(len(s))  # Print the number of unique elements in the set # Output: 2, since 1, "1", and 1.0 are considered the same value in a set

# practice 4
d = {}  # Initialize an empty dictionary

name = input("Enter friend's name: ")  # Prompt user for their name
lang = input("Enter language: ")  # Prompt user for their preferred language

d.update({name: lang})  # Update the dictionary with the name and language as a key-value pair
name = input("Enter friend's name: ")  # Prompt user for their name
lang = input("Enter language: ")  # Prompt user for their preferred language

d.update({name: lang})  # Update the dictionary with the name and language as a key-value pair
name = input("Enter friend's name: ")  # Prompt user for their name
lang = input("Enter language: ")  # Prompt user for their preferred language

d.update({name: lang})  # Update the dictionary with the name and language as a key-value pair
name = input("Enter friend's name: ")  # Prompt user for their name
lang = input("Enter language: ")  # Prompt user for their preferred language

d.update({name: lang})  # Update the dictionary with the name and language as a key-value pair

print("Friends and their languages:", d)  # Print the dictionary containing friends' names and their preferred languages

#practice 5

#can u change the values inside a list inside a set?

s = {9, 8, 12, "Aditya", [1,2]}

# No, you cannot change the values inside a list that is part of a set because lists are mutable and sets require their elements to be immutable.

