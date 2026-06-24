# ==========================
# Strings in Python
# ==========================

# --------------------------
# Creating Strings
# --------------------------

name = "Python"

print(name)                 # Python

# --------------------------
# Indexing
# --------------------------

text = "Python"

print(text[0])              # P
print(text[1])              # y
print(text[-1])             # n
print(text[-2])             # o

# --------------------------
# Slicing
# --------------------------

text = "Python"

print(text[0:3])            # Pyt
print(text[2:5])            # tho
print(text[:4])             # Pyth
print(text[3:])             # hon
print(text[:])              # Python
print(text[::-1])           # nohtyP

# --------------------------
# String Methods
# --------------------------

text = "hello world"

print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(text.title())         # Hello World
print(text.capitalize())    # Hello world
print(text.swapcase())      # HELLO WORLD

print(text.replace("world", "Python"))  # hello Python
print(text.count("o"))                  # 2
print(text.find("world"))               # 6
print(text.index("world"))              # 6

print(text.startswith("hello"))         # True
print(text.endswith("world"))           # True

print(text.split())                     # ['hello', 'world']
print("-".join(["A", "B", "C"]))        # A-B-C

print(text.strip())                     # hello world
print(text.lstrip())                    # hello world
print(text.rstrip())                    # hello world

print(text.isalpha())                   # False
print("Hello".isalpha())                # True

print("123".isdigit())                  # True
print("abc123".isalnum())               # True

# --------------------------
# String Formatting
# --------------------------

name = "Aryan"
age = 18

print(f"My name is {name}")             # My name is Aryan
print(f"I am {age} years old")          # I am 18 years old

# Expressions inside f-string

a = 10
b = 20

print(f"Sum = {a+b}")                   # Sum = 30
print(f"Product = {a*b}")               # Product = 200

# Decimal Formatting

pi = 3.14159265

print(f"{pi:.2f}")                      # 3.14
print(f"{pi:.3f}")                      # 3.142