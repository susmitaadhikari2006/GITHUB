import random
import os
from colorama import Fore, Style
print("\nYou have 6 sttempts best of luck:")

wordList = []
for x in open("words.txt", "r"):
    wordList.append(x.strip())
Secret_word = wordList[random.randint(0,5753)]
guesses_left = 6
    
def get_guess():
    invalidInput = False
    global guesses_left
    while((not invalidInput) and (guesses_left>0)):
        letter = input("Guess:").lower() #not case specific
        if(not len(letter)==5 or not letter.isalpha() or not letter in wordList):
            invalidInput = False
            print("not in the word list")
        else:
            invalidInput = True
    return letter

def update_dashes(hidden_text, guessed_word):
    word = ""
    Secret = hidden_text
    string_list = list(Secret)
    for i in range(len(Secret)):
        if guessed_word[i] == Secret[i]:
            word += Fore.GREEN + guessed_word[i] + Style.RESET_ALL
            idx = Secret.index(guessed_word[i])
            string_list[idx] = "!"
            Secret = ''.join(string_list)
        elif guessed_word[i] in Secret:
            word += Fore.YELLOW + guessed_word[i] + Style.RESET_ALL
            idx = Secret.index(guessed_word[i])
            string_list[idx] = "!"
            Secret = ''.join(string_list)
        else:
            word += guessed_word[i]
    return word

rightword = True
attempts = 0
while((rightword) and guesses_left > 0):
    wordUser = get_guess()
    attempts += 1
    if(wordUser == Secret_word):
        rightword = False
    if(guesses_left==0):
        rightword = True
    dashes = update_dashes(Secret_word, wordUser)
    print(str(attempts) + ". " + dashes)

if guesses_left == 0:
    print("word was: " + Fore.GREEN + Secret_word + Style.RESET_ALL)