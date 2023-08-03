#Your program should read only the grades to a two-dimensional list (ignore   
#the name). Then calculate the average of each student (row) and add it as the
#fourth column in the list.

def main(): 
    myfile=open('/Users/abdullah/Desktop/programming concepts/students.txt','r')
    lines=myfile.readlines()
    myfile.close()
    twodimlist=[]
    i=0
    for line in lines:
        line=line.split(',')
        i=0
        while i<len(line):          #remove /n
            line[i]=line[i].strip()
            i=i+1
        line=line[1:]   #remove name
        k=0
        while k<len(line):          #convert to integer
            line[k]=int(line[k])
            k=k+1
        avg=(line[0]+line[1]+line[2])/3      #avg
        row=[]
        for grade in line:
            row.append(grade)
        row.append(avg)
        twodimlist.append(row)
    print(twodimlist)
main()