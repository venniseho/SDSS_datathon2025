import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "cleaned_real_estate_data.csv"  # Change if needed
df = pd.read_csv(file_path)

# Set a price cap to reduce the impact of extreme outliers
price_cap = df["listing_price"].quantile(0.95)  # Keep only the bottom 95% of prices
df_filtered = df[df["listing_price"] <= price_cap].copy()  # Create a full copy

# Convert prices to thousands (K)
df_filtered.loc[:, "listing_price"] = df_filtered["listing_price"] / 1000

# 1️⃣ Price Distribution Histogram
plt.figure(figsize=(10,6))
sns.histplot(df_filtered["listing_price"], bins=50, kde=True, color='skyblue')
plt.xlabel("Listing Price (in Thousands)")
plt.ylabel("Frequency")
plt.title("Distribution of Listing Prices")
plt.show()
