words = ["Python", "Lorem", "doloribus"]

for word in words:
    content = word
with open("CH-9/practice/log.txt", "r") as f: 
    content = f.read()
    

    
if(word in content):
    print("Yes keywords are available")
else:
    print("No keywords are not abvailable")