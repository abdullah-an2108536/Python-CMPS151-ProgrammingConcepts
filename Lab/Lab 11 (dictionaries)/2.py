# The program should then randomly quiz the user by displaying the name of
# a country and asking the user to enter its capital. The program should ask
# the user if he wants to continue or not. The program should keep a count of
# the number of correct and incorrect responses.

import random

def main():
    capitals = {
        "Qatar": "Doha",
        "Italy": "Rome",
        "UK": "London",
        "France": "Paris",
        "Egypt": "Cairo",
        "Kuwait": "Kuwait",
    }
    listofkeys = list(capitals.keys())
    listofvalues = list(capitals.values())
    correct = 0
    incorrect = 0
    continue_ = "y"
    while continue_ != "n":
        x = random.randint(0, len(listofkeys) - 1)
        answer = input("what is the capital of " + listofkeys[x] + "... ")
        if answer == listofvalues[x]:
            print("correct")
            correct += 1
        else:
            print("incorrect")
            incorrect += 1
        continue_ = input("continue ? (y/n)")
    print("correct answers = ", correct)
    print("incorrect answers = ", incorrect)


main()
