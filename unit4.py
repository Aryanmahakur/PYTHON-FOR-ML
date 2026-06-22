# ==========================
# Loops in Python
# ==========================

# --------------------------
# for Loop
# --------------------------

# Used when the number of iterations is known

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


# --------------------------
# while Loop
# --------------------------

# Used when the number of iterations is not known

i = 1

while i <= 5:
    print(i)
    i += 1

# Output:
# 1 2 3 4 5


# --------------------------
# Nested Loops
# --------------------------

# Loop inside another loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# ...


# --------------------------
# break Statement
# --------------------------

# Terminates the loop immediately

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Output:
# 1 2 3 4


# --------------------------
# continue Statement
# --------------------------

# Skips the current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1 2 4 5


# --------------------------
# pass Statement
# --------------------------

# Placeholder statement; does nothing

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# Output:
# 1 2 3 4 5


# --------------------------
# Example: Multiplication Table
# --------------------------

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)