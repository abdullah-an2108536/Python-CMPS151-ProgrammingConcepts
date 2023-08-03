#An electric company charges the customers as follows:
#- $1.5 for every kwh for the first 1000 kwh
#- $2 for every kwh in the second 1000 kwh
#- $2.5 for every kwh greater than 2000 kwh
#If a customer usage was 3400, then he should pay 1.5*1000+2*1000+2.5*1400.
#Write a program that asks the user to enter his usage, then calculate the cost,
#and add 10% tax, then display the total cost (cost+tax).

usage=int(input('Enter the electricity usage : '))
total_cost=0
cost1=0
cost2=0
cost3=0
for i in range(1,usage+1):
    if i<=1000:
        cost1=cost1+(1.5)
    elif i<=2000:
        cost2=cost2+(2)
    else:
        cost3=cost3+(2.5)
total_cost=cost1+cost2+cost3
tax=1.10
total_cost=total_cost*tax
print('Total cost is.... %.2f' %total_cost)