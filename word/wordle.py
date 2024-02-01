Secret_word = "happy"
i=0
dashes = ""

# putting in dashes for each letter
for g in Secret_word:
    dashes += "-"

print(dashes)
    
def get_guess():
    global i
    invalidInput = False
    letters = "qwertyuiopasdfghjklzxcvbnm"
    while((not invalidInput) and i<10):
        letter = input("Enter your word(enter a letter):").lower() #not case specific
        if(len(letter)>1 or (not any(b in letters for b in letter))):
            invalidInput = False
            print("you entered more then one letter or a number, Try Again")
            i+=1
        else:
            invalidInput = True
    return letter

while((i<10)):
    wordUser = get_guess()
    if (any(c in Secret_word for c in wordUser)):
        print("this letter is in the word!\n")
        dashes += wordUser +"-"  
        print(dashes) 
    else:
        print("YOUR AN IDIOT, TRY AGAIN!")
        print(dashes)
    i+=1