# ==========================
# COLLECTIONS IN PYTHON
# List, Tuple, Set, Dictionary
# ==========================

# ==================================================
# LIST METHODS
# Ordered, Mutable, Allows Duplicates
# ==================================================

nums = [1, 2, 3]

nums.append(4)              # Add one element
print(nums)                 # [1, 2, 3, 4]

nums.extend([5, 6])         # Add multiple elements
print(nums)                 # [1, 2, 3, 4, 5, 6]

nums.insert(1, 100)         # Insert at index 1
print(nums)                 # [1, 100, 2, 3, 4, 5, 6]

nums.remove(100)            # Remove value 100
print(nums)

nums.pop()                  # Remove last element
print(nums)

print(nums.index(3))        # Index of 3

print(nums.count(2))        # Count occurrences of 2

nums.sort()                 # Sort ascending
print(nums)

nums.reverse()              # Reverse list
print(nums)

copy_nums = nums.copy()     # Copy list
print(copy_nums)

nums.clear()                # Remove all elements
print(nums)                 # []

# ==================================================
# TUPLE METHODS
# Ordered, Immutable, Allows Duplicates
# ==================================================

t = (1, 2, 3, 2, 5)

print(t.count(2))           # 2

print(t.index(3))           # 2

# ==================================================
# SET METHODS
# Unordered, Mutable, No Duplicates
# ==================================================

s = {1, 2, 3}

s.add(4)                    # Add one element
print(s)

s.update([5, 6])            # Add multiple elements
print(s)

s.remove(2)                 # Remove element
print(s)

s.discard(10)               # No error if value absent
print(s)

removed = s.pop()           # Remove random element
print(removed)

s2 = {5, 6, 7}

print(s.union(s2))          # Combine sets

print(s.intersection(s2))   # Common elements

print(s.difference(s2))     # Elements only in s

s.clear()                   # Remove all elements
print(s)

# ==================================================
# DICTIONARY METHODS
# Key : Value Pairs
# ==================================================

student = {
    "name": "Aryan",
    "age": 18
}

print(student.keys())       # dict_keys(['name', 'age'])

print(student.values())     # dict_values(['Aryan', 18])

print(student.items())      # All key-value pairs

print(student.get("name"))  # Aryan

student.update({"city": "Bangalore"})
print(student)

student.pop("age")          # Remove key
print(student)

student["course"] = "Python"  # Add new key
print(student)

copy_dict = student.copy()  # Copy dictionary
print(copy_dict)

student.clear()             # Remove everything
print(student)              # {}


# ==========================
# ITERATION IN COLLECTIONS
# List, Tuple, Set, Dictionary
# ==========================

# --------------------------
# List Iteration
# --------------------------

nums = [10, 20, 30, 40]

for i in nums:
    print(i)

# Output:
# 10
# 20
# 30
# 40


# --------------------------
# Tuple Iteration
# --------------------------

t = (1, 2, 3, 4)

for i in t:
    print(i)

# Output:
# 1
# 2
# 3
# 4


# --------------------------
# Set Iteration
# --------------------------

s = {100, 200, 300}

for i in s:
    print(i)

# Output order may vary because sets are unordered


# --------------------------
# Dictionary Iteration
# --------------------------

student = {
    "name": "Aryan",
    "age": 18,
    "city": "Bangalore"
}

# Iterate Keys

for key in student:
    print(key)

# Output:
# name
# age
# city


# Iterate Values

for value in student.values():
    print(value)

# Output:
# Aryan
# 18
# Bangalore


# Iterate Key-Value Pairs

for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Aryan
# age : 18
# city : Bangalore


# --------------------------
# Iteration with Index
# --------------------------

nums = [10, 20, 30]

for index, value in enumerate(nums):
    print(index, value)

# Output:
# 0 10
# 1 20
# 2 30