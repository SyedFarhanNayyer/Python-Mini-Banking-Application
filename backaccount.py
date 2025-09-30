import os
import json


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

# File Path Checking in Directory


def account_generate(filepath, name, passcode=0000):

    account_info = {"name": name, "pass_code": passcode, "balance": 0}

    if os.path.exists(filepath):
        print("You already Have Account, Login to your Account")
    else:
        os.mkdir(filepath)
        print(f"Account Sucessfully Created")
    with open(f"{filepath}/{name}_info.json", "w") as f:
        json.dump(account_info, f)


class online_banking:
    bankname = "Sadaat Bank Limited"

    def __init__(self, name, balance=0):
        self.balance = balance
        self.account_holder = name
        self.accounts_path = "Accounts"
        self.user_info = os.path.join(
            self.accounts_path, f"{self.account_holder}_info.json")

        print(self.user_info)
        self.history = os.path.join(
            self.accounts_path, f"{self.account_holder}_history.json")
        print(self.history)
        checking_file_exist(self.user_info)

        with open(self.user_info, "r") as f:
            new_balance = int(f.read())
            if new_balance != "":
                self.balance = new_balance
            else:
                self.balance = 0

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
        print(self.account_user, self.account_path)

        if self.type == "Login":
            # account_generate(self.account_path)

            self.account_user = online_banking(f"{self.account_user}")
            while True:
                select_option = input(
                    "Withdraw, Deposit, Balance, History, Transfer, Logout: ").capitalize()
                if select_option == "Deposit":
                    self.account_user.deposit(
                        int(input(f"{self.account_user} Deposit Amount: ")))

                elif select_option == "Withdraw":
                    self.account_user.withdrawal(
                        int(input(f"{self.account_use} Withdraw Amount: ")))

                elif select_option == "Balance":
                    self.account_user.balance_check()

                elif select_option == "History":
                    self.account_user.check_transaction_history()

                elif select_option == "Transfer":
                    self.account_user.transfer_fund(
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
