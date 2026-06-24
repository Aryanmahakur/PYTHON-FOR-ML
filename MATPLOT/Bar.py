import matplotlib.pyplot as plt

# Categories (X-axis)
products = ["Laptop", "Mobile", "Tablet", "TV"]

# Values (Y-axis)
sales = [50, 80, 40, 60]

# Bar Chart
plt.bar(
    products,          # Categories
    sales,             # Values
    color="blue",      # Bar color
    width=0.5,         # Bar width
    label="Sales"      # Legend name
)

# Labels
plt.xlabel("Products")
plt.ylabel("Sales")

# Title
plt.title("Product Sales")

# Grid
plt.grid(True)

# Legend
plt.legend()


# Show Plot
plt.show()