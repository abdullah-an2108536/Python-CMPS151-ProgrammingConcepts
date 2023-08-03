time=int(input('enter time in seconds = '))

hours=time//3600
time=time%3600
minutes=time//60
seconds=time%60

print('Times is :   ', hours ,':',minutes,':', seconds )

