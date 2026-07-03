import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("output/amazon_sales_cleaned.csv")
print("=" * 70)
print("AMAZON SALES ANALYSIS")
print("=" * 70)

total_orders = df["Order ID"].nunique()

print(f"Total Orders : {total_orders}")

# -----------------------------------------------------
# Total Revenue
# -----------------------------------------------------

total_revenue = df["Amount"].sum()

print(f"Total Revenue : ₹{total_revenue:,.2f}")

# -----------------------------------------------------
# Total Quantity Sold
# -----------------------------------------------------

total_quantity = df["Qty"].sum()

print(f"Total Quantity Sold : {total_quantity}")

# -----------------------------------------------------
# Average Order Value
# -----------------------------------------------------

average_order_value = total_revenue / total_orders

print(f"Average Order Value : ₹{average_order_value:,.2f}")

# -----------------------------------------------------
# CATEGORY ANALYSIS
# -----------------------------------------------------

print("\n" + "=" * 70)
print("CATEGORY ANALYSIS")
print("=" * 70)

category_analysis = (
    df.groupby("Category")
      .agg({
          "Amount": "sum",
          "Qty": "sum",
          "Order ID": "nunique"
      })
      .rename(columns={
          "Amount": "Revenue",
          "Qty": "Quantity Sold",
          "Order ID": "Total Orders"
      })
      .sort_values(by="Revenue", ascending=False)
)

print(category_analysis)

# ---------------------------------------------------
# CATEGORY REVENUE BAR CHART
# ---------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    category_analysis.index,
    category_analysis["Revenue"]
)

plt.title("Revenue by Product Category")

plt.xlabel("Category")

plt.ylabel("Revenue (INR)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/category_revenue.png", dpi=300)
plt.show()

print("=" * 70)
print("STATE ANALYSIS")
print("=" * 70)

state_analysis = (
    df.groupby("ship-state")
      .agg(
          Revenue=("Amount", "sum"),
          Quantity_Sold=("Qty", "sum"),
          Total_Orders=("Order ID", "nunique")
      )
      .sort_values(by="Revenue", ascending=False)
)

print(state_analysis.head(10))

# ============================================================
# STATE REVENUE GRAPH
# ============================================================

plt.figure(figsize=(12,6))

plt.bar(
    state_analysis.head(10).index,
    state_analysis.head(10)["Revenue"]
)

plt.title("Top 10 States by Revenue")

plt.xlabel("State")

plt.ylabel("Revenue (INR)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/state_revenue.png", dpi=300)
plt.show()

# -----------------------------------------------------
# MONTHLY ANALYSIS
# -----------------------------------------------------

print("=" * 70)
print("MONTHLY ANALYSIS")
print("=" * 70)

monthly_analysis = (
    df.groupby(["Year", "Month"])
      .agg(
          Revenue=("Amount", "sum"),
          Quantity_Sold=("Qty", "sum"),
          Total_Orders=("Order ID", "nunique")
      )
      .sort_values(by=["Year", "Month"])
)

print(monthly_analysis)

# ============================================================
# MONTHLY REVENUE LINE CHART
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_analysis.index.get_level_values("Month"),
    monthly_analysis["Revenue"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")

plt.grid(True)

plt.tight_layout()
plt.savefig("images/monthly_revenue.png", dpi=300)
plt.show()


print("\n" + "=" * 70)
print("TOP SELLING PRODUCTS")
print("=" * 70)

top_products = (
    df.groupby("Style")
      .agg(
          Revenue=("Amount", "sum"),
          Quantity_Sold=("Qty", "sum"),
          Total_Orders=("Order ID", "nunique")
      )
      .sort_values(by="Revenue", ascending=False)
      .head(10)
)

print(top_products)

print("\n" + "=" * 70)
print("CITY ANALYSIS")
print("=" * 70)

city_analysis = (
    df.groupby("ship-city")
      .agg(
          Revenue=("Amount", "sum"),
          Quantity_Sold=("Qty", "sum"),
          Total_Orders=("Order ID", "nunique")
      )
      .sort_values(by="Revenue", ascending=False)
      .head(10)
)

print(city_analysis)


