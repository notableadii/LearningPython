# problem 1

name = input("Enter your name: ")

print(f"Hello {name}.") # f string is used to format the string and u can use variables inside the string using {}

#problem 2

letter = "[NAME] You are selected for the [POSITION] position in [COMPANY]."

print(letter.replace("[NAME]", name).replace("[POSITION]", "Software Engineer").replace("[COMPANY]", "Turing")) # this will replace the [NAME] with the name entered by the user and [POSITION] with Software Engineer and [COMPANY] with Turing

# problem 3
