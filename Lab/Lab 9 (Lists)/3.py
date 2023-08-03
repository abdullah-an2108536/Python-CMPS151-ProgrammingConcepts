#Write a function union that receives two lists and returns one list that
#represents the union between the elements in the two lists. Remember
#union between two lists should not have duplicated elements. Test your
#function

def union(list1,list2):
    unionlist=[]
    for i in list1:
        if i in list2:
            unionlist.append(i)
    return unionlist

def main():
    x=[1,2,3,4,5,6,7,8]
    y=[3,4,5,6]
    unionlist=union(x,y)
    print(unionlist)

main()
