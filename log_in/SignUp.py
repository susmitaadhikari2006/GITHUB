import csv
from argon2 import PasswordHasher

invalidInput = False
special_characters = "!@#$%^&*()-+?_=,<>/ ."
Numbers = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnm"
ph = PasswordHasher()

def checkPass(str):
    # if password contains a special character returns true
    if (any(c in special_characters for c in str) and any(a in Numbers for a in str) and any(b in letters for b in str) and any(d in letters.upper() for d in str) and (len(str)>=8)):
        return True
    else: 
        return False
#runs untill correct input is entered
#assumes incorrect input at first
rows = []
file = open('user.csv')
type(file)
csvreader = csv.reader(file)
usernames = []
for row in csvreader: #this is appending to the rows array form the csvFile
    rows.append(row)
for h in rows:
    usernames.append(h[0])

while(not invalidInput):
    username = input("Enter your username:").lower()#username is not case specific
    password = input("Enter your password:")
    
    if(username.__contains__(" ") or not checkPass(password)):# does the username contains spaces, If so -> LOOP
        print("Username or Password not formated correctly, Try Again:")
        invalidInput = False
    elif(username in usernames):
        print("Username Already Exists")
        invalidInput = False
    else:
        info=(username +","+password)
        rows.append(info.split(",")) # adding the new username and password to the rows array, to use later
        with open('user.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)#updating the csv with the data in rows
        invalidInput = True