# Write a program that reads data of 10 employees, for each employee the user
# inputs employee’s name, and salary. Your program should display the employee’s
# name that has the highest salary.

max=0
name_max='name'
for i in range(10):
    name=input('Enter employee name ... ')
    salary=int(input('Enter Salary'))
    if salary>max:
        salary=max
        name_max=name
print('Employee with the highest salary is...',name_max,'his salary is....',max)
