# ==========================
# FUNCTIONS IN PYTHON
# ==========================

# --------------------------
# Creating Functions
# --------------------------

def greet():
    print("Hello World")

greet()                     # Hello World


# --------------------------
# Arguments
# --------------------------

def greet(name):
    print("Hello", name)

greet("Aryan")              # Hello Aryan


# --------------------------
# Return Statement
# --------------------------

def add(a, b):
    return a + b

result = add(10, 20)

print(result)               # 30


# --------------------------
# Default Arguments
# --------------------------

def greet(name="Guest"):
    print("Hello", name)

greet()                     # Hello Guest
greet("Aryan")              # Hello Aryan


# --------------------------
# Keyword Arguments
# --------------------------

def student(name, age):
    print(name, age)

student(age=18, name="Aryan")   # Aryan 18


# --------------------------
# *args
# --------------------------

# Accepts multiple positional arguments
# Stored as a tuple

def total(*args):
    print(args)

total(10, 20, 30, 40)

# Output:
# (10, 20, 30, 40)


def total(*args):
    print(sum(args))

total(10, 20, 30)

# Output:
# 60


# --------------------------
# **kwargs
# --------------------------

# Accepts multiple keyword arguments
# Stored as a dictionary

def details(**kwargs):
    print(kwargs)

details(name="Aryan", age=18)

# Output:
# {'name': 'Aryan', 'age': 18}


def details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

details(name="Aryan", age=18)

# Output:
# name : Aryan
# age : 18


# --------------------------
# Lambda Functions
# --------------------------

# Anonymous one-line function

square = lambda x: x * x

print(square(5))            # 25


add = lambda a, b: a + b

print(add(10, 20))          # 30


# --------------------------
# Function Returning Multiple Values
# --------------------------

def calc(a, b):
    return a+b, a-b

x, y = calc(10, 5)

print(x)                    # 15
print(y)                    # 5


# --------------------------
# Complete Example
# --------------------------

def student(name, age=18):
    return f"Name: {name}, Age: {age}"

print(student("Aryan"))

# Output:
# Name: Aryan, Age: 18