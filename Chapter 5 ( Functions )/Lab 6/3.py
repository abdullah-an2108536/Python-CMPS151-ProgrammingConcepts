def main():
    print('Celcius\t\tFarenheit')
    print('-------------------------------------------------')
    for C in range(0,101,10):
        print(' %6.2f' %C ,'\t\t',celsiusToFahr(C))

def celsiusToFahr(C):
    F=1.8*C + 32
    return F

main()