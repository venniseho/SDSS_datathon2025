"""
Visualization of Price Variations by Number of Bedrooms

This script categorises data into 3 groups (different number of bedrooms) and visualizes the price variation by each
group. It showed that price variation increases as your number of bedroom increases.

Author: Duncan Wan
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset from the correct location
file_path = "/Users/duncan/PycharmProjects/SDSS_datathon2025/data/cleaned_real_estate_data_numerical.csv"
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

    # Show plot
    plt.show()

else:
    print("❌ Error: 'num_beds' or 'listing_price' column not found in the dataset.")
