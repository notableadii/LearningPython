message = input("Enter username: ")
# Check if the username is at least 10 characters long
if len(message) < 10:
    print("Username must be at least 10 characters long")
else:
    print("Username is valid")