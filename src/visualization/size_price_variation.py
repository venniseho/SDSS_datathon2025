"""
Visualization of Price Variations by Property Size (in Squarefeet)

This script categorises data by their property size and visualizes the price variation by each group. It
showed that price variation was relatively similar for most properties.

Author: Duncan Wan
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

# Load the dataset from the correct location
df = pd.read_csv(file_path)

# Ensure 'size_group' and 'listing_price' exist before analysis
if 'size_group' in df.columns and 'listing_price' in df.columns:
    plt.figure(figsize=(12, 6))

    # Create a boxplot of price by property size group (whiskers + outliers)
    sns.boxplot(x=df['size_group'], y=df['listing_price'])

    # Labels and title
    plt.xlabel("Size Group")
    plt.ylabel("Listing Price")
    plt.title("Price Variations by Property Size Group")

    # Save plot
    plt.savefig(os.path.join(base_dir, 'visualization_images', 'maintenance_price_variation'), dpi=300)
    print("Figure created successfully! You can open 'maintenance_price_variation' to view it.")
else:
    print("Error: 'size_group' or 'listing_price' column not found in the dataset.")
