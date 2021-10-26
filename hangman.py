import random

with open("wordlist.txt","r") as f:
    words = f.readlines()

word = random.choice(words)[:-1]
#print(word)
errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in word:
            print(letter,end=" ")
        else:
            print("_",end=" ")
        print("")

    guess = input(f"Remaing errors are {errors}, Please enter new word: ")
    guesses.append(guess.lower())
    if guess.lower() in word:
        errors -= 1
    if errors ==0:
       break

done = True
for letter in word:
    if letter.lower() not in guesses:
        done = False

if done:
    print("You found the word Finally!! It was",word)
else:
    print("Game over!! The word was",word)
