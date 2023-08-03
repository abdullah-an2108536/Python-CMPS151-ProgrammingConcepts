def addstudent():
    myfile = open("students.txt", "a")
    student_id = int(input("Enter student id : "))
    name = input("Enter student name : ")
    grade = float(input("Enter student grade : "))
    myfile.write(str(student_id) + "\n")
    myfile.write(name + "\n")
    myfile.write(grade + "\n")
    myfile.close()


def displayStudents():
    myfile = open("students.txt", "r")
    id = myfile.readline().strip("\n")
    while id != "":
        name = myfile.readline().strip("\n")
        grade = myfile.readline().strip("\n")
        print(id, name, grade)
        id = myfile.readline().strip("\n")
    myfile.close()


def displayAvg():
    myfile = open("students.txt", "r")
    id = myfile.readline().strip("\n")
    total = 0
    count = 0
    while id != "":
        name = myfile.readline().strip("\n")
        grade = myfile.readline().strip("\n")
        total = total + float(grade)
        count = count + 1
        id = myfile.readline().strip("\n")
    myfile.close()
    avg = total / count
    print("The average grade : ", avg)


def displayTop():
    myfile = open("students.txt", "r")
    id = myfile.readline().strip("\n")
    max = 0
    topname = ""
    while id != "":
        name = myfile.readline().strip("\n")
        grade = myfile.readline().strip("\n")
        if float(grade) > max:
            max = float(grade)
            topname = name
    myfile.close()


def deletestudent(filename, delete_id):
    myfile = open(filename, "r")
    tempfile = open("temp.txt", "w")
    id = myfile.read().strip()
    found = False
    while id != "":
        name = myfile.read().strip()
        grade = myfile.read().strip()
        if id != delete_id:
            tempfile.write()