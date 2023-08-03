# Write a program that asks the user to enter 10 integers, and print the maximum
# digit in all numbers.

max=0
for i in range(10):
    integer=int(input('Enter an integer....'))
    x=integer
    max=0
    while x!=0:
        x1=x%10
        x=x//10
        if x1>max:
            max=x1
    print(max,'is max')
    


