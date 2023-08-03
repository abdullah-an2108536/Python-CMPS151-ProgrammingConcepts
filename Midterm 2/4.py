try:
    myfile=open('/Users/abdullah/Desktop/programming concepts/Course Content/M2/sample 1/data.txt','r')
    contents=myfile.readlines()
    myfile.close()
    sum=0
    for i in range(len(contents)):
        contents[i]=contents[i].strip()
    for i in range(len(contents)):
        contents[i]=float(contents[i])
    for content in contents:
        sum=sum+content
    print(len(contents),'read')
    print(sum)
    print(sum/len(contents))


except FileNotFoundError as err:
    print(err)
