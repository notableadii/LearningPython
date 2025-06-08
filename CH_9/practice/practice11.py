with open("CH-9/practice/rename.txt", "r") as f:
    content = f.read()
    
with open("CH-9/practice/rename_done.txt", "w") as f:
    f.write(content)