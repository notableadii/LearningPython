# what are conditionals?
# Conditionals are statements that allow you to execute certain code based on whether a condition is true or false.
# for example, you can use an if statement to check if a variable is equal to a certain value, and if it is, execute some code.
# In Python, you can use if, elif, and else statements to create conditionals.

# if elif else ladder 
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

print("Have a nice day!") # This message will always be printed regardless of the conditions above

