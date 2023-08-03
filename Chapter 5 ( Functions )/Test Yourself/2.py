#Write function called maxDigit that receives an integer and returns the maximum digit in that
#number. Use that function to read an integer number from the user and print the maximum digit in
#the input number. 

def maxDigit(integer):
    max=-1
    for chr in integer:
        chr2=int(chr)
        if chr2>=max:
            max=chr
    return max

def main():
    x=maxDigit('553353290594036')
    print(x)

main()