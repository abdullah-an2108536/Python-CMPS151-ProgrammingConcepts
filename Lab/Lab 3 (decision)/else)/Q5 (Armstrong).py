number=int(input('Enter three digit number : '))
if (number>999) or (number<100):
    print('invalid')

digit1=number//100
n=number%100
digit2=n//10
digit3=n%10

sum=(digit1**3)+(digit2**3)+(digit3**3)
if (number==sum):
    print('this is an Armstrong number')
else:
    print('this is not an Armstrong number')