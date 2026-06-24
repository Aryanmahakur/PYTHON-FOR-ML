import pandas as pd  # Import pandas library

# Create a Series with default index (0,1,2,3)
s = pd.Series([10, 20, 30, 40])

# Print the Series
print(s)

# Create a Series with custom indexes
s = pd.Series(
    [10,20,30],          # Values
    index=["A","B","C"]  # Custom labels
)

# Print the Series
print(s)

# Create a DataFrame
df = pd.DataFrame({
    "Name":["Alice","Bob"],  # Name column
    "Age":[25,30]           # Age column
})

# Print DataFrame
print(df)

# Read CSV file into DataFrame
df = pd.read_csv("data.csv")

# Read Excel file into DataFrame
df = pd.read_excel("data.xlsx")

# Read JSON file into DataFrame
df = pd.read_json("data.json")

# Import pandas again (not needed if already imported)
import pandas as pd

# Dictionary containing data
data = {
    "Name": ["Aryan", "Rahul", "Priya"],
    "Age": [18, 20, 19]
}

# Create DataFrame from dictionary
df = pd.DataFrame(data)

# Save DataFrame as CSV file
# index=False prevents saving row indexes
df.to_csv("students.csv", index=False)

# Print message
print("CSV file created!")

# Show first 5 rows
print(df.head())

# Show last 5 rows
print(df.tail())

# Show shape (rows, columns)
print(df.shape)

# Show only number of rows
print(df.shape[0])

# Show column names
print(df.columns)

# Convert column names to list
print(list(df.columns))

# Show datatype of each column
print(df.dtypes)

# Show complete DataFrame information
print(df.info())

# Show statistics for numeric columns
print(df.describe())

# Select Age column
print(df["Age"])

# Select first value of Age column
print(df["Age"][0])

# Select multiple columns
# ERROR here because Salary column doesn't exist
print(df[["Name","Salary"]])

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Aryan", "Rahul", "Priya"],
    "Age": [18, 20, 19],
    "City": ["Delhi", "Mumbai", "Pune"]
})

# Print heading
print("Original DataFrame:")

# Print DataFrame
print(df)

# ---------------- LOC ----------------

# 1. Single row using label/index
print("\n1. Single Row:")
print(df.loc[0])

# 2. Multiple rows
print("\n2. Multiple Rows:")
print(df.loc[[0, 2]])

# 3. Row range
# loc includes ending index
print("\n3. Row Range:")
print(df.loc[0:1])

# 4. Specific row and column
print("\n4. Specific Row and Column:")
print(df.loc[1, "Name"])

# 5. Select specific columns
print("\n5. Multiple Columns:")
print(df.loc[:, ["Name", "Age"]])

# 6. Conditional filtering
print("\n6. Age > 18:")
print(df.loc[df["Age"] > 18])

# 7. Conditional filtering + selected columns
print("\n7. Age > 18 (Name and Age only):")
print(df.loc[df["Age"] > 18, ["Name", "Age"]])

# 8. Update value
# Change Age at row 0 to 21
df.loc[0, "Age"] = 21

print("\n8. After Updating Age:")
print(df)

import pandas as pd

# Create DataFrame again
df = pd.DataFrame({
    "Name": ["Aryan", "Rahul", "Priya"],
    "Age": [18, 20, 19],
    "City": ["Delhi", "Mumbai", "Pune"]
})

# Print DataFrame
print("Original DataFrame:")
print(df)

# ---------------- ILOC ----------------

# 1. Single row using position
# Print heading
print("\n1. Single Row:")

# Print heading again (duplicate line)
print("\n1. Single Row:")

# Select first row by position
# iloc uses integer positions
print(df.iloc[0])

# 2. Multiple rows

# Print heading
print("\n2. Multiple Rows:")

# Select row positions 0 and 2
print(df.iloc[[0, 2]])

# 3. Row range

# Print heading
print("\n3. Row Range:")

# Select rows from position 0 up to (but not including) 2
# Returns rows 0 and 1
print(df.iloc[0:2])

# 4. Specific row and column

# Print heading
print("\n4. Specific Row and Column:")

# Row position 1, column position 0
# Returns "Rahul"
print(df.iloc[1, 0])

# 5. Multiple columns

# Print heading
print("\n5. Multiple Columns:")

# All rows, columns at positions 0 and 1
# Name and Age columns
print(df.iloc[:, [0, 1]])

# 6. Rows and columns range

# Print heading
print("\n6. Rows and Columns Range:")

# Rows 0-1 and columns 0-1
print(df.iloc[0:2, 0:2])

# 7. Select specific rows and columns

# Print heading
print("\n7. Specific Rows and Columns:")

# Rows 0 and 2
# Columns 0 and 2
# Name and City
print(df.iloc[[0, 2], [0, 2]])

# 8. Update a value

# Row 0, Column 1 (Age)
# Change Age from 18 to 21
df.iloc[0, 1] = 21

# Print heading
print("\n8. After Updating Age:")

# Print updated DataFrame
print(df)

# Filter rows where Age > 30
print(df[df["Age"] > 30])

# Count missing values in each column
print(df.isnull().sum())

# Check non-missing values
# True = value exists
# False = missing value
print(df.notnull())

# Replace all NaN values with 0
print(df.fillna(0))

# Remove rows containing NaN
print(df.dropna())

# Remove columns containing NaN
print(df.dropna(axis=1))

# Replace NY with New York in City column
df["City"] = df["City"].replace(
    {"NY":"New York"}
)

# Print DataFrame
print(df)

