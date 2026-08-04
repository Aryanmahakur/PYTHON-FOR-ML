import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set a consistent background style for clean output
sns.set_theme(style="darkgrid")

# Create a sample synthetic dataset for all plots
np.random.seed(42)
n = 200

df = pd.DataFrame(
    {
        "Age": np.random.randint(18, 65, size=n),
        "Salary": np.random.randint(30000, 120000, size=n),
        "Sales": np.random.randint(100, 500, size=n),
        "Year": np.random.choice([2020, 2021, 2022, 2023, 2024], size=n),
        "Gender": np.random.choice(["Male", "Female"], size=n),
        "Department": np.random.choice(["IT", "HR", "Sales", "Finance"], size=n),
    }
)

# 1a. HISTOGRAM: Displays value frequency across continuous intervals (bins)
sns.histplot(
    data=df,
    x="Age",  # Feature on x-axis
    bins=15,  # Number of discrete intervals/bars
    kde=True,  # Superimpose Kernel Density Estimate (smooth curve)
    color="skyblue",  # Fill color of bars
)
plt.title("Age Distribution (histplot)")
plt.show()

# 1b. KDE PLOT: Estimates the probability density function (smooth continuous curve)
sns.kdeplot(
    data=df,
    x="Salary",  # Feature on x-axis
    hue="Gender",  # Color-code by category to compare distributions
    fill=True,  # Fill area under the curve
    common_norm=False,  # Normalize each hue group independently
    palette="muted",
)
plt.title("Salary Density by Gender (kdeplot)")
plt.show()

# 1c. DISPLOT: Figure-level interface combining histograms, KDEs, and subplots
sns.displot(
    data=df,
    x="Salary",
    col="Gender",  # Split into side-by-side columns by category
    kde=True,  # Include KDE curve
    kind="hist",  # Can be 'hist', 'kde', or 'ecdf'
    height=4,  # Height of each subplot in inches
)
plt.show()










sns.scatterplot(
    data=df,
    x="Age",  # X-axis variable
    y="Salary",  # Y-axis variable
    hue="Gender",  # Color code by categorical column
    style="Department",  # Distinguish categories using marker shapes
    size="Sales",  # Scale marker size based on a continuous variable
    sizes=(20, 200),  # Min and max size range for markers
    alpha=0.8,  # Transparency (0=transparent, 1=opaque)
)
plt.title("Age vs. Salary by Gender and Department")
plt.show()








sns.lineplot(
    data=df,
    x="Year",  # Sequential/time variable
    y="Sales",  # Continuous target variable
    hue="Department",  # Separate trendlines for each category
    style="Department",  # Unique line styles (solid, dashed, etc.)
    markers=True,  # Place point markers at data coordinates
    dashes=False,  # Solid lines for all series if set to False
    errorbar="ci",  # Show confidence interval as shaded region around lines
)
plt.title("Sales Trends over Time by Department")
plt.show()









sns.barplot(
    data=df,
    x="Gender",  # Categorical grouping column
    y="Salary",  # Numerical value to aggregate
    hue="Department",  # Secondary categorical grouping
    estimator=np.mean,  # Aggregation function (default is mean)
    errorbar="sd",  # Error bars show standard deviation instead of CI
    palette="Set2",  # Color palette scheme
    capsize=0.1,  # Width of caps on error bars
)
plt.title("Mean Salary by Gender and Department")
plt.show()










sns.countplot(
    data=df,
    x="Department",  # Categorical variable to count
    hue="Gender",  # Group counts by secondary category
    palette="pastel",  # Color scheme
    order=[
        "Sales",
        "IT",
        "Finance",
        "HR",
    ],  # Explicit ordering of category bars
)
plt.title("Employee Count by Department and Gender")
plt.show()









sns.boxplot(
    data=df,
    x="Department",  # Group by categorical column
    y="Age",  # Continuous variable
    hue="Gender",  # Sub-group categories side-by-side
    palette="Blues",  # Color theme
    width=0.6,  # Bar width (0 to 1)
    fliersize=5,  # Size of outlier markers beyond 1.5 * IQR
)
plt.title("Age Distribution & Outliers by Department")
plt.show()










sns.violinplot(
    data=df,
    x="Gender",  # Categorical axis
    y="Salary",  # Numerical axis
    hue="Department",  # Secondary grouping
    split=False,  # If hue has 2 levels, True merges left/right sides
    inner="quartile",  # Show internal dashed lines for 25%, 50%, 75%
    palette="magma",  # Color scheme
    bw_method=0.2,  # Bandwidth factor determining KDE smoothing
)
plt.title("Salary Spread & Density by Gender")
plt.show()










sns.pairplot(
    df[["Age", "Salary", "Sales", "Gender"]],
    hue="Gender",  # Group data points and KDE distributions by category
    corner=True,  # Render lower triangle only (removes duplicate mirror plots)
    diag_kind="kde",  # Diagonal visualization: 'kde' or 'hist'
    kind="scatter",  # Off-diagonal plots: 'scatter' or 'reg'
    palette="Set1",
)
plt.suptitle("Pairwise Relationships across Metrics", y=1.02)
plt.show()













sns.jointplot(
    data=df,
    x="Age",
    y="Salary",
    hue="Gender",
    kind="scatter",
    height=6,
    marginal_kws=dict(fill=True)
)
plt.show()









sns.regplot(
    data=df,
    x="Age",  # Independent variable
    y="Salary",  # Dependent variable
    scatter_kws={
        "alpha": 0.5,
        "color": "teal",
    },  # Custom properties for points
    line_kws={"color": "darkred", "linewidth": 2},  # Custom properties for line
    ci=95,  # Confidence interval level percentage for regression estimate
    order=1,  # Polynomial order (1 = linear, 2 = quadratic)
)
plt.title("Linear Regression: Age vs. Salary")
plt.show()









sns.lmplot(
    data=df,
    x="Age",
    y="Salary",
    hue="Gender",  # Separate regression lines per category on one plot
    col="Department",  # Create separate subplots in columns by department
    col_wrap=2,  # Wrap to next row after 2 columns
    height=3.5,  # Subplot height in inches
    scatter_kws={"alpha": 0.6},
)
plt.show()











# Step 1: Initialize the grid layout based on categorical split
g = sns.FacetGrid(
    data=df,
    col="Department",  # Column facets
    row="Gender",  # Row facets
    margin_titles=True,  # Display titles on grid margins
    height=3,  # Height of each panel
)

# Step 2: Map a plotting function onto every panel in the grid
g.map(
    sns.histplot,  # Plotting function to execute across grid
    "Age",  # Variable to plot
    kde=True,  # Arguments passed to histplot
    color="darkgreen",
)

# Step 3: Add titles and adjust layout boundaries
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Age Distribution Grid across Departments and Genders")
plt.show()
sns.heatmap(
    df.corr(numeric_only=True)
)
plt.show();