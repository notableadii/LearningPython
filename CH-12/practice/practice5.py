n = int(input("Enter a number: "))

table = [n * i for i in range(1, 11)]
with open("CH-12/practice/table.txt", "a") as f:
    f.write(f"Table of {n}:\n")
    for i in table:
        f.write(f"{i}\n")
print(f"Table of {n} has been written to table.txt")
