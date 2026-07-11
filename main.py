import json 
import random
import string
from pathlib import Path

class Bank :
    def Createaccount(self):
        pass






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