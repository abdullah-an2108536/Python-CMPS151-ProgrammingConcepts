#sum=0
#for x in range(1,31):
#    for j in range(30,0,-1):
#        sum=sum+(x/j)
#print(sum)

sum=0
for i in range(1,31):
    j=31-i
    term=i/j
    sum+=term
print("Total:",sum)

