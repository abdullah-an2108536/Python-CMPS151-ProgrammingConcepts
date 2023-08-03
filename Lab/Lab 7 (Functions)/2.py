#. Using one of the loop structures, write function power(x,y) which calculates Xy
# Then use this function in main program to calculate the following

def main():
    n=int(input('Enter n : '))
    sum=0
    for n in range(1,n+1):
        sum=sum+power(n,n+1)
    print('K = %.1f' %sum)

def power(x,y):
    pow=1
    for i in range(1,y+1):
        pow=pow*x
    return pow

main()