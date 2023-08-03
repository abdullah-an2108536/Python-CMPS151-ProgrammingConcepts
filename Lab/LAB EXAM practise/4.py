f=open('text.txt','r')
lines=f.readlines()
f.close()
f=open('tickets.txt','w')
i=0
while i<len(lines):
    lines[i]=lines[i].strip()
    i=i+1
for line in lines:
    linelist=line.split(':')
    linelist=linelist[1:]
    ticket=''
    if int(linelist[1])>=90 and int(linelist[1])<=100:
        ticket='300'
    elif int(linelist[1])>=101 and int(linelist[1])<=110:
        ticket='400'
    else:
        ticket='500'
    script=linelist[0]+'-'+ticket
    f.write(script+'\n')
print(lines)
f.close()