import random


def game():
    print("Your playing a game....")
    score = random.randint(1,62)
    #Fetch the highscore
    with open("CH-9/practice/high-score.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your score {score}")
    if(score>highscore):
        #write this highscore on the file
            with open("CH-9/practice/high-score.txt", "w") as f:
                f.write(str(score))
                

    return score

game()