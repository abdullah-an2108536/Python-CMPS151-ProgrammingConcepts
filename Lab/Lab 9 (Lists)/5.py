# Download the text file named GasPrices.txt. The file contains the weekly
# average prices for a gallon of gas in the United States, beginning on April
# 5th, 1993, and ending on August 26th, 2013. Each line in the file contains
# the average price for a gallon of gas on a specific date. Each line is formatted in
# the following way: MM-DD-YYYY:Price MM is the two-digit month, DD is the two-digit day,
# and YYYY is the fourdigit year. Write a program to read the contents of the file
# and display the average price per year.

def getprice(list):
    x = list.split(":")
    return x[1]


def getyear(list):
    x = list.split(":")
    y = x[0].split("-")
    return int(y[2])


def main():
    myfile = open("gas.txt", "r")
    lines = myfile.readlines()
    myfile.close
    for i in lines:
        price = getprice(i)
        year = getyear(i)
        print(year, "", price)


main()
