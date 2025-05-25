# while loops

# while loops are used to repeat a block of code as long as a condition is true

# sourcery skip: while-to-for
i = 1  # initialize the counter variable

while(i<11):  # condition to check and this block will run as long as i is less than 11
    print(i)  # print the value of 
    i += 1  # increment the counter variable by 1
    
'''# Output: 
1
2
3
4
5
6
7
8
9
10

The above code will print the numbers from 1 to 10, one by one.

In while loops, the condition is checked first. If it evaluates to true, the body of the loop
is executed otherwise not!
If the loop is entered, the process of [condition check & execution] is continued until
the condition becomes False.

'''

i = 1  # re-initialize the counter variable

while(i<=50):
    print(i)  # print the value of i
    i += 1
    