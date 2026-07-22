import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample Data
x = [10, 20, 30, 40, 50]
y = [100, 200, 150, 300, 250]

# Style

# Figure Size
plt.figure(figsize=(8, 5), dpi=100)

# Plot
plt.plot(
    x,
    y,
    label="Sales",
    color="blue",
    marker="o"
)

# Title and Labels
plt.title(
    "Sales Report",
    fontsize=15,
    color="black",
    fontweight="bold"
)

plt.xlabel(
    "Month",
    fontsize=12,
    color="green",
    fontweight="bold"
)

plt.ylabel(
    "Revenue",
    fontsize=12,
    color="red",
    fontweight="bold"
)

# Legend
plt.legend(
    loc="upper left",
    fontsize=10,
    title="Data"
)

# Grid
plt.grid(
    True,
    color="gray",
    linestyle="--",
    linewidth=0.5
)

# Axis Limits
plt.xlim(0, 60)
plt.ylim(0, 350)

# Ticks
plt.xticks(range(0, 61, 10))
plt.yticks(range(0, 351, 50))

# Save Figure
plt.savefig(
    "plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================
# 3D Plot Example
# ==========================

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection="3d")

z = [5, 10, 15, 20, 25]

ax.scatter(
    x,
    y,
    z
)

ax.plot(
    x,
    y,
    z
)

ax.set_title("3D Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()