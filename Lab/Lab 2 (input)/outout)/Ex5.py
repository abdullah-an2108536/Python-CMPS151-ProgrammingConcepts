p=float(input('Enter the starting principal = '))
r=float(input('Enter the annual interest rate = '))
n=int(input('How many times per year is the interest compounded = '))
t=int(input('For how many years will the account earn interest = '))

r=r/100
A=p*(1+r/n)**(n*t)

print('At the end of',t,'years, you will have $ %.2f' %A)