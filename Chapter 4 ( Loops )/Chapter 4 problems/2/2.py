#Write a Python program that sums the numbers that fall in a range of values.
#Ask the user to input the starting and ending values of the range.
#Validate the input.

start=int(input('start ='))
end=int(input('start ='))
sum=0
for i in range(start,end+1):
    sum=sum+i
print(sum)