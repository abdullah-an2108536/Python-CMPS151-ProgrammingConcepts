class Employee:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.salary = 0

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


employee1 = Employee()
employee1.id = 123
employee1.name = "Ahmed"
employee1.salary = 15000

employee2 = Employee()
employee2.id = 456
employee2.name = "Sara"
employee2.salary = 25000

employee1.increaseSalary(0.1)

print(employee1)
print()
print(employee2)
