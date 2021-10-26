import random

randomNum = random.randint(1,9)
userguess = None
guesses = 0

while(userguess != randomNum):
    userguess = int(input("Enter your Guess: "))
    guesses+=1
    if(userguess == randomNum):
        print("You guessesd it correct")
    else:
        if(userguess>randomNum):
            print("Please enter smaller number")
        else:
            print("Please enter Bigger number")

with open("highscore.txt","r") as f:
    score = f.read()

with open("highscore.txt","w") as f:
    f.write(score)

print(f"You have gueesed the number in {guesses} guesses")