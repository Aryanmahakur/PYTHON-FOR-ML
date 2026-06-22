# ==========================
# Conditional Statements
# ==========================

# --------------------------
# if Statement
# --------------------------

age = 18

if age >= 18:
    print("You can vote")

# --------------------------
# if-else Statement
# --------------------------

num = 5

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# --------------------------
# if-elif-else Statement
# --------------------------

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")

# --------------------------
# Nested if Statement
# --------------------------

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Not Eligible")

# --------------------------
# Example Program
# --------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")