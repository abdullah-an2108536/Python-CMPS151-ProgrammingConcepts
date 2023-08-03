# startup screen.
print("_" * 48)
print("\t\tZAKI Restaurant")
print("_" * 48)
print("Meal#\tMeal Price\tMeal Description")
print("_" * 48)
print("1\t30.00\t\tShawarma.")
print("2\t50.00\t\tPizza.")
print("3\t70.00\t\tSea Food.")
print("4\t35.00\t\tGrilled Chicken.")
print("_" * 48)

# ask for meal number and quantity.
meal_number = int(input("Enter the meal number you want to order: "))
while (meal_number < 1) or (meal_number > 4):  # validating input
    print("Invalid meal #, please enter a number between 1 and 4 ! ")
    meal_number = int(input("Enter the meal number you want to order: "))

meal_quantity = int(input("Enter meal quantity : "))
while (meal_quantity < 1) or (meal_quantity > 100):  # validating input
    print("Invalid quantity , please enter quantity between 1 and 100 ! ")
    meal_quantity = int(input("Enter meal quantity : "))

# establish relationship between meal number and price.
if meal_number == 1:
    meal_price = 30
elif meal_number == 2:
    meal_price = 50
elif meal_number == 3:
    meal_price = 70
else:
    meal_price = 35

# calculations.
subtotal = meal_price * meal_quantity
tax = 0.15 * subtotal
total_meal_price = tax + subtotal
total_bill = total_meal_price

# display order information.
print("_" * 92)
print(
    "Meal#   Meal Price\tMeal Quantity\tSubtotal Meal Price\tTax\t    Total Meal Price"
)
print(
    meal_number,
    "     ",
    meal_price,
    "\t       ",
    meal_quantity,
    "\t       ",
    subtotal,
    "\t\t       ",
    tax,
    "\t   ",
    total_meal_price,
)
print("Total Bill: ", total_bill)

# asking user for another meal.
another_meal = input("Would you like to order another meal? [Y/N] ")
while (
    (another_meal != "y")
    and (another_meal != "Y")
    and (another_meal != "n")
    and (another_meal != "N")
):
    print("Invalid Input")
    another_meal = input("Would you like to order another meal? [Y/N] ")

# loop if user wants another meal
while another_meal == "y" or (another_meal == "Y"):
    print("_" * 48)  # startup screen again
    print("\t\tZAKI Restaurant")
    print("_" * 48)
    print("Meal#\tMeal Price\tMeal Description")
    print("_" * 48)
    print("1\t30.00\t\tShawarma.")
    print("2\t50.00\t\tPizza.")
    print("3\t70.00\t\tSea Food.")
    print("4\t35.00\t\tGrilled Chicken.")
    print("_" * 48)
    # asking for meal number and quantity again
    meal_number = int(input("Enter the meal number you want to order: "))
    while (meal_number < 1) or (meal_number > 4):
        print("Invalid meal #, please enter a number between 1 and 4 ! ")
        meal_number = int(input("Enter the meal number you want to order: "))
    meal_quantity = int(input("Enter meal quantity : "))
    while (meal_quantity < 1) or (meal_quantity > 100):
        print("Invalid quantity , please enter quantity between 1 and 100 ! ")
        meal_quantity = int(input("Enter meal quantity : "))
    if meal_number == 1:  # calculations again
        meal_price = 30
    elif meal_number == 2:
        meal_price = 50
    elif meal_number == 3:
        meal_price = 70
    else:
        meal_price = 35
    subtotal = meal_price * meal_quantity
    tax = 0.15 * subtotal
    total_meal_price = tax + subtotal
    total_bill = total_meal_price + total_bill  # total bill calculation is different
    print("_" * 92)  # disoplaying again
    print(
        "Meal#   Meal Price\tMeal Quantity\tSubtotal Meal Price\tTax\t    Total Meal Price"
    )
    print(
        meal_number,
        "     ",
        meal_price,
        "\t       ",
        meal_quantity,
        "\t       ",
        subtotal,
        "\t\t       ",
        tax,
        "\t   ",
        total_meal_price,
    )
    print("Total Bill: ", total_bill)
    another_meal = input("Would you like to order another meal? [Y/N] ")
    while (
        (another_meal != "y")
        and (another_meal != "Y")
        and (another_meal != "n")
        and (another_meal != "N")
    ):
        print("Invalid Input")
        another_meal = input("Would you like to order another meal? [Y/N] ")

# when user dosen't want another meal
if another_meal == "n" or (another_meal == "N"):
    # asking for delivery or pickup
    transport_des = input("Enter 1 for delivery or 2 for self-pickup: ")
    while transport_des != "1" and transport_des != "2":  # validating input
        print("Invalid Input...")
        transport_des = input("Enter 1 for delivery or 2 for self-pickup: ")
    if transport_des == "1":  # asking for zone when user choses delivery
        zone = int(input("Enter the zone number: "))
        while zone < 1 or zone > 12:  # validating input
            print("Invalid Input")
            zone = int(input("Enter the zone number: "))
        if zone >= 1 and zone <= 4:  # setting delivery price
            delivery = 10
        elif zone >= 5 and zone <= 8:
            delivery = 15
        elif zone >= 9 and zone <= 12:
            delivery = 25
        total_bill = total_bill + delivery
        # printing total bill including delivery charges
        print("Delivery Charge:", delivery)
        print("Total Bill :", total_bill)
    else:
        # just printing total bill again if user choses pickup
        print("Total Bill :", total_bill)
        print("Thank You !")