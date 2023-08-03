m=int(input('Enter m :'))
while m<0:
    m=int(input('Enter m: '))
y=0
for i in range(0,m+1):
    y=y+((3+2*i)/(2**i))
print(y)