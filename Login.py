import json
users = []
passWrd =[]

with open('users.json', 'r') as file:
    # Load JSON data from file
    data = json.load(file)

def getUser(datas):
    for i in datas["username"]:
        users.append(i)
    return users
def getPass(datas):
    for i in datas["password"]:
        passWrd.append(i)
    return passWrd

print(users)
print(passWrd)

# Closing file
invalidInput = False
special_characters = "!@#$%^&*()-+?_=,<>/ "
Numbers = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnm"
#method to check password in the password
print(getUser(data))
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
    else:
        invalidInput = True 
    n +=1
    if (n<=4):
        print("you used " +str(n) + " of 5 attempts")
    if(n==5):
        print("\n you have used all attempts! Please contact our customer service department for help at: \n 000-000-0000")
