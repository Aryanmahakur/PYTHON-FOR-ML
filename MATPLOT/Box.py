import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 62, 65, 68, 70, 72,
         75, 78, 80, 82, 85, 88, 90, 95, 120]

# Box Plot
plt.boxplot(
    marks,
    vert=True,         # Vertical boxplot
    patch_artist=True, # Fill color
    labels=["Marks"]   # Box label
)

# Labels
plt.ylabel("Marks")

# Title
plt.title("Marks Distribution")

# Grid
plt.grid(True)

# Show Plot
plt.show()