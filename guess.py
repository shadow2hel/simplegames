import random
import sys

randomNumber = random.randrange(0,100)

while(True):
    print("Guess the number:")
    try:
        guessNumber = int(input())
    except:
        print("That's not a number!")
        continue

    if guessNumber > randomNumber:
        print("Lower!")
    elif guessNumber < randomNumber:
        print("Higher!")
    elif guessNumber == randomNumber:
        print("You guessed it!")
        print("Wanna play again?(y/n)")
        answer = input().lower()
        if answer == "y":
            print("Here we go!")
            randomNumber = random.randrange(0, 100)
            continue
        elif answer == "n":
            print("Aww, you suck..")
            break
