# This program displays the records that are
# in the employees.txt file.

def main():
    empfile=open('employee.txt','r')
    name=empfile.readline().strip()
    while name!='':
        id=empfile.readline().strip()
        dep=empfile.readline().strip()
        print('name  ..',name)
        print('id  ..',id)
        print('dep  ..',dep)
        name=empfile.readline().strip()
    empfile.close()
main()