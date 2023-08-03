# This program reads the contents of the
# philosophers.txt file one line at a time.

def main():
    myfile=open('Philosiphers.txt','r')

    line1=myfile.readline()
    line2=myfile.readline()
    line3=myfile.readline()

    myfile.close()

    print(line1.strip())
    print(line2.strip())
    print(line3.strip())

main()