# Create new DataFrame
df = pd.DataFrame({
    "Result":[1,0,1,0]
})

# Replace values
# 1 -> Pass
# 0 -> Fail
df["Result"] = df["Result"].replace({
    1:"Pass",
    0:"Fail"
})

# Rename column Age to Student_Age
# NOTE:
# Current DataFrame only has Result column
# So this will not change anything
df = df.rename(
    columns={
        "Age":"Student_Age"
    }
)

# Drop City column
# NOTE:
# City does not exist in current DataFrame
# This will cause KeyError
df = df.drop(columns=["City"])

# Drop row with index 1
df = df.drop(index=1)

# Check duplicate rows
# True = duplicate
# False = unique
print(df.duplicated())

# Remove duplicate rows
df = df.drop_duplicates()

# Sort by Age column
# NOTE:
# Age column does not exist here
df.sort_values("Age")

# Sort Age ascending
df.sort_values("Age", ascending=True)

# Sort by Age first then Salary
# NOTE:
# Age and Salary columns do not exist
df.sort_values(
    ["Age","Salary"]
)

# Sort by index descending
df.sort_index(
    ascending=False
)

# Sort Salary descending
# Show top 5 rows
# NOTE:
# Salary column does not exist
df.sort_values(
    "Salary",
    ascending=False
).head(5)

# Import libraries
import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame({
    "Marks": [10, 20, 20, 30, 40, 50, np.nan]
})

# Print heading
print("Data:")

# Print DataFrame
print(df)

# Mean (Average)
print("\nMean:")
print(df["Marks"].mean())

# Median (Middle Value)
print("\nMedian:")
print(df["Marks"].median())

# Mode (Most Frequent Value)
print("\nMode:")
print(df["Marks"].mode())

# Minimum Value
print("\nMin:")
print(df["Marks"].min())

# Maximum Value
print("\nMax:")
print(df["Marks"].max())

# Sum of Values
print("\nSum:")
print(df["Marks"].sum())

# Count non-null values
print("\nCount:")
print(df["Marks"].count())

# Standard Deviation
print("\nStandard Deviation:")
print(df["Marks"].std())

# Variance
print("\nVariance:")
print(df["Marks"].var())

# 25th percentile
print("\n25% Quantile:")
print(df["Marks"].quantile(0.25))

# 50th percentile (same as median)
print("\n50% Quantile (Median):")
print(df["Marks"].quantile(0.50))

# 75th percentile
print("\n75% Quantile:")
print(df["Marks"].quantile(0.75))

# Complete statistical summary
print("\nDescribe:")
print(df["Marks"].describe())

# Create groups by Department
# NOTE:
# Department column does not exist in this DataFrame
df.groupby("Department")

# Sum Salary department-wise
# NOTE:
# Department and Salary columns do not exist
print(
    df.groupby("Department")["Salary"].sum()
)

# Count Salary values department-wise
print(
    df.groupby("Department")["Salary"].count()
)
# Find maximum Salary in each Department
print(
    df.groupby("Department")["Salary"].max()
)

# Example Output:
# HR    45000
# IT    70000

# Find minimum Salary in each Department
print(
    df.groupby("Department")["Salary"].min()
)

# Example Output:
# HR    40000
# IT    50000

# Group by Department and Gender
# Then find average Salary for each group
print(
    df.groupby(
        ["Department","Gender"]
    )["Salary"].mean()
)

# Example:
# Department Gender
# HR         F         45000
# HR         M         40000
# IT         F         60000
# IT         M         50000

# Count occurrences of each Department
print(
    df["Department"].value_counts()
)

# Example Output:
# IT    3
# HR    2

# Concatenate df1 and df2 vertically
# Default axis=0
df3 = pd.concat([df1, df2])

# Print combined DataFrame
print(df3)

# Example:
# df1
# A
# B
#
# df2
# C
# D
#
# Result
# A
# B
# C
# D

# Concatenate horizontally (side by side)
pd.concat(
    [df1,df2],
    axis=1
)

# axis=1 means columns are joined

# Merge df1 and df2 using common column ID
df = pd.merge(
    df1,
    df2,
    on="ID"
)

# Print merged DataFrame
print(df)

# Example:
# df1
# ID Name
# 1  Aryan
# 2  Rahul
#
# df2
# ID Salary
# 1  50000
# 2  60000
#
# Result
# ID Name  Salary
# 1 Aryan 50000
# 2 Rahul 60000

# INNER JOIN
# Keep only matching IDs from both DataFrames
pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)

# Example:
# df1 IDs: 1 2 3
# df2 IDs: 2 3 4
#
# Result:
# 2 3

# LEFT JOIN
# Keep all rows from left DataFrame (df1)
pd.merge(
    df1,
    df2,
    on="ID",
    how="left"
)

# Example:
# Result IDs:
# 1 2 3

# RIGHT JOIN
# Keep all rows from right DataFrame (df2)
pd.merge(
    df1,
    df2,
    on="ID",
    how="right"
)

# Example:
# Result IDs:
# 2 3 4

# OUTER JOIN
# Keep all rows from both DataFrames
pd.merge(
    df1,
    df2,
    on="ID",
    how="outer"
)

# Example:
# Result IDs:
# 1 2 3 4

# One-Hot Encoding
# Convert categorical Gender values into numeric columns
pd.get_dummies(df["Gender"])

# Example:
# Gender
# Male
# Female
# Male
#
# Output:
#
# Female Male
#   0      1
#   1      0
#   0      1

# ML models cannot understand text like:
# Male, Female
#
# So get_dummies() converts them into numbers.