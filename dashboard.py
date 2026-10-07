import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ecommerce_sales.csv")

# Calculations
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

category_sales = df.groupby("Category")["Sales"].sum()
category_profit = df.groupby("Category")["Profit"].sum()

best_product = df.loc[df["Sales"].idxmax(), "Product"]
best_category = category_sales.idxmax()

# =========================
# DASHBOARD
# =========================

fig = plt.figure(figsize=(14, 9))
fig.suptitle("E-Commerce Sales Analytics Dashboard",
             fontsize=20, fontweight="bold")

# Total Sales
plt.figtext(
    0.20, 0.88,
    f"Total Sales\n₹{total_sales:,}",
    ha="center",
    fontsize=16,
    fontweight="bold"
)

# Total Profit
plt.figtext(
    0.50, 0.88,
    f"Total Profit\n₹{total_profit:,}",
    ha="center",
    fontsize=16,
    fontweight="bold"
)

# Best Product
plt.figtext(
    0.80, 0.88,
    f"Best Product\n{best_product}",
    ha="center",
    fontsize=16,
    fontweight="bold"
)

# Sales by Category
ax1 = fig.add_axes([0.08, 0.48, 0.38, 0.30])
category_sales.plot(kind="bar", ax=ax1)
ax1.set_title("Sales by Category")
ax1.set_xlabel("Category")
ax1.set_ylabel("Sales")

# Profit by Category
ax2 = fig.add_axes([0.55, 0.48, 0.38, 0.30])
category_profit.plot(kind="bar", ax=ax2)
ax2.set_title("Profit by Category")
ax2.set_xlabel("Category")
ax2.set_ylabel("Profit")

# Product Sales
product_sales = df.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
)

ax3 = fig.add_axes([0.08, 0.08, 0.85, 0.28])
product_sales.plot(kind="bar", ax=ax3)
ax3.set_title("Sales by Product")
ax3.set_xlabel("Product")
ax3.set_ylabel("Sales")

# Save dashboard
plt.savefig("charts/ecommerce_dashboard.png", dpi=300, bbox_inches="tight")

plt.show()

print("\n===== DASHBOARD CREATED SUCCESSFULLY =====")
print("Best Category:", best_category)
print("Best Product:", best_product)