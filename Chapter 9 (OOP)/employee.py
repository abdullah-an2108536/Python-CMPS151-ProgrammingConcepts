#   Create a class Employee that has two private attributes ,
#   name(string), salary(float), add the following methods:
#   • __str__ to display student’s state.
#   • Setter/getter for every private data
#   • netSalary that returns the net salary by deducting 15% as a
#   tax from the salary.
#   Then create two employee objects.
#   Update their salaries.
#   call method netSalary for each one of them.

class Employee:
    def __init__(self,a,b):
        self.__name=a
        self.__salary=b
    def __str__(self):
        return 'name = '+self.__name+'\nsalary = '+str(self.__salary)
    def setname(self,name):
        self.__name=name
    def setsalary(self,salary):
        self.__salary=salary
    def getname(self):
        return self.__name
    def getsalary(self):
        return self.__salary
    def netsalary(self):
        return (self.__salary-(self.__salary*0.15))

emp1=Employee('Abdullah',3500)
emp1.setsalary(4000)
print(emp1)
print('NET = ',emp1.netsalary())

emp2=Employee('Ansha',689)
print(emp2)