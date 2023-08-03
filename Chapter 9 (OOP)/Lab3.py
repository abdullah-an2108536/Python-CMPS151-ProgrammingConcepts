# Modify the code in Q2 by making all the attributes private.
# • Add setter/ getter methods to each one of them (set_id,get_id,
# set_name,get_name, set_salary, get_salary). In method set_salary,
# ensure that the salary always is a positive, otherwise make it zero.
# • Update the code that replaces the salary of the second object.
# • Calculate and output the total of the salaries of the three objects.


class Employee:
    def __init__(self, i, n, s):
        self.__id = i
        self.__name = n
        self.__salary = s

    def increaseSalary(self, percent_increase):
        self.__salary += self.__salary * percent_increase

    def set__id(self, i):
        self.__id = i

    def set__name(self, n):
        self.__name = n

    def set__salary(self, s):
        self.__salary = s
        if self.__salary < 0:
            self.__salary = 0

    def get__id(self):
        return self.__id

    def get__name(self):
        return self.__name

    def get__salary(self):
        return self.__salary

    def __str__(self):
        return (
            "id = "
            + str(self.id)
            + "\nname = "
            + self.name
            + "\nsalary = "
            + str(self.salary)
        )


employee1 = Employee(123, "Ahmed", 15000)
employee1.increaseSalary(10)

employee2 = Employee(456, "Sara", 25000)

employee2.set__salary(20000)

total = employee1.get__salary() + employee2.get__salary()
print(total)
