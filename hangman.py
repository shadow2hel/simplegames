import os
import getpass

def print_with_spaces(word):
    return ' '.join(word)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    LIVES = 7
    out_of_lives = False
    gameWord = ''
    gameWordList = list(gameWord)
    guessList = gameWordList[:]
    found_a_letter = False
    found_letter_already = False
    found_letters = []
    found_letter = ''

galgje = Game()

def initialize_game():

    galgje.LIVES = 7
    galgje.out_of_lives = False
    galgje.gameWord = getpass.getpass('Give a word or sentence we should use:').lower()
    galgje.found_a_letter = False
    galgje.found_letter_already = False
    galgje.found_letters = []
    galgje.found_letter = ''

    galgje.gameWordList = list(galgje.gameWord)

    galgje.guessList = galgje.gameWordList[:]

    for j in galgje.alphabet:
        for index, i in enumerate(galgje.guessList):
            if j in i:
                i1 = i.replace(j, "_")
                galgje.guessList[index] = i1

    play()

def play():
    while galgje.out_of_lives == False:
        print(print_with_spaces(galgje.guessList))

        draw_hangman()

        print("Guess a letter:")
        guess = input()

        if len(guess) > 1:
            if guess == galgje.gameWord:
                clear()
                print(print_with_spaces(galgje.gameWord))
                draw_hangman()
                print("You found the word(s)!")
                replay()
                break
            else:
                clear()
                print("Wrong!")
                galgje.LIVES = galgje.LIVES - 1
                check_lives()
        else:
            if galgje.found_letters != None:
                for index, letter in enumerate(galgje.gameWordList):
                    if letter == guess and guess not in galgje.found_letters:
                        galgje.found_a_letter = True
                        galgje.found_letter_already = False
                        galgje.found_letter = guess
                        i1 = galgje.guessList[index] = guess
                        galgje.guessList[index] = i1
                    elif guess in galgje.found_letters:
                        galgje.found_letter_already = True
            else:
                for index, letter in enumerate(galgje.gameWordList):
                    if letter == guess:
                        galgje.found_a_letter = True
                        galgje.found_letter_already = False
                        galgje.found_letter = guess
                        i1 = galgje.guessList[index] = guess
                        galgje.guessList[index] = i1
                    elif guess in galgje.found_letters:
                        galgje.found_letter_already = True
            if not galgje.found_a_letter:
                clear()
                print("Wrong!")
                galgje.LIVES -= 1
                check_lives()
            elif galgje.found_letter_already == True:
                clear()
                print("Found this letter already!")
                galgje.LIVES -= 1
                check_lives()
            elif galgje.guessList == galgje.gameWordList:
                clear()
                print(print_with_spaces(galgje.guessList))
                draw_hangman()
                print("You found the word(s)!")
                replay()
                break
            else:
                clear()
                print("Right!")
                galgje.found_letters.append(galgje.found_letter)

def check_lives():
    if galgje.LIVES == 0:
        galgje.out_of_lives = True
        draw_hangman()
        print("You're out of lives!")
        replay()
    else:
        print(f'You have {galgje.LIVES} lives remaining.')

def replay():
    print("Do you want to play again?(Y/n)")
    answer = input().lower()
    if answer == "y":
        initialize_game()
    elif answer == "n":
        exit()
    else:
        print("You didn't answer correctly!")
        replay()



def draw_hangman():
    if galgje.LIVES == 7:
        print("  _______")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/|\\")
    elif galgje.LIVES == 6:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |")
        print(" |")
        print(" |")
        print("/|\\")
    elif galgje.LIVES == 5:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |       |")
        print(" |       |")
        print(" |")
        print("/|\\")
    elif galgje.LIVES == 4:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|")
        print(" |       |")
        print(" |")
        print("/|\\")
    elif galgje.LIVES == 3:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|/")
        print(" |       |")
        print(" |")
        print("/|\\")
    elif galgje.LIVES == 2:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / ")
        print("/|\\")
    elif galgje.LIVES == 1:
        print("  _______")
        print(" |/      |")
        print(" |       0")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / \\")
        print("/|\\")
    elif galgje.LIVES == 0:
        print("  _______")
        print(" |/      |       ______ _____  ___ ______ ")
        print(" |       0       |  _  \  ___|/ _ \|  _  \\")
        print(" |      \\|/      | | | | |__ / /_\ \ | | |")
        print(" |       |       | | | |  __||  _  | | | |")
        print(" |      / \\      | |/ /| |___| | | | |/ / ")
        print("/|\\              |___/ \____/\_| |_/___/")

initialize_game()