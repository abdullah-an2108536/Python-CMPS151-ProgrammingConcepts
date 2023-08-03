#Use for loop to print the numbers from 1 to 10 and their squares in a table that
#has two columns: the number and its square.

limit=int(input('Enter ending limit :'))
print('Number\tSquare')
print('-------------')
for i in range(1,limit+1):
    print(i,'\t',i**2)