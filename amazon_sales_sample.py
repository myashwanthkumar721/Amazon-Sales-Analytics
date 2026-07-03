import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("output/amazon_sales_cleaned.csv")

# Create a sample of 10,000 rows
sample_df = df.head(10000)

# Save the sample dataset
sample_df.to_csv("output/amazon_sales_sample.csv", index=False)

print("Sample dataset created successfully!")
print("Rows:", len(sample_df))