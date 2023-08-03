#Write a program to read an integer number from user then print if it is prime
#or not. A prime number is an integer number greater than 1, and it is only
#divisible by one and itself

number=int(input('Enter a number : '))
prime=True
for i in range(2,number):
    if number%i==0:
        prime=False
        break
if prime:
    print(number,'is prime')
else:
    print(number,'is not prime')
