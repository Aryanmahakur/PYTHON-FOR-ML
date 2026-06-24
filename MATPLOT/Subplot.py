import matplotlib.pyplot as plt

# First Plot
plt.subplot(2, 2, 1)
plt.plot([1,2,3,4], [10,20,15,25])
plt.title("Line Plot")

# Second Plot
plt.subplot(2, 2, 2)
plt.scatter([1,2,3,4], [10,20,15,25])
plt.title("Scatter Plot")

# Third Plot
plt.subplot(2, 2, 3)
plt.bar(["A","B","C"], [10,20,15])
plt.title("Bar Chart")

# Fourth Plot
plt.subplot(2, 2, 4)
plt.hist([10,20,20,30,40,40,40,50])
plt.title("Histogram")

plt.tight_layout()

plt.show()