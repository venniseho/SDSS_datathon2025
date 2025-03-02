"""
Visualization of Price Variations by Wards

This script categorises data into 3 groups based on wards (10, 11, 13) and visualizes the price variation by each
ward. It showed that price variation was not significant, and was consistent across wards. Additionally, the median
and upper and lower quartiles are relatively similar, suggesting property prices do not change much across wards,
giving us reason to not include neighborhood/ward in our machine learning model.

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

# Create a boxplot for price variations across wards
sns.boxplot(x=df['ward_num'], y=df['listing_price'])

# Labels and title
plt.xlabel("Ward Number")
plt.ylabel("Listing Price")
plt.title("Price Variations Across Wards")

# Show plot
plt.show()