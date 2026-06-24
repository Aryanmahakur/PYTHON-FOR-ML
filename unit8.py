# ==========================
# CLASS, OBJECT, CONSTRUCTOR
# ==========================

# Class
# A class is a blueprint/template for creating objects.

class Student:

    # Constructor
    # __init__() is automatically called when an object is created.
    # It initializes the object's data.

    def __init__(self, name, age):

        # Instance Variables
        # Data belonging to each object

        self.name = name
        self.age = age

    # Method
    # Function inside a class

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Object Creation
# s1 is an object (instance) of Student class

s1 = Student("Aryan", 18)

# Calling Method using Object

s1.display()

# Output:
# Name: Aryan
# Age: 18