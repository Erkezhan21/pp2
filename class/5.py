class Account:
    def __init__(self):
        self.balance=0
 
    def deposit(self):
        amt = float(input("Amount to be Deposited: ")) #amount
        self.balance += amt
        print("\n Amount Deposited:",amt)
 
    def withdraw(self):
        amt = float(input("\n Amount to be Withdrawn: "))

        if self.balance >= amt:
            self.balance -= amt
            print("\n You Withdrew:", amt)
        else:
            print("\n Withdrawals exceeded the available balance ")
 
    def display(self):
        print("\n Tot Balance=",self.balance)
 
bank = Account()
bank.deposit()
bank.withdraw()
bank.display()