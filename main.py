
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# 1. Sales by Category
print("----- Sales by Category -----")
sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)

# 2. Profit by Region
print("\n----- Profit by Region -----")
profit_by_region = df.groupby("Region")["Profit"].sum()
print(profit_by_region)

# 3. Top Selling Sub-Categories
print("\n----- Top Selling Sub-Categories -----")
top_subcategory = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
print(top_subcategory)

# 4. Chart
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()