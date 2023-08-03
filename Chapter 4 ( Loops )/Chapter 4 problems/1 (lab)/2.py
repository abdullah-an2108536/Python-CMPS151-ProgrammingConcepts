#Create a program that asks the user to enter a number (call it x)
# and then uses a while loop to print and add up all of the numbers from 1 to x and then 
# compute the average of these numbers

x=int(input('enter number:'))
sum=0
i=1
while i<=x:
    sum=sum+i
    if i !=x:
        print(i,'+',end='')
    else:
        print(i)
    i=i+1
print(sum)
print(sum/x)