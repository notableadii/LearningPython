a = int(input("Enter a number: "))  # Prompt user for input

#if statement example with multiple conditions
#if statement no 1
if(a%2 == 0):  # Check if the number is even
    print("The number is even.")  # If true, print this message    
#if statement no 
if (a >= 18):  # Check if the number is greater than 18
    print("You are eligible to vote.")  # If true, print this message
    print("You can vote in the upcoming elections.")  # Additional message if eligible

elif(a < 0):  # Check if the number is negative
    print("Please enter a valid age.")

else:  # If the condition is false
    print("You are not eligible to vote.")  # Print this message