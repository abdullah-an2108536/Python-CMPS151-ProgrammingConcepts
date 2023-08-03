# Prime number is the number that is divisible only by one and itself. Write function
# is Prime that receives an integer and returns true if that number is prime,
# otherwise it returns false.
# Use that function in main function to print the prime numbers between 2 and 100.

def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def main():
    for i in range(2,100):
        if isPrime(i):
            print(i)

main()