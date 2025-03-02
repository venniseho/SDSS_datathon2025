import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "../../data/cleaned_real_estate_data.csv"  # Change if needed
df = pd.read_csv(file_path)

# 1️⃣ Price Distribution Histogram
plt.figure(figsize=(10,6))
sns.histplot(df["listing_price"], bins=50, kde=True, color='skyblue')
plt.xlabel("Listing Price")
plt.ylabel("Frequency")
plt.title("Distribution of Listing Prices")
plt.show()
