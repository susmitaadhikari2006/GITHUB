from colorama import Fore
import random

wordList = []
for x in open("words.txt", "r"):
    wordList.append(x.strip())
Secret_word = wordList[random.randint(0,5753)]
dashes = ""
guesses_left = 10

# putting in dashes for each letter
for g in Secret_word:
    dashes += "-"

print(dashes)
def update_dashes(hidden_text, guessed_letters):
    dashes = "".join(x if x.lower() in guessed_letters else "-" for x in hidden_text)
    return dashes
        
def get_guess():
    invalidInput = False
    global guesses_left
    letters = "qwertyuiopasdfghjklzxcvbnm"
    while((not invalidInput) and (not guesses_left==0)):
        letter = input("Guess:").lower() #not case specific
        if(len(letter)>1 or (not any(b in letters for b in letter))):
            invalidInput = False
            print("you entered more then one letter or a number, Try Again")
            guesses_left -= 1
            print(str(guesses_left) + " incorrect guesses left.")
        else:
            invalidInput = True
    return letter

guessed_letters = {""}
rightword = True
while((rightword) and (guesses_left>0)):
    wordUser = get_guess()
    if (any(c in Secret_word for c in wordUser)):
        print("this letter is in the word!\n")
        guessed_letters.add(wordUser)
        dashes = update_dashes(Secret_word, guessed_letters)
        print(dashes)
        if(dashes == Secret_word):
            rightword = False   
    else:
        print("YOUR AN IDIOT, TRY AGAIN!")
        guesses_left -= 1
        print(update_dashes(Secret_word, guessed_letters))
    print(str(guesses_left) + " incorrect guesses left.")
if(guesses_left == 0):
    print("you lost The word was: "+ Secret_word)
else:
    print("Congrats! You win. The word was: " + Secret_word)