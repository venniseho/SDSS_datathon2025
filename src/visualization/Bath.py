"""
Visualization of Price Variations by Number of Bathrooms

This script categorises data into 3 groups (1,2,3 bathrooms) and visualizes the price variation by each group. It
showed that price variation was higher for places with 2 or 3 bathrooms, but was low for places with 1 bathroom.

Author: Duncan Wan
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "/Users/duncan/PycharmProjects/SDSS_datathon2025/data/cleaned_real_estate_data_numerical.csv"
df = pd.read_csv(file_path)

plt.figure(figsize=(12, 6))

# Create a boxplot for price variations by number of bathrooms
sns.boxplot(x=df['num_baths'], y=df['listing_price'])

# Labels and title
plt.xlabel("Number of Bathrooms")
plt.ylabel("Listing Price")
plt.title("Price Variations by Number of Bathrooms")

# Show plot
plt.show()