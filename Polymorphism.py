class Person:
    def __init__(self, name):
        self.name = name

    def display_role(self):
        print("I am a person")


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display_role(self):
        print(f"{self.name} is a Student")
        print(f"Marks: {self.marks}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display_role(self):
        print(f"{self.name} is a Teacher")
        print(f"Subject: {self.subject}")


class Principal(Person):
    def __init__(self, name, experience):
        super().__init__(name)
        self.experience = experience

    def display_role(self):
        print(f"{self.name} is a Principal")
        print(f"Experience: {self.experience} years")


people = [
    Student("Aryan", 95),
    Teacher("Rahul", "Python"),
    Principal("Sharma", 15)
]

for person in people:
    person.display_role()
    print("-" * 30)