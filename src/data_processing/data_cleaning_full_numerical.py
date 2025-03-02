"""
Toronto Real Estate Data Preprocessing (Fully Numerical)

This script prepares raw real estate data for machine learning by:
- Converting all categorical variables into numerical values
- Handling missing & dirty data to ensure data integrity

Column Headers:
"id", "ward_num", "num_beds", "num_baths", "has_den", "size_group", "has_parking",
"property_orientation", "days_on_market", "building_age", "monthly_maintenance_fee",
"listing_price", "latitude", "longitude"

Author: Vennise Ho
Generated with assistance from ChatGPT, an AI language model by OpenAI.
Date: 2025-03-01
"""
import os
import pandas as pd

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
file_path = os.path.join(project_root, "data", "real-estate-data.csv")

# Load the dataset
df = pd.read_csv(file_path)

# Define new column headers
df.columns = [
    "id", "ward_num", "num_beds", "num_baths", "has_den", "size_group", "has_parking",
    "property_orientation", "days_on_market", "building_age", "monthly_maintenance_fee",
    "listing_price", "latitude", "longitude"
]


# Convert 'size' column from range format to a size_group
def convert_size_to_group(size: str) -> int:
    """
    Converts property size range to a numerical size group.
    """
    if not isinstance(size, str):
        raise TypeError("Only strings are allowed")
    if "+" in size:
        return 8  # 4000+ sqft
    lower_bound = int(size.split('-')[0])
    return lower_bound // 500


# Clean property orientation values
def clean_property_orientation(value: str) -> int:
    """
    Converts property orientation into numerical values.
    Mapping: {'N': 0, 'S': 1, 'E': 2, 'W': 3}
    """
    if not isinstance(value, str):
        raise TypeError("Only strings are allowed")
    mapping = {"N": 0, "S": 1, "E": 2, "W": 3}
    return mapping.get(value.upper(), None)


# Data Cleaning
df = df.replace("NA", pd.NA).dropna()
df['ward_num'] = df['ward_num'].str.extract('(\\d+)').astype(int)
df["size_group"] = df["size_group"].apply(convert_size_to_group)
df["property_orientation"] = df["property_orientation"].apply(clean_property_orientation)

# Convert boolean features to integer (0/1)
df["has_den"] = df["has_den"].str.strip().str.lower().map({"yes": 1, "no": 0})
df["has_parking"] = df["has_parking"].str.strip().str.lower().map({"yes": 1, "n": 0})

# Save the cleaned numerical dataset
df.to_csv("../../data/cleaned_real_estate_data_numerical.csv", index=False)

# Display cleaned data info
df.info()
