import json 
import random
import string
from pathlib import Path

class Bank :
    database = 'info.json'
    info = []
    
    try:
        if Path(database).exists():
            with open(database) as fs: 
                info = json.load(fs) 
        else: 
            print("No Such File Exists ")


    except Exception as err:
        print("an exception accured as {err}") 
    
    @staticmethod
    def update(): 

        with open(Bank.database, 'w') as fs: 
            json.dump(Bank.info, fs)



    def Createaccount(self):
      info = {
        "name": input("Enter Your Full Name : "),
        "age": int(input("Enter Your Age : ")),
        "email": input("Enter Your Email Address : "),
        "pin": int(input("Enter Your Pin : ")),
        "accountNo." : 1234,
        "balance" : 0
        
      }
      if info["age"] < 18 or len(str(info["pin"])) != 4 : 
        print("Sorry You Are Not Elgible for Creating a Bank Account ")
      else: 
        Bank.info.append(info)
        print("Account Created Successfully")
        print(f"Name : {info['name']}")
        print(f"Age : {info['age']}")
        print(f"Email : {info['email']}")
        print(f"Pin : {info['pin']}")
        print(f"Account Number : {info['accountNo.']}")
        print(f"Balance : {info['balance']}")
        
        print("Please NoteDown Your Details Somewhere Safe")
        Bank.update()






user = Bank() 






print("Press 1 for Creating an Account")
print("Press 2 for Depositing Money in the Bank Account")
print("Press 3 for Withdrawing Money from Bank Account")
print("Press 4 for Checking details of Bank Account")
print("Press 5 for Updating the details")
print("Press 6 for Deleting the Account")

check = int(input("Enter your choice: "))

if check == 1:
    print("Creating Account")
    user.Createaccount()

elif check == 2:
    print("Depositing Money")
elif check == 3:
    print("Withdrawing Money")
elif check == 4:
    print("Checking Details")
elif check == 5:
    print("Updating Details")
elif check == 6:
    print("Deleting Account")
else:
    print("Invalid Choice")