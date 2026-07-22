# ==========================
# Python Basics
# ==========================

# print() -> Used to display output on the screen
print("Hello World")      # Output: Hello World
print(10)                 # Output: 10

# --------------------------
# Variables
# --------------------------

# Variables store data in memory

name = "Aryan"       # String (str) | No Output
age = 18             # Integer (int) | No Output
salary = 25000.5     # Float (decimal number) | No Output
is_student = True    # Boolean (True or False) | No Output

# Print the values stored in variables
print(name)          # Output: Aryan
print(age)           # Output: 18
print(salary)        # Output: 25000.5
print(is_student)    # Output: True

# --------------------------
# Data Types
# --------------------------

x = 10               # No Output
print(type(x))       # Output: <class 'int'>

y = 10.5             # No Output
print(type(y))       # Output: <class 'float'>

z = "Python"         # No Output
print(type(z))       # Output: <class 'str'>

a = False            # No Output
print(type(a))       # Output: <class 'bool'>

# --------------------------
# Type Conversion
# --------------------------

num = 100            # No Output

# Convert integer to float
num_float = float(num)      # No Output
print(num_float)            # Output: 100.0

# Convert integer to string
num_str = str(num)          # No Output
print(num_str)              # Output: 100

# Convert string to integer
text = "200"  
print(text)              # No Output
text_int = int(text)        # No Output
print(text_int)             # Output: 200

# Convert float to integer
value = 15.9                # No Output
value_int = int(value)      # No Output
print(value_int)            # Output: 15

# --------------------------
# Input / Output
# --------------------------

# input() always returns a string

name = input("Enter your name: ")
# Displays: Enter your name:
# Example Input: Aryan

print("Name:", name)        # Output: Name: Aryan

# Convert input to integer
age = int(input("Enter your age: "))
# Displays: Enter your age:
# Example Input: 18

print("Age:", age)          # Output: Age: 18

# Convert input to float
salary = float(input("Enter salary: "))
# Displays: Enter salary:
# Example Input: 25000.5

print("Salary:", salary)    # Output: Salary: 25000.5

# --------------------------
# Example Program
# --------------------------

# Take user's name
name = input("Enter your name: ")
# Displays: Enter your name:
# Example Input: Aryan

# Take user's age and convert to integer
age = int(input("Enter your age: "))
# Displays: Enter your age:
# Example Input: 18

# Display greeting
print("Hello", name)        # Output: Hello Aryan

# Display age
print("You are", age, "years old")    # Output: You are 18 years old