import json
import csv
special_characters = "!@#$%^&*()-+?_=,<>/ ."
Numbers = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnm"
rows = []
file = open('user.csv')
type(file)
csvreader = csv.reader(file)
usernames = []
Passwords = []
for row in csvreader: #this is appending to the rows array form the csvFile
    rows.append(row)#returns a 2d array of (username,password)
for h in rows:
    usernames.append(h[0])#making a list of usernames
    Passwords.append(h[1])#making a list of passwords

def checkPass(str):
    # if password contains a special character returns true
    if (any(c in special_characters for c in str) and any(a in Numbers for a in str) and any(b in letters for b in str) and any(d in letters.upper() for d in str) and (len(str)>=8)):
        return True
    else: 
        return False
#assumes incorrect input at first
n = 0
invalidInput = True
while((invalidInput)  and (n<5)):
    username = input("Enter your username:").lower()#username is not case specific
    password = input("Enter your password:")
    for i in range(0, len(rows)):
        if ((usernames[i] == username) and (password[i]== password)):   
            invalidInput = True
        else:
            invalidInput = False 
    n +=1
    if (n<=4):
        print("you used " +str(n) + " of 5 attempts")
    if(n==5):
        print("\n you have used all attempts! Please contact our customer service department for help at: \n 000-000-0000")
