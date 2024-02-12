import random
import os
from colorama import Fore

wordList = []
for x in open("words.txt", "r"):
    wordList.append(x.strip())
Secret_word = wordList[random.randint(0,5753)]
print(Secret_word)
dashes = Secret_word
guesses_left = 5
    
def get_guess():
    invalidInput = False
    global guesses_left
    while((not invalidInput) and (guesses_left>0)):
        letter = input("Guess:").lower() #not case specific
        if(not len(letter)==5 or not letter.isalpha() or not letter in wordList):
            invalidInput = False
            print("Invalid Input, Please enter a 5 LETTER word")
        else:
            invalidInput = True
    return letter

def update_dashes(hidden_text, guessed_word):
    # dashes = "".join(x if x.lower() in guessed_word else "-" for x in hidden_text)
    # guess[count] = guessed_word
    return guessed_word

rightword = True
attempts = 0
while((rightword) and (guesses_left>0)):
    wordUser = get_guess()
    attempts =+ 1
    dashes = update_dashes(Secret_word, wordUser)
    print(str(attempts) + ". " + dashes)
    if(dashes == Secret_word):
        rightword = False
    elif(guesses_left==0):
        rightword = False
    guesses_left -= 1