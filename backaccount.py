import os


# File Path Checking in Directory

def checking_file_exist(filepath):
    try:
        with open(f"{filepath}", "r") as f:
            f.read()
    except FileNotFoundError:
        with open(f"{filepath}", "w") as f:
            f.write("0")


class backaccount:
    bankname = "Standard Chartered"

    def __init__(self, name, balance=0):
        self.balance = balance
        self.name = name
        self.filepath = f"Bank Account Application/backaccount/{self.name}_account.txt"
        self.history = f"Bank Account Application/backaccount/{self.name}_account_history.txt"

        checking_file_exist(self.filepath)

        with open(self.filepath, "r") as f:
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
                        payee_path = f"Bank Account Application/backaccount/{payee}_account.txt"
                        payee_history_path = f"Bank Account Application/backaccount/{payee}_account_history.txt"

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
        if self.type == "Login":
            account_name = input("Enter Name: ")
            try:
                with open(f"Bank Account Application/backaccount/{account_name}_account.txt", "r") as f:
                    f.read()
            except FileNotFoundError:
                print("Your account is not created")
                return

            account_name = backaccount(f"{account_name}")
            while True:
                select_option = input(
                    "Withdraw, Deposit, Balance, History, Transfer, Logout: ").capitalize()
                if select_option == "Deposit":
                    account_name.deposit(
                        int(input(f"{account_name} Deposit Amount: ")))

                elif select_option == "Withdraw":
                    account_name.withdrawal(
                        int(input(f"{account_name} Withdraw Amount: ")))

                elif select_option == "Balance":
                    account_name.balance_check()

                elif select_option == "History":
                    account_name.check_transaction_history()

                elif select_option == "Transfer":
                    account_name.transfer_fund(
                        input("Enter Payee Name: "), int(input("Enter Amount: ")))

                elif select_option == "Logout":
                    print(f"Thank you to using the Standard Chartered Bank, Bye Bye")
                    break
                else:
                    print(
                        f"Your Selected Option {select_option} is not available in menu")

        if self.type == "Signup":
            account_name = input("Enter Name: ")
            try:
                with open(f"Bank Account Application/backaccount/{account_name}_account.txt", "r") as f:
                    name = f.read()
                    if name:
                        print("You Already have Account, Please login Instead")
                        return
            finally:
                with open(f"Bank Account Application/backaccount/{account_name}_account.txt", "w") as f:
                    f.write("0")
                    print("Your Account is Created Sucessfully, Please Login")
                    return


start_banking = account_handling()
