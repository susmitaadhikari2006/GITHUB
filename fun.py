#There are 584 lines in the file
import random
import os
from colorama import Fore



#Pick a word and get the guess
wordList = []
for x in open("words.txt", "r"):
    wordList.append(x.strip())
word = wordList[random.randint(0,583)]
guess = ['hello','hello','hello','hello','hello']
print(word)
count = 0
colors = [["white","white","white","white","white"],
          ["white","white","white","white","white"],
          ["white","white","white","white","white"],
          ["white","white","white","white","white"],
          ["white","white","white","white","white"]]
while count <= 5:
    guess[count] = input("Guess a 5-letter word\n")
    if len(guess[count]) != 5:
        print("Please enter a 5-letter word.")
        continue
    if not guess[count].isalpha():
        print("Please enter a word with letters only.")
        continue
    
# Doesn't work because the wordlist is that great
  # if not guess[count] in wordList:
  #      print("Please enter a real word.")
  #     continue
        

    #Win State
    if(guess[count] == word):
        os.system('cls||clear')
        print(Fore.GREEN + str(count+1) + ". " + word)
        print(Fore.WHITE)
        exit()

    #Guesses

    # Guesses
    for i in range(0, 5):
        if guess[count][i] == word[i]:
            colors[count][i] = "green"
        else:
            for j in range(0, 5):
                if guess[count][j] == word[i] and colors[count][j] != "green":
                    colors[count][j] = "yellow"
                    break 

    os.system('cls||clear')
    for i in range(0,count+1):
        loc = 0 
        print(str(i + 1) + ".", end = "")
        for x in guess[i]:
            if(colors[i][loc]  == "green"):
                print(Fore.GREEN + x, end='')
            elif(colors[i][loc]  == "yellow"):
                print(Fore.YELLOW + x, end='')
            else:
                print(Fore.WHITE + x, end='') 
            loc += 1  
        print(Fore.WHITE) 
        print()

    count += 1

    if( count == 5):
        print("The correct word was " + Fore.GREEN + word + Fore.WHITE + ".")
        exit()