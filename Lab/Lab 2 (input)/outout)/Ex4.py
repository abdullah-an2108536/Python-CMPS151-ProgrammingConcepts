number=int(input('Enter interger of 3 digits : '))

digit1=number%10
number=number//10
digit2=number%10
digit3=number//10

total= digit1 + digit2 + digit3

print('Total =',total)


