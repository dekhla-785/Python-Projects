import random

words = ["player","police","river","nature","camera","water"]
word =random.choice(words)

print(words)
# print(word)
userGuess =""
guess = 0
turns= 6

name = input("Enter Your name: ")
print("Welcome",name, "Have a good Game!!")

while(userGuess!=word):
    userGuess=input("Enter your guess: ")
    guess+=1
    if(userGuess==word):
        print("Your guess is correct")
    elif userGuess not in word:
          turns-=1
          print("Your guess is wrong!! Try Again")
          if turns==0:
           print("You lost the Game")
           break
    else:
        print("Done Well!!")
        
print(f"You have remain {turns} turns")
print(f"You have done guesses the word in {guess} guesses")
