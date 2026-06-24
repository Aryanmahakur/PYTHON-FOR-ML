import matplotlib.pyplot as plt

# X-axis values
days = [1, 2, 3, 4, 5]

# Y-axis values
sales = [100, 150, 120, 180, 200]

# Line Plot
plt.plot(
    days,                  # X values
    sales,                 # Y values
    color="red",           # Line color
    linestyle="--",        # Line style (-, --, :, -.)
    linewidth=3,           # Thickness of line
    marker="o",            # Marker on each point
    markersize=8,          # Marker size
    label="Sales"          # Legend name
)

# Labels
plt.xlabel("Days")         # X-axis label
plt.ylabel("Sales")        # Y-axis label

# Title
plt.title("Sales Trend")

# Grid
plt.grid(True)

# Legend
plt.legend()

# Show Plot
plt.show()