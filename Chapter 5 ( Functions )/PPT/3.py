# Write function factorial(n) that receives an integer and
# return its factorial. Call this function. 

Const=1

def main():
    number=int(input('Enter a number....'))
    print('factorial is',factorial(number))

def factorial(x):
    fact=1
    for i in range(Const,x+1):
        fact=fact*i
    return fact

main()