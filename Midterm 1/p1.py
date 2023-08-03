#Write a program that asks the user to enter two numbers, your program should
# validate that the first one is less than the second one, then print all odd numbers
# between these two numbers including them if they are odds. 

a=int(input('a='))
b=int(input('b='))
while a>=b:
    a=int(input('a='))
for i in range(a,b):
    if i%2!=0:
        print(i)
