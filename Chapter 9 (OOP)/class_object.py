class Account:  # class and then class name, upper letter
    def __init__(self):
        self.account_number = 0  # data attributs, start with self
        self.name = ""
        self.balance = 0

    def deposit(self, ammount):  # self will have the data attributes
        self.balance += ammount

    def withdraw(self, ammount):
        if self.balance >= ammount:
            self.balance -= ammount
        else:
            print("Insufficent fund")

    def getbalance(self):
        return self.balance

#--------------------------------------------------------

account = Account()  # self a variable to class name ()

account.account_number = 45678  # variable.attributes in class
account.name = "Abdullah Nawaz"
account.balance = 5000

print('balance before = ',account.getbalance())

account.withdraw(2500)

print('balance befaore = ',account.getbalance())

