import os
import json

# Initial Directories

if not os.path.exists("Accounts"):
    os.mkdir("Accounts")

# File Path Checking in Directory

def checking_file_exist(filepath):
    print(filepath)
    try:
        os.path.exists(filepath)
    except FileNotFoundError:
        with open(f"{filepath}", "w") as f:
            f.write("0")

# Account Creation

def account_generate(filepath, name, passcode=0000,):

    account_info = {"bank" : "Sadaat Bank Limited", "name": name, "pass_code": passcode, "balance": 0, "history" : [] }

    if os.path.exists(filepath):
        print("You already Have Account, Login to your Account")
    else:
        os.mkdir(filepath)
        print(f"Account Sucessfully Created")
    with open(f"{filepath}/{name}_info.json", "w") as f:
        json.dump(account_info, f)

# Account Verfication

def verify_account(name, passcode):
    if os.path.exists(f"Accounts/{name}/{name}_info.json"):
        with open(f"Accounts/{name}/{name}_info.json", "r") as f:
            account_info = json.load(f)
            if account_info["pass_code"] == passcode:
                return True
            else:
                print("Invalid Passcode")
                return False
    else:
        print(f"Hi {name}, You are not a Sadaat Bank Limited User.")
        return False

class online_banking:
    bankname = "Sadaat Bank Limited"

    def __init__(self, name, balance=0):
        self.account_holder = name
        self.user_info_path = f"Accounts/{self.account_holder}/{self.account_holder}_info.json"
        with open(self.user_info_path, "r") as f:
            user_account_info = json.load(f)

        self.balance = user_account_info["balance"]

        print(f"Your Current Balance is {self.balance}")

        with open(self.user_info_path, "r") as f:
            account_info = json.load(f)
        self.account_info = account_info

    # Deposit Functionality

    def deposit(self, amount):
        self.balance += amount
        
        self.account_info["balance"] = self.balance
        with open(self.user_info_path, "w") as f:
            self.account_info["history"].append(f"Welcome to {self.account_info["bank"]}, You Deposit Rupees +{amount}, You have Balance of Rupess {self.account_info["balance"]}")
            json.dump(self.account_info, f , indent=4)
        print(f"Welcome to {self.account_info["bank"]}, You Deposit Rupees: {amount} you balance is Rupees: {self.balance}")
            

    # Withdrawal Functionality

    def withdrawal(self, cash=0):
        if cash <= self.balance and cash <= 50000:
            self.balance -= cash
            self.account_info["balance"] = self.balance

            with open(f"{self.user_info_path}", "w") as f:
                self.account_info["history"].append(f"Welcome to {self.account_info["bank"]}, You Widthawal of Rupees: {cash} you new balance is Rupees: {self.balance}")
                json.dump(self.account_info, f , indent=4)

                print(
                f"Welcome to {self.account_info["bank"]}, You Widthawal of Rupees: {cash} you new balance is Rupees: {self.balance}")                
         
        elif cash > 50000:
            print("You Limit is just 50,000 Rupess, Try lower Value")
        else:
            print("Insufficient Balance in your Account.")

    # Balance Checker Functionality

    def balance_check(self):
        print(
            f"Welcome to {self.account_info["bank"]}, Your account balance is {self.account_info["balance"]} ")

    # Transaction History Functionality

    def check_transaction_history(self):
        for item in self.account_info["history"]:
            print(f"{item}\n")

    # Transfer Fund within Accounts Functionality

    def transfer_fund(self, payee, value):
        
        if payee != "" and value != "":
            if value <= self.balance:
                payee_path = f"Accounts/{payee}/{payee}_info.json"
                if os.path.exists(payee_path):
                    with open(payee_path, "r") as f:
                        payee_info = json.load(f)

                    payee_balanace = payee_info["balance"]
                    self.balance -= value
                    payee_balanace += value

                    payee_info["balance"] = payee_balanace
                    self.account_info["balance"] = self.balance

                    with open(payee_path, "w") as f:

                        payee_info["history"].append(f"Welcome to {self.account_info["bank"]}, {self.account_holder} is transfered Rupees +{value}, You have Balance of Rupess {payee_info["balance"]}")
                        json.dump(payee_info, f , indent=4)

                    with open(self.user_info_path, "w") as f:

                        self.account_info["history"].append(f"Welcome to {self.account_info["bank"]}, {self.account_holder}, You Transfered -{value} Rupees to {payee}")
                        json.dump(self.account_info, f , indent=4)
                        
                    print(
                            f"Welcome to {self.account_info["bank"]}, {self.account_holder}, You Transfered {value} Rupees to {payee}")
    
                else:
                    print("Payee Account Not Available")
            else:
                print("Insufficient Balance in your Account")


# Selecting Actions Functionality

class account_handling:
    type = input("Login / Signup: ")

    def __init__(self):

        self.account_user = input("Enter Name: ")
        self.account_passcode = input("Enter Passcode: ")
        self.account_path = f"Accounts/{self.account_user}"

        if self.type == "Login":

            if verify_account(self.account_user, self.account_passcode) is True:

                account_access = online_banking(f"{self.account_user}")
                print("Welcome to Sadaat Bank Limited!")
                print("Withdraw\nDeposit\nBalance\nHistory\nTransfer\nLogout")
                while True:
                    select_option = input("Select Menu: ").capitalize()
                    if select_option == "Deposit":
                        account_access.deposit(
                            int(input(f"{self.account_user} Deposit Amount: ")))

                    elif select_option == "Withdraw":
                        account_access.withdrawal(
                            int(input(f"{self.account_user} Withdraw Amount: ")))

                    elif select_option == "Balance":
                        account_access.balance_check()

                    elif select_option == "History":
                        account_access.check_transaction_history()

                    elif select_option == "Transfer":
                        account_access.transfer_fund(
                            input("Enter Payee Name: "), int(input("Enter Amount: ")))

                    elif select_option == "Logout":
                        print(f"Thank you to using the Standard Chartered Bank, Bye Bye")
                        break
                    else:
                        print(
                            f"Your Selected Option {select_option} is not available in menu")
                

        if self.type == "Signup":

            account_generate(self.account_path,
                             self.account_user, self.account_passcode)


start_banking = account_handling()
