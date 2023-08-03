#Which contains students’ grades, each entry has student name (key), and a
#list of three grades (value). The grades represent student’s grades in math,
#science, English. Write a program to output the average, and to print the
#name of the student who has the minimum grade in English.

grades={'Ahmed':[60,23,50],"Naser":[90,80,70],"Sara":[77,89,99],'Nouf':[44,55,76]}
max=100
maxname=''
for k,v in grades.items():
    avg=sum(v)/3
    print(k,avg)
    if v[2]<max:
        max=v[2]
        maxname=k
print(maxname)

grades={'Ahmed':[60,23,50],"Naser":[90,80,0],"Sara":[77,89,99],'Nouf':[44,55,76]}
for k,v in grades.items():
    print(k,sum(v)/len(v))
min=100
for k,v in grades.items():
    if v[2]<min:
        min=v[2]
        name=k
print(name)