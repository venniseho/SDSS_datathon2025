"""
Correlation Matrix Heatmap for Real Estate Data

This script take the real estate data, computes the correlation matrix, and visualizes it using a heatmap. The heatmap
helps understand how variables correlate with each other, in particular, how explanatory variables correlate with
price. This helped us identify the variables that correlate significantly to the housing price, which helped us justify
which variable to include in our machine learning model. Specifically, we identified that number of bedrooms, number
of bathrooms, property size, and monthly maintenance fees had high correlation values.

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

# Compute the correlation matrix
correlation_matrix = df.drop(columns=['id']).corr()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)

# Title and labels
plt.title("Correlation Matrix Heatmap")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Display the heatmap
plt.show()