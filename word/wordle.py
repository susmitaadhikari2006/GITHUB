Secret_word = "happy"

def get_guess():
    invalidInput = False
    while((not invalidInput)):
        letter = input("Enter your word(enter a letter):").lower() #not case specific
        if(len(letter)>1):
            invalidInput = False
            print("you entered more then one letter, Try Again")
        else:
            invalidInput = True
        n +=1
    return letter


invalidWord= False
i=0
while((not invalidWord) and (i<10)):
    input = get_guess()
    if (any(c in Secret_word for c in input)):
        print("this letter is in the word!")
    i+=1