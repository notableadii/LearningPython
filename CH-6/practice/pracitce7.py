post = input("Enter a string: ")

required_words = ["Aditya", "aditya", "ADITYA"]

if (post in required_words):
    print("This post has aditya in it")
else:
    print("This post does not have aditya in it")