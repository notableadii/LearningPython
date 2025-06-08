from icecream import ic
import pyjokes
from time import sleep #these are modules which are codes written by someone else

#pip is a package manager for python 
# pip install pyjokes
# pip install icecream
# pip install time


"""This is a multi-line comment
Comments are used to explain the code"""
# this is a single line comment

ic("Importing Jokes....")
sleep(2)
jokes = pyjokes.get_joke(language="en") 
ic(jokes)
sleep(1)
variable = '''Multi line string
Line 2'''
ic(variable)

# print("Hellow World")