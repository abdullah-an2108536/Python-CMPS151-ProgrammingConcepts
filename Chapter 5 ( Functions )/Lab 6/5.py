# Write a Python function that swaps two integers


def main():
    x = int(input("Enter x : "))
    y = int(input("Enter y : "))
    print("Before: x = ", x, " and y= ", y)
    x, y = myswap(x, y)
    print("After : x = ", x, " and y= ", y)


def myswap(x, y):
    j = x
    k = y
    x = k
    y = j
    return x, y


main()


