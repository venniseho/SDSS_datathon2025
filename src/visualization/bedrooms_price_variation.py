"""
Visualization of Price Variations by Number of Bedrooms

This script categorises data into 3 groups (different number of bedrooms) and visualizes the price variation by each
group. It showed that price variation increases as your number of bedroom increases.

Author: Duncan Wan
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
file_path = os.path.join(project_root, "data", "cleaned_real_estate_data_numerical.csv")

# Load the dataset from the correct location
df = pd.read_csv(file_path)

# Ensure 'num_beds' and 'listing_price' exist before analysis
if 'num_beds' in df.columns and 'listing_price' in df.columns:
    plt.figure(figsize=(12, 6))

    # Create a boxplot to show price variation (whiskers and box plot) by number of bedrooms
    sns.boxplot(x=df['num_beds'], y=df['listing_price'], showfliers=True)  # Includes outliers (whiskers)

    # Labels and title
    plt.xlabel("Number of Bedrooms")
    plt.ylabel("Listing Price")
    plt.title("Price Variations by Number of Bedrooms (Boxplot with Whiskers)")

    # Save plot
    plt.savefig(os.path.join(base_dir, 'visualization_images', 'bedrooms_price_variation'), dpi=300)
    print("Figure created successfully! You can open 'bedrooms_price_variation' to view it.")

else:
    print("Error: 'num_beds' or 'listing_price' column not found in the dataset.")
