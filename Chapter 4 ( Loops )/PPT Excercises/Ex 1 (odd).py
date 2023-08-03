#Write a program that keeps asking the user to enter a number
#and checks if it is odd or even until the user enters 0 prints “Done…

number=int(input('Enter number: '))

while number !=0:
    if (number%2==0):
        print(number,'is even')
        number=int(input('Enter number: '))
    else:
        print(number,'is odd')
        number=int(input('Enter number: '))


print('Done')