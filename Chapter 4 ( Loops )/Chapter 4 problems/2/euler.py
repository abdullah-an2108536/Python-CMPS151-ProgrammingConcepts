n=int(input('Enter n : '))
e=1
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    e=e+(1/fact)
print(e)