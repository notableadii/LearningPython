n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i == 0):
        print("Number is not prime")
        break  # break the loop when a factor is found
else:
    print("Number is prime")  # this else block executes if the loop completes without a break