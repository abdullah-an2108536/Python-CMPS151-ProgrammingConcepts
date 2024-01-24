# Write a program that keep reading students’ scores from the user, until the
# user enters ‐1, the display how many students passed, and how many failed.
# Student is considered passed if the score is 60 or more, and failed if it is less than
# 60.

score = int(input("Enter student score : "))
passed = 0
failed = 0
while score != -1:
    if score >= 60:
        passed += 1
    else:
        failed += 1
    score = int(input("Enter student score : "))
print(passed, "students passed and", failed, "students failed")

# function that takes a list of numbers and returns the average of the numbers in the list.
def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)
