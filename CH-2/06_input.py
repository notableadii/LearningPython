from time import sleep
# from icecream import ic
# input() function is used to take input from the user
from colorama import Fore, Back, Style

print(Fore.RED +
    '''
 /$$$$$$ /$$   /$$ /$$$$$$$  /$$   /$$ /$$$$$$$$      
|_  $$_/| $$$ | $$| $$__  $$| $$  | $$|__  $$__/      
  | $$  | $$$$| $$| $$  \ $$| $$  | $$   | $$         
  | $$  | $$ $$ $$| $$$$$$$/| $$  | $$   | $$         
  | $$  | $$  $$$$| $$____/ | $$  | $$   | $$         
  | $$  | $$\  $$$| $$      | $$  | $$   | $$         
 /$$$$$$| $$ \  $$| $$      |  $$$$$$/   | $$         
|______/|__/  \__/|__/       \______/    |__/                                                                                        
'''
)
sleep(2)

a = input(Fore.BLUE + Style.BRIGHT + "Enter a number: ") # a is a string
b = input(Fore.BLUE + Style.BRIGHT + "Enter a number: ") # b is a string
print(" ") #space
print(Fore.WHITE +"Number a = ", a) # Input of the user is taken as a string
print(Fore.WHITE +"Number b = ", b) # Input of the user is taken as a string
print(" ") #space

print(Fore.CYAN +"Sum of a and b = ", a + b) # and b are strings so they will be concatenated
print(" ") #space

print(Fore.YELLOW +"Type of a = ", type(a)) # <class 'str'> because a is a string
print(Fore.YELLOW + "Type of b = ", type(b)) # <class 'str'> because b is a string
print(" ") #space

# after taking input from the user we need to convert the string to an integer

c = int(a) # a is converted to an integer
d = int(b) # b is converted to an integer

print(Fore.YELLOW + "Type of a after converting = ", type(c)) # <class 'str'> because a is a string
print(Fore.YELLOW + "Type of b after converting = ", type(d)) # <class 'str'> because b is a string
print(" ") #space

print(Fore.CYAN + "Sum of a and b = ", c + d) # sum of a and b
print(" ") #space

# an easier and direct way to convert a string to an integer is to use the eval function

print(Fore.CYAN + "Sum of a and b after using evaluate funciton = ", eval(a) + eval(b)) # sum of a and b
print(" ") #space

# eval function is used to evaluate a string as a python expression

# another way to convert a string to an integer is directly take input from the user as an integer

e = int(input(Fore.BLUE + Style.BRIGHT + "Enter a number: ")) # a is an integer
f = int(input(Fore.BLUE + Style.BRIGHT + "Enter a number: ")) # b is an integer

print(Fore.CYAN + "Sum of e and f = ", e + f) # sum of e and f
print(" ") #space

print(Fore.YELLOW + "Type of e = ", type(e)) # <class 'int'> because e is an integer
print(" ") #space


print(Fore.YELLOW + "Type of f = ", type(f)) # <class 'int'> because f is an integer
sleep(2)
print(" ") #space

print(Fore.RED + Style.NORMAL +
    '''
    Closing the program in 3 seconds...
    ''')
sleep(3)
print(" ") #space

print(Fore.RED + Style.NORMAL + '''
██╗ ██████╗██╗   ██╗
██║██╔════╝╚██╗ ██╔╝
██║██║      ╚████╔╝ 
██║██║       ╚██╔╝  
██║╚██████╗   ██║   
╚═╝ ╚═════╝   ╚═╝   
    ''')

sleep(2)