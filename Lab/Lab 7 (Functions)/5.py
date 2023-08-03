#Write a function stars(n) that receives length to get a triangle shape as in the
#below sample run. Test your function in the main

def stars(n):
    for i in range(n):
        for j in range (1,n-i+1):
            print('*',end=' ')
        print('\n')

def main():
    n=int(input('Enter the length of the triangle .... '))
    stars(n)

main()


#                                           SECOND METHOD
#   def stars(n):
#       count=n
#       for i in range(n):
#           print('* '*count)
#           count=count-1
#   
#   def main():
#       n=int(input('Enter the length of the triangle .... '))
#       stars(n)
#   main()