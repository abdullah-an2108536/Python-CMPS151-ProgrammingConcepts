n=int(input('Enter n : '))
y=1
fact=1
print('i','\t','sum of i terms')
print('---','\t','--------------------')
for i in range(1,n+1):
    fact=fact*i
    y=y+(1/fact)
    print(i,'\t',y)
print(sum)