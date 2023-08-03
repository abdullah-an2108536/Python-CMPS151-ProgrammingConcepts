r=int(input('enter radius : '))
if r<=0:
    print('Invlaid Input')
    exit(1)
h=int(input('enter height : '))
if h<=0:
    print('Invlaid Input')
    exit(1)
V=(3.14)*((r**2)*(h))
SA=(2*(3.14)*(r**2))+(2*(3.14)*(r*h))
print('Volume:',V)
print('Surface Area:',SA)
