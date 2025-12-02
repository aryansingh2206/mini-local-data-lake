import pandas as pd
import os
import numpy as np

df = pd.read_csv("processed/sales_cleaned.csv")

# -----------------------------
# ADD DATE PARTITION (no date in dataset)
# -----------------------------

# Generate synthetic dates between 2022–2023
df["date"] = pd.to_datetime(
    np.random.choice(pd.date_range("2022-01-01", "2023-12-31"), len(df))
)

# Partition by year
for year, group in df.groupby(df["date"].dt.year):
    year_dir = f"curated/year={year}"
    os.makedirs(year_dir, exist_ok=True)
    group.to_parquet(f"{year_dir}/sales.parquet", index=False)

print("Curated data created with year partitions")
