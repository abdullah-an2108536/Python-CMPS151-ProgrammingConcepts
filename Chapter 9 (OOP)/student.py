# Create a class Student that has three attributes id (int),
# name(string), gpa(float), add method __str__ to display
# student’s state. Then create two student objects.


class Student:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.gpa = 0.00

    def __str__(self):
        return (
            "id = "
            + str(self.id)
            + "\nname = "
            + self.name
            + "\nGPA = "
            + str(self.gpa)
        )


# -------------------------------------------------------------------------------
student1 = Student()
student1.id = 8977
student1.name = "Abdullah"
student1.gpa = 3.65
print(student1, "\n")  # __str__ function is used like this

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


class Student:
    def __init__(self, i, n, g):
        self.id = i
        self.name = n
        self.gpa = g

    def __str__(self):
        return (
            "id = "
            + str(self.id)
            + "\nname = "
            + self.name
            + "\nGPA = "
            + str(self.gpa)
        )


student2 = Student(8842, "John", 3.84)
print(student2)
