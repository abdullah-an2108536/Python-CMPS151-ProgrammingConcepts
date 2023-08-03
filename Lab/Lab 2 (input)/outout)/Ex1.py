import math

a=float(input('enter a: '))
b=float(input('enter b: '))
c=float(input('enter c: '))

x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
x2=(-b-(b**2-4*a*c)**0.5)/(2*a)

print('x1= ',x1)
print('x2= ',x2)