import csv
from pyargon2 import hash
import string
import random
"""variables"""
salt = "" #new salt
pepper = "" #new pepper
special_characters = "!@#$%^&*()-+?_=,<>/ ." #String of Special Characters
Numbers = "1234567890" #String of Numbers  
letters = "qwertyuiopasdfghjklzxcvbnm" #String of letters
indexForNewPass = 0 #setting the Index initially to 0
rows = [] #this is the 2D array of information (username,password,salt,pepper)
usernames = [] #list for usernames
passwords = [] #list of hashed Passwords
salts = [] #list of salts used
peppers = [] #list of peppers used
userInfo = []
UserUsername = []
UserPassword = []


"""opening the CSV file and getting information"""
file = open('hashed.csv')
type(file)
csvreader = csv.reader(file)
for row in csvreader: #this is appending to the rows array form the csvFile
    rows.append(row)#returns a 2d array of (username,password,salt,pepper)
for h in rows:
    usernames.append(h[0])#making a list of usernames
    passwords.append(h[1])#making a list of passwords
    salts.append(h[2])#making a list of salts
    peppers.append(h[3])#Making a list of peppers

Userfile = open('user.csv')
type(Userfile)
csvreaderUser = csv.reader(Userfile)
for row in csvreaderUser: #this is appending to the rows array form the csvFile
    userInfo.append(row)#returns a 2d array of (username,password,salt,pepper)
for h in rows:
    UserUsername.append(h[0])#making a list of usernames
    UserPassword.append(h[1])#making a list of passwords Unhashed

"""methods"""
#method to check if the passed in password meets the requirements -> returns a boolean
def checkPass(str):
    # if password contains a special character returns true
    if (any(c in special_characters for c in str) and any(a in Numbers for a in str) and any(b in letters for b in str) and any(d in letters.upper() for d in str) and (len(str)>=8)):
        return True
    else: 
        return False
    
#a method to create a string of random characters
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#assumes incorrect input at first
n = 0 # increases as their attempts increase
invalidInput = True #assumes invalid input at first
signin = False # false until they sign in
while((invalidInput) and (n<5)): #runs until they able to sign in AND until they have reached 5 attempts
    print("LOGIN:\n")
    username = input("Enter your username:").lower()#username is not case specific
    password = input("Enter your password:")
    for i in range(len(rows)):
        if ((usernames[i]==username) and (passwords[i] == hash(hash(hash(password, salts[i]), salts[i]), salts[i], peppers[i]))):#checks if the given password matches
            print("Log In success!")
            indexForNewPass = i #sets the new index for the user in the data
            invalidInput = False #gets out of the loop
            signin = True #the user have successfully signed in
            break #to go to the next step
        else:
            invalidInput = True#if log in fails try again! until 5 times
    n +=1 # increments until 5
    if (n<=4):
        print("you used " +str(n) + " of 5 attempts")
    if(n==5):
        print("you have used all attempts! Please contact our customer service department for help at: \n 000-000-0000")
        

"""The user has succesfuly signed in"""
while(signin):
    change = input("do you want to change your password? y/n: \n To sign out enter q: ").lower() # the 'y' or 'n' is not case specific
    if(change == "y"):
        oldPass = input("please enter your old password:") # having the user enter their old password
        if(hash(hash(hash(oldPass, salts[indexForNewPass]), salts[indexForNewPass]), salts[indexForNewPass], peppers[indexForNewPass]) == passwords[indexForNewPass]):
            newPass = input("please enter your new password:") #asking user for their new password
            if(checkPass(newPass)): #if the new password meets requirements
                #creating a new salt and pepper
                salt = id_generator()
                pepper = id_generator()
                #adding the new salt an pepper to the 2D list of everything
                rows[indexForNewPass][1] = hash(hash(hash(newPass, salt), salt), salt, pepper)
                rows[indexForNewPass][2] = salt
                rows[indexForNewPass][3] = pepper
                userInfo[indexForNewPass][1] = newPass
                #updating the new information the already exiting CSV file
                with open('hashed.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                with open('user.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(userInfo)
        signin = True
    elif(change == "n"):
        signin = True
        
    #exiting the program if the user wants to do so
    elif(change == "q"):
        signin = False
    else:
        print("Please enter valid information \n")
        signin = True #if user enters incorrect value stay signed in and ask again