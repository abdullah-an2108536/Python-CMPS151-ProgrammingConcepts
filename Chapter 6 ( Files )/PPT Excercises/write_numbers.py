def main():
    num1=int(input('Enter a number .... '))
    num2=int(input('Enter a number .... '))
    num3=int(input('Enter a number .... '))

    myfile=open('Philosiphers.txt','w')

    myfile.write(str(num1)+'\n')
    myfile.write(str(num2)+'\n')
    myfile.write(str(num3)+'\n')

    myfile.close()

main()


