#Write a function printStars that receives an integer n and print
#a triangle of starts, its based has n starts, then call this function
#For example if n was 5 the output should look like the following

def printStars(n):
    for i in range(n):
        for j in range(i+1):
            print('*')

printStars(5)
