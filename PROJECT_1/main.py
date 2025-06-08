"""
This is the rules comment - it tells us what each number means:
1 for snake
-1 for water
0 for gun
"""

# Import the random module - this is like a magic box that gives us random numbers
# We need this so the computer can make random choices
import random

# Make the computer choose randomly between 1, -1, or 0
# random.choice() picks one item from the list [1, -1, 0]
# It's like putting three pieces of paper in a hat and picking one blindly
computer = random.choice([1, -1, 0])

# Create a dictionary (like a translator book) that converts letters to numbers
# When player types 's', it means 1 (snake)
# When player types 'w', it means -1 (water)
# When player types 'g', it means 0 (gun)
youDict = {"s": 1, "w": -1, "g": 0}

# Create another dictionary that does the opposite - converts numbers back to words
# This is so we can show the player what they chose in a nice way
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}


# Function to get valid input from the player
def get_player_choice():
    while True:
        print("\nEnter your choice:")
        print("s - Snake")
        print("w - Water")
        print("g - Gun")
        youstr = input("Your choice: ").lower().strip()

        if youstr in youDict:
            return youstr
        else:
            print(
                "Invalid choice! Please enter 's' for Snake, 'w' for Water, or 'g' for Gun."
            )


# Get the player's choice
youstr = get_player_choice()

# Use the dictionary to translate the player's letter choice into a number
you = youDict[youstr]

# Print what both the player and computer chose
print(f"\nYou chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# Now we check who wins! This is like a big decision tree
# == means "is equal to" (checking if two things are the same)

# First, check if it's a tie (both chose the same thing)
if computer == you:
    print("It's a tie!")

# Check if computer chose water (-1) AND player chose snake (1)
# In this game: Snake drinks water, so snake wins!
elif computer == -1 and you == 1:
    print("You win!")

# Check if computer chose snake (1) AND player chose gun (0)
# In this game: Gun shoots snake, so gun wins! (Computer wins)
elif computer == 1 and you == 0:
    print("You lose!")

# Check if computer chose snake (1) AND player chose water (-1)
# In this game: Snake drinks water, so snake wins! (Computer wins)
elif computer == 1 and you == -1:
    print("You lose!")

# Check if computer chose gun (0) AND player chose water (-1)
# In this game: Water drowns gun, so water wins! (Player wins)
elif computer == 0 and you == -1:
    print("You Win!")

# Check if computer chose gun (0) AND player chose snake (1)
# In this game: Gun shoots snake, so gun wins! (Computer wins)
elif computer == 0 and you == 1:
    print("You Lose!")

# Check if computer chose water (-1) AND player chose gun (0)
# In this game: Water drowns gun, so water wins! (Computer wins)
elif computer == -1 and you == 0:
    print("You Lose!")

# This is a safety net - if somehow none of the above conditions are true
# This should never happen, but it's good practice to have a backup plan
else:
    print("Something went wrong!")
