# Write a program that will convert an integer value representing an amount of
# money in QatariRiyals into the smallest number of bank notes needed to
# add up to that amount

money = int(input("Enter a number of Riyals to convert or 0 to Stop: "))
while money != 0:
    fiveh = money // 500
    money = money % 500
    oneh = money // 100
    money = money % 100
    fifty = money // 50
    money = money % 50
    ten = money // 10
    money = money % 10
    five = money // 5
    money = money % 5
    one = money // 1
    print(
        fiveh,
        "- 500,",
        oneh,
        "- 100,",
        fifty,
        "- 50,",
        ten,
        "- 10,",
        five,
        "- 5,",
        one,
        "- 1,",
    )
    money = int(input("Enter a number of Riyals to convert or 0 to Stop: "))
print("Done...")
