#sum = 0
#count = 0
#for i in range(8, 281, 4):
#    sum = sum+i
#    count = count+1
#print('sum...', sum)
#print('Average...', sum/count)

sum = 0
count = 0
for i in range(8, 281):
    if i%4==0:
        sum = sum + i
        count = count + 1
print('sum...', sum)
print('Average...', sum/count)