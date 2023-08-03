#Write a program to read from the user the elements (integers) of a list that has three
#rows and three columns. Then calculate and output the total of the elements in the
#primary diagonal and the total of the elements in the secondary diagonal of the list. 

userlist=[]
for i in range(3):
    row=[]
    for j in range(3):
        x=int(input('enter integer....'))
        row.append(x)
    userlist.append(row)
print(userlist)

total_primary=0
for i in range(3):
    total_primary+=userlist[i][i]
print("Total of elements in the primary diagonal:",total_primary)

total_secondary=0
for i in range(3):
    j=2-i
    total_secondary+=userlist[i][j]
print("Total of elements in the secondary diagonal:",total_secondary)