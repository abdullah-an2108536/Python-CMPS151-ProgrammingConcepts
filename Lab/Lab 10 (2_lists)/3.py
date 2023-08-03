#Write a function convert(x) that receives any two-dim l list and returns
#one-dimensional list that contains all elements of x.

def convert(x):
    finallist=[]
    for i in range(len(x)):
        for j in range(len(x[0])):
            finallist.append(x[i][j])
    return finallist

print(convert([[1,2,3],[4,5,6],[7,8,9]]))