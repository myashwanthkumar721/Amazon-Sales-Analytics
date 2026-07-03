# ======================================================
# Amazon Sales Analytics Project
# File: cleaning.py
# ======================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display all columns
pd.set_option('display.max_columns', None)

print("=" * 70)
print(" AMAZON SALES ANALYTICS PROJECT ")
print("=" * 70)

# ------------------------------
# Load Dataset
# ------------------------------

file_path = r"C:\Users\Jayak\Downloads\Amazon Sale Report.csv"

df = pd.read_csv(file_path, low_memory=False)

print("\n Dataset Loaded Successfully!")

# ------------------------------
# Dataset Shape
# ------------------------------

print("\nDataset Shape:")
print(df.shape)

# ------------------------------
# First 5 Rows
# ------------------------------

print("\nFirst 5 Rows:")
print(df.head())

# ------------------------------
# Last 5 Rows
# ------------------------------

print("\nLast 5 Rows:")
print(df.tail())

# ------------------------------
# Dataset Information
# ------------------------------

print("\nDataset Information")
print(df.info())

# ------------------------------
# Column Names
# ------------------------------

print("\nColumn Names")

for col in df.columns:
    print(col)

# ------------------------------
# Data Types
# ------------------------------

print("\nData Types")
print(df.dtypes)

# ------------------------------
# Summary Statistics
# ------------------------------

print("\nSummary Statistics")
print(df.describe(include='all'))

# ------------------------------
# Missing Values
# ------------------------------

print("\nMissing Values")

missing = df.isnull().sum()

print(missing)

# ------------------------------
# Duplicate Rows
# ------------------------------

print("\nDuplicate Rows")

print(df.duplicated().sum())

# -----------------------------------------------------
# Remove Unnecessary Column
# -----------------------------------------------------

print("\n" + "=" * 70)
print("REMOVE UNNECESSARY COLUMN")
print("=" * 70)

# Remove the extra column
df = df.drop(columns=["Unnamed: 22"])

print("Column 'Unnamed: 22' removed successfully!")

print("\nNew Dataset Shape:")
print(df.shape)

print("\nUpdated Columns:")
print(df.columns.tolist())

# -----------------------------------------------------
# Handle Missing Values
# -----------------------------------------------------

print("\n" + "=" * 70)
print("HANDLING MISSING VALUES")
print("=" * 70)

# Remove rows with missing shipping information
df = df.dropna(subset=[
    "ship-city",
    "ship-state",
    "ship-postal-code",
    "ship-country"
])

# Fill missing promotion IDs
df["promotion-ids"] = df["promotion-ids"].fillna("No Promotion")

# Fill missing fulfilled-by values
df["fulfilled-by"] = df["fulfilled-by"].fillna("Unknown")

print("Missing values handled successfully!")

print("\nRemaining Missing Values:")
print(df.isnull().sum())

# -----------------------------------------------------
# Fix Data Types
# -----------------------------------------------------

print("\n" + "=" * 70)
print("FIXING DATA TYPES")
print("=" * 70)

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%m-%d-%y")

print(" Date column converted successfully!")

print("\nUpdated Data Types:")
print(df.dtypes)

# -----------------------------------------------------
# Feature Engineering
# -----------------------------------------------------

print("\n" + "=" * 70)
print("FEATURE ENGINEERING")
print("=" * 70)

# Create Month column
df["Month"] = df["Date"].dt.month_name()

# Create Month Number column
df["Month Number"] = df["Date"].dt.month

# Create Year column
df["Year"] = df["Date"].dt.year

# Create Day column
df["Day"] = df["Date"].dt.day
df["Day Number"] = df["Date"].dt.dayofweek + 1
# Create Day Name column
df["Day Name"] = df["Date"].dt.day_name()

print(" New columns created successfully!")

print("\nNew Columns:")
print(df[["Date", "Month","Month Number", "Year", "Day", "Day Name"]].head())
print(df.columns.tolist())

# -----------------------------------------------------
# Check Duplicate Rows
# -----------------------------------------------------

print("\n" + "=" * 70)
print("CHECKING DUPLICATES")
print("=" * 70)

# Count duplicate rows
duplicates = df.duplicated().sum()

print(f"Total Duplicate Rows: {duplicates}")

# Remove duplicates if found
if duplicates > 0:
    df = df.drop_duplicates()
    print(" Duplicate rows removed successfully!")
else:
    print(" No duplicate rows found.")

# Save Cleaned Dataset
df.to_csv("output/amazon_sales_cleaned.csv", index=False)

print("\n Cleaned dataset saved successfully!")

