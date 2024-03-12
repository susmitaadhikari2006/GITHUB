import csv
from pyargon2 import hash
import string
import random
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#variables
salt = ""
pepper = ""
special_characters = "!@#$%^&*()-+?_=,<>/ ."
Numbers = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnm"
indexForNewPass = 0
rows = []
file = open('hashed.csv')
type(file)
csvreader = csv.reader(file)
usernames = []
passwords = []
salts = []
peppers = []
for row in csvreader: #this is appending to the rows array form the csvFile
    rows.append(row)#returns a 2d array of (username,password)
for h in rows:
    usernames.append(h[0])#making a list of usernames
    passwords.append(h[1])#making a list of passwords
    salts.append(h[2])
    peppers.append(h[3])
def checkPass(str):
    # if password contains a special character returns true
    if (any(c in special_characters for c in str) and any(a in Numbers for a in str) and any(b in letters for b in str) and any(d in letters.upper() for d in str) and (len(str)>=8)):
        return True
    else: 
        return False
#assumes incorrect input at first
n = 0
invalidInput = True
signin = False # false untill they sign in
while((invalidInput) and (n<5)):
    print("LOGIN:\n")
    username = input("Enter your username:").lower()#username is not case specific
    password = input("Enter your password:")
    for i in range(len(rows)):
        if ((usernames[i]==username) and (passwords[i] == hash(hash(hash(password, salts[i]), salts[i]), salts[i], peppers[i]))): 
            print("Log In success!") 
            indexForNewPass = i
            invalidInput = False
            signin = True
            break
        else:
            invalidInput = True 
    n +=1
    if (n<=4):
        print("you used " +str(n) + " of 5 attempts")
    if(n==5):
        print("you have used all attempts! Please contact our customer service department for help at: \n 000-000-0000")
while(signin):
    change = input("do you want to change your password? y/n: \n To sign out enter q: ").lower() # the 'y' or 'n' is not case specific
    if(change == "y"):
        oldPass = input("please enter your old password:") # having the user enter their old password
        if(hash(hash(hash(oldPass, salts[indexForNewPass]), salts[indexForNewPass]), salts[indexForNewPass], peppers[indexForNewPass]) == passwords[indexForNewPass]):
            newPass = input("please enter your new password:")
            if(checkPass(newPass)):
                salt = id_generator()
                pepper = id_generator()
                rows[indexForNewPass][1] = hash(hash(hash(newPass, salt), salt), salt, pepper)
                rows[indexForNewPass][2] = salt
                rows[indexForNewPass][3] = pepper
                with open('hashed.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)#updating the csv with the data in
        signin = True
    elif(change == "n"):
        signin = True
    elif(change == "q"):
        signin = False
    else:
        signin = True
    