# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class
class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    # Override Parent display()
    def display(self):

        # Call Parent display()
        super().display()

        # Child-specific display
        print("Course:", self.course)


s1 = Student("Aryan", 18, "Python")

s1.display()