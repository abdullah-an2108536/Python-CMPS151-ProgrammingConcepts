#Assume you have a list of 10 numbers, write a program to calculate the
#average of the elements in the list.
numbers=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in numbers:
    sum=sum+i
avg=sum/len(numbers)
print(avg)