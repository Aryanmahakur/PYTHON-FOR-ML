import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# ----------------------------
# Dataset already loaded
# ----------------------------
# Example:
# df = pd.read_csv("data.csv")

# Select ONLY 2 features
X = df[["Feature1", "Feature2"]].values

# Target column
y = df["Target"].values

# ----------------------------
# Train model
# ----------------------------
model = LogisticRegression()
model.fit(X, y)

# ----------------------------
# Create mesh grid
# ----------------------------
x_min = X[:, 0].min() - 1
x_max = X[:, 0].max() + 1

y_min = X[:, 1].min() - 1
y_max = X[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.02),
    np.arange(y_min, y_max, 0.02)
)

# ----------------------------
# Predict every point
# ----------------------------
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# ----------------------------
# Plot decision boundary
# ----------------------------
plt.figure(figsize=(8,6))

# Decision regions
plt.contourf(xx, yy, Z, alpha=0.3)

# Original data points
plt.scatter(
    X[:,0],
    X[:,1],
    c=y,
    edgecolor="black"
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Decision Boundary")
plt.show()