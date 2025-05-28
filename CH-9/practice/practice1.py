f = open("CH-9/practice/poem.txt", "r")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present in then content")
else:
    print("its not present")
f.close