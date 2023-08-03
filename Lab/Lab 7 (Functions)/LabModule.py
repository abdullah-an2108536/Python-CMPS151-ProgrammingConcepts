def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

def power(x,y):
    pow=1
    for i in range(1,y+1):
        pow=pow*x
    return pow

def digits(x):
    count=0
    while x!=0:
        x=x//10
        count=count+1
    return count

def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def celsiusToFahr(C):
    F=1.8*C + 32
    return F

def max(x,y):
    if x>y:
        return x
    else:
        return y