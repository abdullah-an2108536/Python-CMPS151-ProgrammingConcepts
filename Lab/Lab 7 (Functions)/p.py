def stars(n):
    count=n
    for i in range(n):
        print('* '*count)
        count=count-1

def main():
    n=int(input('Enter the length of the triangle .... '))
    stars(n)

main()


