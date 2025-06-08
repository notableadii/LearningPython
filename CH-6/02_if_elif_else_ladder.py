# if elif else ladder example

a = int(input("Enter a number: "))  # Prompt user for input

if (a >= 18):  # Check if the number is greater than 18
    print("You are eligible to vote.")  # If true, print this message
    print("You can vote in the upcoming elections.")  # Additional message if eligible

elif(a < 0):  # Check if the number is negative
    print("Please enter a valid age.")

elif(a == 0):
    print("You are entering the world, welcome!")

else:  # If the condition is false
    print("You are not eligible to vote.")  # Print this message