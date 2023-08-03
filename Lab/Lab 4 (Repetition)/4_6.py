n=int(input('Enter n : '))
y=0
for x in range(1,n+1):
    y=y+(x/(x+1))
print('y =',y)