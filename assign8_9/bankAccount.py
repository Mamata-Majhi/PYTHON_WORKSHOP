from datetime import datetime
class BankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        # attributes
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
        self.transaction_history=[]

    # method for displaying account setails
    def display(self):
        print(f"Account_Number={self.account_number}\nAccount_holder={self.account_holder}\nBalance={self.balance}")
    
    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
    
    #  method for depositing balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = f"{timestamp} - Deposit: +${amount}"
            self.transaction_history.append(transaction)
            print(f"Deposit of Rs.{amount} successful. New balance:Rs.{self.balance}")

        else:
            print("Invalid deposit amount!!")
    # method for withdrawing balance
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance=self.balance-amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = f"{timestamp} - Deposit: +${amount}"
            self.transaction_history.append(transaction)
            print(f"Withdrawl of Rs.{amount} successful. New balance:Rs.{self.balance}")

        else:
            print("Invalid withdrawal amount or insufficient balance!! ")
        

account1=BankAccount(account_number=456578,account_holder="Mamata",balance=100000)
account1.display()

account1.deposit(500)
account1.display()

account1.withdraw(1000)
account1.display()

account1.display_transaction_history()



    
        