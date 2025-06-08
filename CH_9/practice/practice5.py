words = ["Donkey", "bad"] # replacing using list 

with open("CH-9/practice/ceonsor.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(words))
    print(word, type(word)) # because for loop converts the list items from list to str

with open("CH-9/practice/ceonsor.txt", "w") as f:
    f.write(content)
    
