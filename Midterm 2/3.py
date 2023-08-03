line='North, 2550, 4500, 7000, 4000'
sum=0
list=line.split(',')
list2=list[1:]
for i in list2:
    sum=sum+int(i)
print(sum)
print(sum/4)