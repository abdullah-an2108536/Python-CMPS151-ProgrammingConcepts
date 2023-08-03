# Write function digits( int n) that receives an integer and returns number of digits
# in that number. For example, if n is 345, the function should return 3. Then test
# this function in the main.

def digits(x):
    #count=0
    #while x!=0:
    #    x=x//10
    #    count=count+1
    #return count
    string=str(x)
    return len(string)

def main():
    n=int(input('Enter integer, n : '))
    print('This integer has',digits(n),'digits')

main()

