hour=int(input('Enter hours.... '))
i=1
while hour<0 or hour>23:
    i=i+1
    if i<=3:
        hour=int(input('Enter hours.... '))
    else:
        print('Bye for now')
        exit(1)
print('done')