class Account():
    def __init__(self, owner, balance):
        self.ownner = owner
        self.balance = balance
    
    def __str__(self):
        return ("The owner is " + self.ownner + "\nThe balance is " + str(self.balance))

    def deposit(self,amount):
        self.balance = self.balance + amount
        return ("you just added to your account: " + str(amount) + "$")


    def withdraw(self, amount):
        if self.balance - amount < 0:
            return ("You don´t have enough money for that")
        else:
            self.balance = self.balance - amount
            return ("you just withdraw from your account: " + str(amount) + "$")

pepe = Account("pepe",222)

a = pepe.balance
b = pepe.deposit(675)
c= pepe.withdraw(400)
d= pepe.balance
e = pepe.withdraw(497)
print (b,c,a,d)
print(e)