import Bank

account1 = Bank.Account(100, "Khalid", 0)
account2 = Bank.Account(200, "Nouf", 0)

account1.deposit(5000)
account2.deposit(3000)

account1.withdraw(4000)
account1.withdraw(4000)
print(account1.get_balance())
print()
print(account2.get_balance())

#   write function transfer that receives two objects of type account and a
#   number represents amount of money to be transferred from the first
#   object to the second object. Call the function to transfer 500 from the
#   first account to the second one, and print the balances of the two
#   accounts after transfer


def transfer(account1, account2, money):
    account1.withdraw(money)
    account2.deposit(money)


transfer(account1, account2, 500)

print(account1.get_balance())
print(account2.get_balance())
