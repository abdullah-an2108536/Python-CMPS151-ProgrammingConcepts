# Write a program to find the factorial of a number.
# Validate your input. Continue only if the user inputs a non-negative value.


x=int(input('Enter x : '))
while x<0:
    x=int(input('Enter x : '))
fact=1
for i in range(1,x+1):
    fact=fact*i
print('factorial = ',fact)


