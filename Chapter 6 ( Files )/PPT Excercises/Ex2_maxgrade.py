# Write a program to opens the file “Students.txt”, process the
# data to display the name of the students who has the highest
# grade. (assume the number of students records is unkown)

def main():
    maxfile=open('Philosiphers.txt','r')
    max=0
    name=maxfile.readline()
    while name!='':
        grade=int(maxfile.readline().strip())
        if grade>max:
            maxname=name.strip()
        name=maxfile.readline()
    maxfile.close()
    print('Stdent with the highest grade is ...',maxname)
main()



