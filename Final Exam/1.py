# It was about something the pollish  n ( idk how to spell it), anyway
# it’s a number that the sum of its odd n = sum of its even number n
# it doesn’t contain zero
# So if it’s true return true wither ways return false
# Either* way


def ispolish(n):
    if n <= 0:  # no zero
        return False
    n = str(n)
    listn = list(n)
    sumodd = 0
    sumeven = 0
    for i in listn:
        if int(i) % 2 == 0:
            sumeven += int(i)  # dont forget int()
        else:
            sumodd += int(i)
    if sumodd == sumeven:
        return True
    else:
        return False


print(ispolish(853))
