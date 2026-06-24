import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75,
         78, 80, 82, 85, 88, 90, 92, 95]

# Histogram
plt.hist(
    marks,          # Data
    bins=5,         # Number of intervals
    color="blue",   # Bar color
    edgecolor="black", # Border color
    label="Marks"
)

# Labels
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Title
plt.title("Marks Distribution")

# Grid
plt.grid(True)

# Legend
plt.legend()

# Show Plot
plt.show()