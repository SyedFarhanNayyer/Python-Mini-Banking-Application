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

    account_info = {"Bank" : "Sadaat Bank Limited", "name": name, "pass_code": passcode, "balance": 0, "History" : {} }

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
    else: 
        return False


class online_banking:
    bankname = "Sadaat Bank Limited"

    def __init__(self, name, balance=0):
        self.account_holder = name
        self.user_info = f"Accounts/{self.account_holder}/{self.account_holder}_info.json"
        print(self.user_info)
        with open(self.user_info, "r") as f:
            user_account_info = json.load(f)

        self.balance = user_account_info["balance"]

        print(self.balance)

    # Deposit Functionality

    def deposit(self, amount):
        self.balance += amount
        with open(f"{self.filepath}", "w") as f:
            f.write(f"{self.balance}")
        print(
            f"Welcome to {self.bankname}, You Deposit Rupees: {amount} you balance is Rupees: {self.balance}")

        checking_file_exist(self.history)

        with open(f"{self.history}", "a") as f:
            f.write(
                f"\nWelcome to {self.bankname}, You Deposit Rupees +{amount}, You have Balance of Rupess {self.balance}")

    # Withdrawal Functionality

    def withdrawal(self, cash=0):
        if cash <= self.balance and cash <= 50000:
            self.balance -= cash
            with open(f"{self.filepath}", "w") as f:
                f.write(f"{self.balance}")
            print(
                f"Welcome to {self.bankname}, You Widthawal of Rupees: {cash} you new balance is Rupees: {self.balance}")

            checking_file_exist(self.history)

            with open(f"{self.history}", "a") as f:
                f.write(
                    f"\nWelcome to {self.bankname}, You Withdraw Rupees -{cash}, You have Balance of Rupess {self.balance}")

        elif cash > 50000:
            print("You Limit is just 50,000 Rupess, Try lower Value")
        else:
            print("Insufficient Balance in your Account.")

    # Balance Checker Functionality

    def balance_check(self):
        print(
            f"Welcome to {self.bankname}, Your account balance is {self.balance} ")

    # Transaction History Functionality

    def check_transaction_history(self):
        with open(f"{self.history}", "r") as f:
            history = f.readlines()
            for transaction in history:
                print(f"{transaction}", end="")

    # Transfer Fund within Accounts Functionality

    def transfer_fund(self, payee, value):

        if payee != "" and value != "":
            if value <= self.balance:
                self.balance -= value
                with open(f"{self.filepath}", "w") as f:
                    f.write(f"{self.balance}")
                    print(
                        f"Welcome to {self.bankname}, {self.name}, You Transfered {value} Rupees to {payee}")

                    checking_file_exist(self.history)

                    with open(f"{self.history}", "a") as f:
                        f.write(
                            f"\nWelcome to {self.bankname}, {self.name}, You Transfered {value} Rupees to {payee}")
                    if payee != "":
                        payee_path = f"Bank Account Application/Accounts/{payee}_account.txt"
                        payee_history_path = f"Bank Account Application/Accounts/{payee}_account_history.txt"

                        with open(f"{payee_path}", "r") as f:
                            payee_balance = int(f.read())
                            payee_balance += value

                        with open(f"{payee_path}", "w") as f:
                            f.write(f"{payee_balance}")
                        with open(f"{payee_history_path}", "a") as f:
                            f.write(
                                f"\nWelcome to {self.bankname}, {self.name} is transfered Rupees +{value}, You have Balance of Rupess {payee_balance}")
            else:
                print("Insufficient Balance in your Account")


# Selecting Options Functionality

class account_handling:
    type = input("Login / Signup: ")

    def __init__(self):

        self.account_user = input("Enter Name: ")
        self.account_passcode = input("Enter Passcode: ")
        self.account_path = f"Accounts/{self.account_user}"
  

        if self.type == "Login":

            if verify_account(self.account_user, self.account_passcode) is True:

                account_access = online_banking(f"{self.account_user}")
                while True:
                    print("Welcome to Sadaat Bank Limited!")
                    print("Withdraw\nDeposit\nBalance\nHistory\nTransfer\nLogout")
                    select_option = input("Select Menu: ").capitalize()
                    if select_option == "Deposit":
                        account_access.deposit(
                            int(input(f"{self.account_user} Deposit Amount: ")))

                    elif select_option == "Withdraw":
                        account_access.withdrawal(
                            int(input(f"{self.account_use} Withdraw Amount: ")))

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
            else:
                print(f"Hi {self.account_user}, You are not a Sadaat Bank Limited User.")

        if self.type == "Signup":

            account_generate(self.account_path,
                             self.account_user, self.account_passcode)


start_banking = account_handling()
