# ==========================
# Operators in Python
# ==========================

# --------------------------
# Arithmetic Operators
# --------------------------

a = 10
b = 3

print(a + b)   # Addition = 13
print(a - b)   # Subtraction = 7
print(a * b)   # Multiplication = 30
print(a / b)   # Division = 3.3333
print(a // b)  # Floor Division = 3
print(a % b)   # Modulus (Remainder) = 1
print(a ** b)  # Power = 1000

# --------------------------
# Comparison Operators
# --------------------------

x = 10
y = 20

print(x == y)  # Equal to -> False
print(x != y)  # Not equal to -> True
print(x > y)   # Greater than -> False
print(x < y)   # Less than -> True
print(x >= y)  # Greater than or equal -> False
print(x <= y)  # Less than or equal -> True

# --------------------------
# Logical Operators
# --------------------------

a = True
b = False

print(a and b)  # True if both are True -> False
print(a or b)   # True if at least one is True -> True
print(not a)    # Opposite value -> False

# --------------------------
# Assignment Operators
# --------------------------

num = 10

num += 5    # num = num + 5
print(num)  # 15

num -= 3    # num = num - 3
print(num)  # 12

num *= 2    # num = num * 2
print(num)  # 24

# --------------------------
# Membership Operators
# --------------------------

text = "Python"

print("P" in text)        # True
print("z" in text)        # False
print("z" not in text)    # True

numbers = [10, 20, 30]

print(20 in numbers)      # True
print(50 not in numbers)  # True

# --------------------------
# Identity Operators
# --------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (same object)
print(a is c)      # False (different objects)
print(a is not c)  # True

# --------------------------
# Combined Example
# --------------------------

x = 5
y = 2

print(x + y)            # Arithmetic
print(x > y)            # Comparison
print(x > 0 and y > 0)  # Logical

x += 10                 # Assignment
print(x)

name = "Aryan"
print("A" in name)      # Membership

a = [1, 2]
b = a
print(a is b)           # Identity