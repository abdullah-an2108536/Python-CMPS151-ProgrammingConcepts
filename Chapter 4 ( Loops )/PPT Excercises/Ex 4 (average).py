#write a program to read 10 integers from user and print the average.

sum=0
for i in range(10):
    integer=int(input('Enter integer='))
    sum+=integer
print(sum/10)