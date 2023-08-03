#mid term last question. output number without leftmost digit.

x=int(input('Enter a non negative interger: '))
while x<0:
    print('Invalid input. Your input is negative')
    x=int(input('Enter a non negative interger: '))
x2=x
digit=x
while digit>10:           #find first digit
    digit=digit//10
count=0
while x2!=0:            #find number of digits
    x2=x2//10
    count=count+1
subt=10
for i in range(count-2):       #1000/10/100/10000000
    subt=subt*10
subt2=subt*digit
final=x-subt2
if final<0:
    final=0
print('final=',final)