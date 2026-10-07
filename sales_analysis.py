import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("ecommerce_sales.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# Plot Sales by Category
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
# plt.show()

# =========================
# CHARTS
# =========================

# Sales by Category
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
# plt.show()

# Profit by Category
category_profit = df.groupby("Category")["Profit"].sum()

category_profit.plot(kind="bar", title="Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("charts/profit_by_category.png")
# plt.show()

# Sales by Product
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

product_sales.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/sales_by_product.png")
# plt.show()
print("\n===== IMPORTANT INSIGHTS =====")

print("Total Products:", df["Product"].nunique())

best_product = df.loc[df["Sales"].idxmax(), "Product"]
print("Best Selling Product:", best_product)

profit_product = df.loc[df["Profit"].idxmax(), "Product"]
print("Highest Profit Product:", profit_product)

best_category = category_sales.idxmax()
print("Best Sales Category:", best_category)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())