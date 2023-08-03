#Write a program that keeps asking the user to enter integer number until the user enters -999,
#  then display the maximum number entered. 

x=int(input('x='))
max=x
while x!=-999:
    x=int(input('x='))
    if x>max:
        max=x
print(max)


