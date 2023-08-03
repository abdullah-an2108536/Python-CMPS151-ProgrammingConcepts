#Write a program to read data of 10 students, and save
#them to a file called “students.txt”. For each student, it
#reads student’s name, and grade. In the file, each line
#contains a name will be followed by a line contains the
#grade. 

def main():
    studentfile=open('students.txt','w')
    for i in range(1):
        name=input('Enter a name ')
        grade=int(input('Enter a grade ... '))
        studentfile.write(name+'\n')
        studentfile.write(str(grade)+'\n')
    studentfile.close()
main()