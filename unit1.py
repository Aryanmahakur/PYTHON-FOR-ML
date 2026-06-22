# ==========================
# Python Basics
# ==========================

# print() -> used to display output
print("Hello World")
print(10)

# --------------------------
# Variables
# --------------------------

name = "Aryan"      # String variable
age = 18            # Integer variable
salary = 25000.5    # Float variable
is_student = True   # Boolean variable

print(name)
print(age)
print(salary)
print(is_student)

# --------------------------
# Data Types
# --------------------------

x = 10
print(type(x))      # int

y = 10.5
print(type(y))      # float

z = "Python"
print(type(z))      # str

a = False
print(type(a))      # bool

# --------------------------
# Type Conversion
# --------------------------

num = 100

# int to float
num_float = float(num)
print(num_float)

# int to string
num_str = str(num)
print(num_str)

# string to int
text = "200"
text_int = int(text)
print(text_int)

# float to int
value = 15.9
value_int = int(value)
print(value_int)    # Decimal part removed

# --------------------------
# Input / Output
# --------------------------

name = input("Enter your name: ")      # Takes string input
print("Name:", name)

age = int(input("Enter your age: "))   # Convert input to int
print("Age:", age)

salary = float(input("Enter salary: ")) # Convert input to float
print("Salary:", salary)

# --------------------------
# Example Program
# --------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("You are", age, "years old")