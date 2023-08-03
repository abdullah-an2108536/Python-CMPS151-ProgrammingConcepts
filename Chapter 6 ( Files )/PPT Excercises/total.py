def main():
    myfile=open('Philosiphers.txt','r')

    num1=int(myfile.readline().strip())
    num2=int(myfile.readline().strip())
    num3=int(myfile.readline().strip())

    total=num1+num2+num3

    myfile.close()
    print('Total is ',total)

main()