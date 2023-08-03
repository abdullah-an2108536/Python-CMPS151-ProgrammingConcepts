def getfact(n):
    if n<0:
        return -1
    elif n>=0:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact

print(getfact(5))
