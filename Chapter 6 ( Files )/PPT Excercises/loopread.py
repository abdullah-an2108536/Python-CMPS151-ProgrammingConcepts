def main():
    myfile=open('Philosiphers.txt','r')
    line=myfile.readline()
    total=0
    while line!='':
        total=total+int(line)
        line=myfile.readline()
    myfile.close
    print(total)
main()