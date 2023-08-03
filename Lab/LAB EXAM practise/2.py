def minimum(list,x):
    if x>len(list):
        print('error')
        exit
    list2=list[x:]
    return min(list2)
    

print(minimum([1,2,7,6,9,8,5,10],4))

