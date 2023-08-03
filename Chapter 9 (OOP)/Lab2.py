# Modify _ _init_ _method in Q 1 to receive initial values for the attributes,
# and update the code that creates the objects.
# Then replace the salary of the second object by 20000, and print the objects’
# sates after this update.

class Employee:
    def __init__(self,i,n,s):
        self.id = i
        self.name = n
        self.salary = s

    def increaseSalary(self, percent_increase):
        self.salary += self.salary * percent_increase

    def __str__(self):
        return (
            "id = "
            + str(self.id)
            + "\nname = "
            + self.name
            + "\nsalary = "
            + str(self.salary)
        )


employee1 = Employee(123,'Ahmed',15000)

employee2 = Employee(456,'Sara',25000)

employee2.salary=20000

print(employee2)
