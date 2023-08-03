# This program gets employee data from the user and
# saves it as records in the employee.txt file.

def main():
    num_emps=int(input('How many records .... '))
    empfile=open('employee.txt','w')
    for count in range(1,num_emps+1):
        print('Enter data for employee #',count,'...')
        name=input('Enter name')
        empfile.write(name+'\n')
        id=input('Enter id for employee ')
        empfile.write(id+'\n')
        dep=input('Enter dep for employee ')
        empfile.write(dep+'\n')
    empfile.close()

main()


