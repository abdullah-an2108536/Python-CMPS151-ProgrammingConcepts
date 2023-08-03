#Q2)Write a program that reads 10 integers and display the minimum.


min=0
for i in range(10):
    num=int(input("Enter a number : "))
    if num<=min:
        min=num
print("The minimum integer is : "+str(min))