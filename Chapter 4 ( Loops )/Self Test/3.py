#Using nested loop, write a program that displays the following pattern  

for i in range(1,8):
    for j in range (7-i):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()

for i in range(4):
