#Write a function split that receives a list of integers and returns two lists:
#one includes only odd numbers and the other one includes only even
#numbers. Test split function. 

def split(list):
    odd=[]
    even=[]
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

def main():
    mylist=[2,3,4,5,6,7]
    odd,even=split(mylist)
    print('odd=',odd)
    print('even',even)

main()
