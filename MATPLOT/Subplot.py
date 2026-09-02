import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])
z = np.array([5, 15, 10, 20, 25])

# Create 2 rows × 2 columns
fig = plt.figure(figsize=(10, 8))

# ---------------- 1. 2D Line Plot ----------------
ax1 = fig.add_subplot(2, 2, 1)

ax1.plot(x, y, marker='o')
ax1.set_title("2D Line Plot")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")


# ---------------- 2. 2D Bar Plot ----------------
ax2 = fig.add_subplot(2, 2, 2)

ax2.bar(x, y)
ax2.set_title("2D Bar Plot")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")


# ---------------- 3. 2D Scatter Plot ----------------
ax3 = fig.add_subplot(2, 2, 3)

ax3.scatter(x, y)
ax3.set_title("2D Scatter Plot")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")


# ---------------- 4. 3D Scatter Plot ----------------
ax4 = fig.add_subplot(2, 2, 4, projection="3d")

ax4.scatter(x, y, z)
ax4.set_title("3D Scatter Plot")
ax4.set_xlabel("X")
ax4.set_ylabel("Y")
ax4.set_zlabel("Z")


# Adjust spacing
plt.tight_layout()

# Display
plt.show()