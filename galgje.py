import os
import getpass

alphabet = list("abcdefghijklmnopqrstuvwxyz")

LIVES = 7
out_of_lives = False

gameWord = getpass.getpass('Give a word or sentence we should use:').lower()

gameWordList = list(gameWord)

def print_with_spaces(word):
    return ' '.join(word)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_lives():
    if LIVES == 0:
        out_of_lives = True
        draw_hangman()
        print("You're out of lives!")
        print("Do you want to play again?(Y/n)")
        exit()
    else:
        print(f'You have {LIVES} lives remaining.')

def draw_hangman():
    if LIVES == 7:
        print("  _______")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/|\\")
    elif LIVES == 6:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |")
        print(" |")
        print(" |")
        print("/|\\")
    elif LIVES == 5:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |       |")
        print(" |       |")
        print(" |")
        print("/|\\")
    elif LIVES == 4:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|")
        print(" |       |")
        print(" |")
        print("/|\\")
    elif LIVES == 3:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|/")
        print(" |       |")
        print(" |")
        print("/|\\")
    elif LIVES == 2:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / ")
        print("/|\\")
    elif LIVES == 1:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / \\")
        print("/|\\")
    elif LIVES == 0:
        print("  _______")
        print(" |/      |       ______ _____  ___ ______ ")
        print(" |       0       |  _  \  ___|/ _ \|  _  \\")
        print(" |      \\|/      | | | | |__ / /_\ \ | | |")
        print(" |       |       | | | |  __||  _  | | | |")
        print(" |      / \\      | |/ /| |___| | | | |/ / ")
        print("/|\\              |___/ \____/\_| |_/___/")

guessList = gameWordList[:]

for j in alphabet:
    for index, i in enumerate(guessList):
        if j in i:
            i1=i.replace(j,"_")
            guessList[index]= i1

found_a_letter = False
found_letter_already = False
found_letters = []
found_letter = ''

while out_of_lives == False:
    print(print_with_spaces(guessList))

    draw_hangman()

    print("Guess a letter:")
    guess = input()



    if len(guess) > 1:
        if guess == gameWord:
            clear()
            print(print_with_spaces(gameWord))
            draw_hangman()
            print("You found the word(s)!")
            break
        else:
            clear()
            print("Wrong!")
            LIVES = LIVES - 1
            check_lives()
    else:
        if found_letters != None:
            for index, letter in enumerate(gameWordList):
                if letter == guess and  guess not in found_letters:
                    found_a_letter = True
                    found_letter_already = False
                    found_letter = guess
                    i1=guessList[index] = guess
                    guessList[index]= i1
                elif guess in found_letters:
                    found_letter_already = True
        else:
            for index, letter in enumerate(gameWordList):
                if letter == guess:
                    found_a_letter = True
                    found_letter_already = False
                    found_letter = guess
                    i1=guessList[index] = guess
                    guessList[index]= i1
                elif guess in found_letters:
                    found_letter_already = True
        if not found_a_letter:
            clear()
            print("Wrong!")
            LIVES -= 1
            check_lives()
        elif found_letter_already == True:
            clear()
            print("Found this letter already!")
            LIVES -= 1
            check_lives()
        elif guessList == gameWordList:
            clear()
            print(print_with_spaces(guessList))
            draw_hangman()
            print("You found the word(s)!")
            break
        else:
            clear()
            print("Right!")
            found_letters.append(found_letter)
