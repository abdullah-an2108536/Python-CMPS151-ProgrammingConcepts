salary = int(input('Enter Salary : ')) 
children = int(input('Enter number of children : ')) 

if (salary<30000):
    tax=0.1*salary
elif (salary>=30000) and (children>=3):
    tax=0.2*salary
elif (salary>=30000) and (children<3):
    tax=0.3*salary

net=salary-tax
print('net_salary :%.2f' %net)