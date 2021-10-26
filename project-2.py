import random
randomNumber = random.randint(1,100)
userGuess = None
guesses = 0
# print(randomNumber)

while(userGuess != randomNumber):
    userGuess = int(input("Enter your Guess: "))
    guesses+= 1
    if(userGuess==randomNumber):
        print("You Guessed it correct")
    else:
        if(userGuess>randomNumber):
            print("Your Guess is wrong!! Enter a smaller number")
        else:
            print("Your Guess is wrong!! Enter a bigger number")

print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt","r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("You have just broken the record!!!")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))


