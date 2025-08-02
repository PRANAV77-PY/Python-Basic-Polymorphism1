class ATM:
    def __init__(self,balance):
        self.balance = balance


    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Withdrawn: ',amount)
            print('Balance: ',self.balance)
        else:
            print("Insufficient funds")
            print('Balance: ',self.balance)

#object Creation
atm = ATM(10000)
atm.withdraw(3000)

