weight=int(input('Enter weight of package in pounds: '))
if (weight<=2):
    charge=weight*1.50
    print('Shipping charges : %.2f' %charge)
elif (weight>2) and (weight<6):
    charge=weight*3.00
    print('Shipping charges : %.2f' %charge)
elif (weight>6) and (weight<10):
    charge=weight*4.00
    print('Shipping charges : %.2f' %charge)
else:
    charge=weight*4.75
    print('Shipping charges : %.2f' %charge)