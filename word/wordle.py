Secret_word = "happy"

def get_guess():
    invalidInput = False
    letters = "qwertyuiopasdfghjklzxcvbnm"
    while((not invalidInput)):
        letter = input("Enter your word(enter a letter):").lower() #not case specific
        if(len(letter)>1 or (not any(b in letters for b in letter))):
            invalidInput = False
            print("you entered more then one letter or a number, Try Again")
        else:
            invalidInput = True
    return letter

invalidWord= False
i=0
while((not invalidWord) and (i<10)):
    wordUser = get_guess()
    if (any(c in Secret_word for c in wordUser)):
        print("this letter is in the word!")
    else:
        print("YOUR AN IDIOT, TRY AGAIN!")
    i+=1