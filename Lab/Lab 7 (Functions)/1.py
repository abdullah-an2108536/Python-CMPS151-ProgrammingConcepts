# Write function fact(n) that receives n integer number and calculate
# n!=1X2X3X…Xn.
# Then write main function that reads integer x from the user then using the function
# fact calculate y as follows

def main():
    n=int(input('Enter an integer, n : '))
    factorial_n=factorial(n)
    y=0
    for i in range (1,n+1):
        y=y+(i/factorial(i+1))
    print('y = ',y)

def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

main()