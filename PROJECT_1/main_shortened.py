'''
Snake Water Gun Game - Mathematical Logic Version
1 for snake
-1 for water
0 for gun

The secret math pattern:
- If (you - computer) = 1 or -2, YOU WIN!
- If (you - computer) = -1 or 2, YOU LOSE!
- If (you - computer) = 0, IT'S A TIE!
'''

import random

# Computer makes a random choice
computer = random.choice([1, -1, 0])

# Get player's choice
youstr = input("Enter your choice (s/w/g): ")

# Convert player's choice to number
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]

# Convert numbers back to names for display
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# HERE'S THE MAGIC! 🎩✨
# Calculate the difference between your choice and computer's choice
difference = you - computer

print(f"Math magic: {you} - {computer} = {difference}")

# Use the mathematical pattern to determine winner
if difference == 0:
    print("It's a tie! 🤝")
elif difference == 2 or difference == -1:
    print("You win! 🎉")
elif difference == 1 or difference == -2:
    print("You lose! 😅")
else:
    print("Something went wrong!")

'''
WHY THIS WORKS - The Mathematical Secret! 🧮

Here are ALL possible combinations and their math:

YOU WIN when difference = 2 or -1:
- Snake(1) - Water(-1) = 2 → You win! (Snake drinks water)
- Water(-1) - Gun(0) = -1 → You win! (Water drowns gun)  
- Gun(0) - Snake(1) = -1 → You win! (Gun shoots snake)

YOU LOSE when difference = 1 or -2:
- Snake(1) - Gun(0) = 1 → You lose! (Gun shoots snake)
- Gun(0) - Water(-1) = 1 → You lose! (Water drowns gun)
- Water(-1) - Snake(1) = -2 → You lose! (Snake drinks water)

TIE when difference = 0:
- Same choice = 0 → It's a tie!

The pattern: Win differences are [2, -1], Lose differences are [1, -2]
This replaces 6+ if-elif statements with just 3! 🔥
'''