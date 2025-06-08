with open("CH-9/practice/this.txt") as f:
    content = f.read()
    
with open("CH-9/practice/this_copy.txt", "w") as f:
    f.write(content)