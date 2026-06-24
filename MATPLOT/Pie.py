import matplotlib.pyplot as plt

# Data
products = ["Laptop", "Mobile", "Tablet", "TV"]

sales = [40, 30, 20, 10]

# Pie Chart
plt.pie(
    sales,                # Values
    labels=products,      # Labels
    autopct="%1.1f%%",    # Show percentage
    startangle=90,        # Starting angle
    explode=(0.1,0,0,0), # Separate slice
    shadow=True           # Shadow effect
)

# Title
plt.title("Product Sales Share")

# Show Plot
plt.show()