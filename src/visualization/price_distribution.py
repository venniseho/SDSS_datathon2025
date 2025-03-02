"""
Real Estate Data Visualization - Price Distribution

This script loads a cleaned real estate dataset and generates a histogram
showing the distribution of listing prices.

Features:
- Loads the cleaned dataset from the `data/` directory.
- Uses Seaborn to plot a histogram with a KDE (Kernel Density Estimate).
- Displays the frequency of listing prices to analyze price distribution.

Author: Oceane Yembiline
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
file_path = os.path.join(project_root, "data", "cleaned_real_estate_data_numerical.csv")

# Load the cleaned dataset
df = pd.read_csv(file_path)

# Price Distribution Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df["listing_price"], bins=50, kde=True, color='skyblue')
plt.xlabel("Listing Price")
plt.ylabel("Frequency")
plt.title("Distribution of Listing Prices")
plt.savefig(os.path.join(base_dir, 'visualization_images', 'price_distribution'), dpi=300)
print("Figure created successfully! You can open 'price_distribution' to view it.")
