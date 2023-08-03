#  To create a new module, create a new file call it “myModule.py”, and copy the
# functions “fact” (in Q1), and function “power” (Q2) to that file. In another file,
# write a program to read two integers from user x, y. Call function “fact” to print
# the factorial for both numbers, and call function “power” to print xy.

import LabModule

def main():
    x=int(input('Enter an integer, x.... '))
    y=int(input('Enter an integer, y.... '))
    print('Factorial of x is',LabModule.factorial(x))
    print('Factorial of y is',LabModule.factorial(y))
    print('power....',LabModule.power(x,y))
    print('max is',LabModule.max(x,y))
    if LabModule.isPrime(x):
        print('x is a Prime number')
    else:
        print('x is not a Prime number')
    if LabModule.isPrime(y):
        print('y is a Prime number')
    else:
        print('y is not a Prime number')
main()