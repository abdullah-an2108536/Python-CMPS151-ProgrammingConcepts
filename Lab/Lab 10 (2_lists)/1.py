#Q1 Assume you have a list x=[[2,4],[1,6],[9,5],[-2,8]], using loops, write a
#program to display the total of the rows, and the total of the columns in this
#list.

x=[[2,4],
[1,6],
[9,5],[
    -2,8]]

def totalrows(list):
    totallist=[]
    for i in range(len(list)):
        sum=0
        for j in range(len(list[0])):
            sum+=list[i][j]
        totallist.append(sum)
    return totallist

print(totalrows(x))

def totalcolumns(list):
    totallist=[]
    for i in range(len(list[0])):
        sum=0
        for j in range(len(list)):
            sum+=list[j][i]
        totallist.append(sum)
    return totallist

print(totalcolumns(x))