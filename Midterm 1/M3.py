print('-'*40)
print('x\t\tf(x)')
print('-'*40)
for x in range(-100,101,2):
    if x<-20:
        fx=(x**3)-(2*(x**2))+10
        print(x,'\t\t',fx)
    elif x<30:
        fx=-2*(x)-5
        print(x,'\t\t',fx)
    else:
        fx=(10*(x**2)+13)/(7*(x)+4)
        print(x,'\t\t',fx)
