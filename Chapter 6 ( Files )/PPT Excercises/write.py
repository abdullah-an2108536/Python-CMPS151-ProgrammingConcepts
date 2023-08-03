# This program gets three names from the user
# and writes them to a file.

def main():
    name1=input('Enter name 1 ')
    name2=input('Enter name 2 ')
    name3=input('Enter name 3 ')

    myfile=open('Philosiphers.txt','w')
    myfile.write(name1+'\n')
    myfile.write(name2+'\n')
    myfile.write(name3+'\n')
    myfile.close()


main()