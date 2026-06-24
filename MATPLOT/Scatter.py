import matplotlib.pyplot as plt

# X-axis values
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]

# Y-axis values
marks = [35, 40, 50, 55, 65, 70, 80, 90]

# Scatter Plot
plt.scatter(
    hours_studied,      # X values
    marks,              # Y values
    color="red",        # Point color
    marker="o",         # Point shape
    s=100,              # Point size
    label="Students"    # Legend name
)

# Labels
plt.xlabel("Hours Studied")

plt.ylabel("Marks")

# Title
plt.title("Hours Studied vs Marks")

# Grid
plt.grid(True)

# Legend
plt.legend()

# Axis Limits (Optional)
plt.xlim(0, 9)
plt.ylim(0, 100)

# Tick Values (Optional)
plt.xticks(range(0, 10))
plt.yticks(range(0, 101, 10))

# Show Plot
plt.show()