
def main():
    x=int(input('Enter x : '))
    print(mypow(x,3))


def mypow(x,y):
    pow=1
    for i in range(y):
        pow=pow*x
    return pow

main()