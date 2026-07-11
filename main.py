import json 
import random
import string
from pathlib import Path

class Bank:
    database = 'info.json'
    info = []
    
    try:
        if Path(database).exists():
            with open(database) as fs: 
                info = json.load(fs) 
        else: 
            print("No Such File Exists ")
    except Exception as err:
        print(f"An exception occurred: {err}") 
    
    @staticmethod
    def update(): 
        with open(Bank.database, 'w') as fs: 
            json.dump(Bank.info, fs, indent=4)

    def _authenticate(self):
        try:
            acc_no = int(input("Enter Your Account Number : "))
            pin = int(input("Enter Your Pin : "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            return None
        
        for account in Bank.info:
            if account["accountNo."] == acc_no and account["pin"] == pin:
                return account
        
        print("Authentication Failed! Incorrect Account Number or Pin.")
        return None

    def Createaccount(self):
        info = {
            "name": input("Enter Your Full Name : "),
            "age": int(input("Enter Your Age : ")),
            "email": input("Enter Your Email Address : "),
            "pin": int(input("Enter Your Pin : ")),
            "accountNo.": random.randint(100000, 999999),
            "balance": 0
        }
        
        if info["age"] < 18 or len(str(info["pin"])) != 4: 
            print("Sorry You Are Not Eligible for Creating a Bank Account ")
        else: 
            Bank.info.append(info)
            print("\nAccount Created Successfully")
            print(f"Name : {info['name']}")
            print(f"Age : {info['age']}")
            print(f"Email : {info['email']}")
            print(f"Pin : {info['pin']}")
            print(f"Account Number : {info['accountNo.']}")
            print(f"Balance : {info['balance']}")
            
            print("Please Note Down Your Details Somewhere Safe\n")
            Bank.update()

    def deposit(self):
        account = self._authenticate()
        if account:
            try:
                amount = float(input("Enter Amount to Deposit : "))
                if amount > 0:
                    account["balance"] += amount
                    Bank.update()
                    print(f"Successfully deposited {amount}. New Balance: {account['balance']}")
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input.")

    def withdraw(self):
        account = self._authenticate()
        if account:
            try:
                amount = float(input("Enter Amount to Withdraw : "))
                if amount > 0:
                    if account["balance"] >= amount:
                        account["balance"] -= amount
                        Bank.update()
                        print(f"Successfully withdrew {amount}. New Balance: {account['balance']}")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input.")

    def check_details(self):
        account = self._authenticate()
        if account:
            print("\n--- Account Details ---")
            print(f"Name : {account['name']}")
            print(f"Age : {account['age']}")
            print(f"Email : {account['email']}")
            print(f"Pin : {account['pin']}")
            print(f"Account Number : {account['accountNo.']}")
            print(f"Balance : {account['balance']}")
            print("-----------------------\n")

    def update_details(self):
        account = self._authenticate()
        if account:
            print("\nLeave field blank if you do not want to update it.")
            name = input(f"Enter New Full Name [{account['name']}]: ")
            if name.strip():
                account["name"] = name
            
            age_str = input(f"Enter New Age [{account['age']}]: ")
            if age_str.strip():
                try:
                    age = int(age_str)
                    if age >= 18:
                        account["age"] = age
                    else:
                        print("Age must be 18 or above. Keeping old age.")
                except ValueError:
                    print("Invalid input. Keeping old age.")

            email = input(f"Enter New Email Address [{account['email']}]: ")
            if email.strip():
                account["email"] = email

            pin_str = input(f"Enter New Pin [{account['pin']}]: ")
            if pin_str.strip():
                try:
                    pin = int(pin_str)
                    if len(str(pin)) == 4:
                        account["pin"] = pin
                    else:
                        print("Pin must be 4 digits. Keeping old pin.")
                except ValueError:
                    print("Invalid input. Keeping old pin.")
            
            Bank.update()
            print("Account updated successfully!\n")

    def delete_account(self):
        account = self._authenticate()
        if account:
            confirm = input("Are you sure you want to delete this account? (y/n): ")
            if confirm.lower() == 'y':
                Bank.info.remove(account)
                Bank.update()
                print("Account deleted successfully.")
            else:
                print("Deletion cancelled.")

user = Bank() 

while True:
    print("\n--- Bank Management System ---")
    print("Press 1 for Creating an Account")
    print("Press 2 for Depositing Money in the Bank Account")
    print("Press 3 for Withdrawing Money from Bank Account")
    print("Press 4 for Checking details of Bank Account")
    print("Press 5 for Updating the details")
    print("Press 6 for Deleting the Account")
    print("Press 7 to Exit")
    
    try:
        check = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number.")
        continue

    if check == 1:
        print("\n--- Creating Account ---")
        user.Createaccount()

    elif check == 2:
        print("\n--- Depositing Money ---")
        user.deposit()

    elif check == 3:
        print("\n--- Withdrawing Money ---")
        user.withdraw()

    elif check == 4:
        print("\n--- Checking Details ---")
        user.check_details()

    elif check == 5:
        print("\n--- Updating Details ---")
        user.update_details()

    elif check == 6:
        print("\n--- Deleting Account ---")
        user.delete_account()

    elif check == 7:
        print("Exiting...")
        break

    else:
        print("Invalid Choice. Please try again.")