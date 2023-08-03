class Account:
    def __init__(self,a,n,b):
        self.__accno=a
        self.__name=n
        self.__balance=b
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            print('insufficent funds')
        else:
            self.__balance+=amount
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return 'account number = '+str(self.__accno)+'\nname = '+self.__name+'\nbalance = '+str(self.__balance)