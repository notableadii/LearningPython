with open("CH-9/practice/log.txt") as f: 
    lines = f.readlines()
    

lineno = 1

for line in lines:
    if("Python" in line):
      print(f"Yes keyword is available. Line no: {lineno}")
      break
    lineno +=1
else:
    print("No keyword is not abvailable")