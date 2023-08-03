#Write a program that asks the user to enter an integer number
#composed of three digits. Your program should print the total of the digits.

i=int(input('enter an integer number . '))
i=str(i)
sum=0
for j in i:
    sum=sum+int(j)
print(sum)

