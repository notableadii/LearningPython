from random import randint

n = randint(1, 100)
a =-1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Guess a number: "))
    if(a>n):
        print("Too high!")
    else:
        print("Too low!")
print(f"Congratulations! You've guessed the number {n} in {guesses} attempts.")
# This code implements a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.




# class PerfectGuess:
#     def __init__(self):
#         self.number_to_guess = randint(1, 100)
#         self.attempts = 0

#     def guess(self, user_guess):
#         self.attempts += 1
#         if user_guess < self.number_to_guess:
#             return "Too low!"
#         elif user_guess > self.number_to_guess:
#             return "Too high!"
#         else:
#             return f"Congratulations! You've guessed the number {self.number_to_guess} in {self.attempts} attempts."
#     def reset_game(self):
#         self.number_to_guess = randint(1, 100)
#         self.attempts = 0
#         return "Game reset! A new number has been generated."

# # Example usage
# if __name__ == "__main__":
#     game = PerfectGuess()
#     while True:
#         try:
#             user_input = input("Enter your guess (or type 'reset' to start a new game): ")
#             if user_input.lower() == 'reset':
#                 print(game.reset_game())
#                 continue
#             guess = int(user_input)
#             result = game.guess(guess)
#             print(result)
#             if "Congratulations" in result:
#                 break
#         except ValueError:
#             print("Please enter a valid number.")
#         except KeyboardInterrupt:
#             print("\nGame interrupted. Exiting...")
#         except Exception as e:
#             print(f"An error occurred: {e}. Please try again.")
# # The code implements a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.
