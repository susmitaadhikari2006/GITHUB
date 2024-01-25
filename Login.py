import json

invalidInput = False
special_characters = "!@#$%^&*()-+?_=,<>/ "
Numbers = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnm"
#method to check password in the password
def checkPass(str):
    # if password contains a special character returns true
    if (any(c in special_characters for c in str) and any(a in Numbers for a in str) and any(b in letters for b in str) and any(d in letters.upper() for d in str)):
        return True
    else: 
        return False
#runs untill correct inputnis entered
#assumes incorrect input at first
n = 0
while((not invalidInput)  and (n<5)):
    username = input("Enter your username:").lower()#username is not case specific
    password = input("Enter your password:")
    if(username.__contains__(" ") or not checkPass(password)):# does the username contains spaces, If so -> LOOP
        print("Username or Password not formated correctly, Try Again:")
        invalidInput = False
    else:#meet requirements -> go to checking for if user and password match
        #PUT USER AND PASSWORD VALIDATION HERE
        invalidInput = True 
    n +=1
    if (n<=4):
        print("you used " +str(n) + " of 5 attempts")
    if(n==5):
        print("\n you have used all attempts! Please contact our customer service department for help at: \n 000-000-0000")
