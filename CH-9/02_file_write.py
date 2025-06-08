st = "Hey, I'm a string"

f = open("CH-9/Myfile.txt", "w") # w is for write mode
f.write(st) # write the string to the file
f.close() # close the file

f = open("CH-9/Myfile.txt", "r") # r is for read mode
data = f.read() # read the file
print(data) # print the file
f.close() # close the file


