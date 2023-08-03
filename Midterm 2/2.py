list=[]
values=int(input('How many values '))
for i in range(values):
    text='enter value'+str(i)
    x=input(text)
    list.append(x)
print('values = ',end='')
for j in list:
    print(j,end=' ')