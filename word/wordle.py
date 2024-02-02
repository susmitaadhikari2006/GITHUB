Secret_word = "software"
i=0
dashes = ""

# putting in dashes for each letter
for g in Secret_word:
    dashes += "-"

print(dashes)
def update_dashes(hidden_text, guessed_letters):
    dashes = "".join(x if x.lower() in guessed_letters else "-" for x in hidden_text)
    return dashes
        
def get_guess():
    global i
    invalidInput = False
    letters = "qwertyuiopasdfghjklzxcvbnm"
    while((not invalidInput) and i<10):
        letter = input("Guess:").lower() #not case specific
        if(len(letter)>1 or (not any(b in letters for b in letter))):
            invalidInput = False
            print("you entered more then one letter or a number, Try Again")
            i+=1
        else:
            invalidInput = True
    return letter

guessed_letters = {""}
while((i<10)):
    wordUser = get_guess()
    if (any(c in Secret_word for c in wordUser)):
        print("this letter is in the word!\n")
        guessed_letters.add(wordUser)
        print(update_dashes(Secret_word, guessed_letters))
    else:
        print("YOUR AN IDIOT, TRY AGAIN!")
        print(dashes)
    i+=1
    if i==10:
        print("The Word was: " + Secret_word)