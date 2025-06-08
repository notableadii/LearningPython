def GoodDay(name, ending): #here name is a parameter of the function GoodDay
    print("Good day " + name)
    print(ending)
    return "done" # this function returns the string "done"

a = GoodDay("Aditya", "Thank you") # this is how we call a function with an argument
print(a) # this will print None because the function GoodDay does not return anything