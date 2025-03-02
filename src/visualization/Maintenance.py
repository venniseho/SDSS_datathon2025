"""
Visualization of Price Variations by Monthly Maintenance Fees

This script categorizes the monthly maintenance fees (in increments of 500 CAD), and visualizes the price variations
using box plots. It was found that price variation remained relatively similar for monthly maintenance fees above 1000.

Author: Duncan Wan
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
file_path = "/Users/duncan/PycharmProjects/SDSS_datathon2025/data/cleaned_real_estate_data_numerical.csv"
df = pd.read_csv(file_path)

# Define maintenance fee bins
bins = [0, 500, 1000, 1500, 2000, 2500, 3000, df['monthly_maintenance_fee'].max()]
labels = ['0-500', '501-1000', '1001-1500', '1501-2000', '2001-2500', '2501-3000', '3000+']

# Create a new column with categorized maintenance fees
df['maintenance_fee_group'] = pd.cut(df['monthly_maintenance_fee'], bins=bins, labels=labels, include_lowest=True)

plt.figure(figsize=(12, 6))

# Create a boxplot with grouped maintenance fees
sns.boxplot(x=df['maintenance_fee_group'], y=df['listing_price'])

# Labels and title
plt.xlabel("Monthly Maintenance Fee Group")
plt.ylabel("Listing Price")
plt.title("Price Variations by Monthly Maintenance Fee Group")

# Show plot
plt.show()
