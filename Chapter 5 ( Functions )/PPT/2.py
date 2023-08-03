# Write function max(x,y) that receives two integers and
# returns the maximum one. Call this function.


def main():
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    print("max is ", max(x, y))


def max(x, y):
    if x > y:
        return x
    else:
        return y


main()
