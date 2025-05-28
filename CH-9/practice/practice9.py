with open("CH-9/practice/this.txt") as f:
    content1 = f.read()
    
with open("CH-9/practice/this_copy.txt") as f:
    content2 = f.read()
    
if(content1 == content2):
    print("Yes identical")
else:
    print("Not identical")