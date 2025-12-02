import pandas as pd
import os

# Load raw dataset
df = pd.read_csv("raw/sales.csv")

# -----------------------------
# CLEANING
# -----------------------------

# Remove rows with missing essential values
df = df.dropna(subset=[
    "product_id",
    "product_name",
    "category",
    "discounted_price",
    "actual_price"
])

# Normalize category names
df["category"] = df["category"].str.strip().str.lower()

# Convert prices to numeric (remove currency symbols if present)
df["discounted_price"] = (
    df["discounted_price"]
    .astype(str)
    .str.replace("[^0-9.]", "", regex=True)
    .astype(float)
)

df["actual_price"] = (
    df["actual_price"]
    .astype(str)
    .str.replace("[^0-9.]", "", regex=True)
    .astype(float)
)

# Ensure rating numeric
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")

# Fill missing ratings safely (no chained assignment)
df["rating"] = df["rating"].fillna(0)
df["rating_count"] = df["rating_count"].fillna(0)


# Save cleaned file
os.makedirs("processed", exist_ok=True)
df.to_csv("processed/sales_cleaned.csv", index=False)

print("Processed file created → processed zone")
