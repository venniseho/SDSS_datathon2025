"""
Data Cleaning

New column headers: "id", "ward_num", "num_beds", "num_baths", "has_den", "size_group", "has_parking",
                    "property_orientation", "days_on_market", "building_age", "monthly_maintenance_fee",
                    "listing_price", "latitude", "longitude"

This code was generated with assistance from ChatGPT, an AI language model by OpenAI.
Date: 2025-03-01
"""

import pandas as pd

# Load the dataset
file_path = "real-estate-data.csv"  # Change path if needed
df = pd.read_csv(file_path)

# Rename column headers for ease of use
df.columns = ["id", "ward_num", "num_beds", "num_baths", "has_den", "size_group", "has_parking",
              "property_orientation", "days_on_market", "building_age", "monthly_maintenance_fee", "listing_price",
              "latitude", "longitude"]


# Convert 'size' column from range format to a size_group
def convert_size_to_group(size: str) -> int:
    """
    Converts size in size_group column from range format to a size_group.
    If the value is missing ('NA'), return NaN.
    Raises an error if the value inputted is not a string.

    Size groups:
    0. 0-499 sqft
    1. 500-999 sqft
    2. 1000-1499 sqft
    3. 1500-1999 sqft
    4. 2000-2499 sqft
    5. 2500-2999 sqft
    6. 3000-3499 sqft
    7. 3500-3999 sqft
    8. 4000+ sqft

    :param size: the size range of the property
    :return:
    """
    if not isinstance(size, str):
        raise TypeError("Only strings are allowed")

    if '+' in size:
        return 8  # indicating val of 4000+

    lower_bound = int(size.split('-')[0])
    return lower_bound // 500  # converted to size group


def clean_property_orientation(property_orientation: str) -> str:
    """
    Cleans property orientation data to 'N', 'S', 'W', 'E'

    :param property_orientation: the dirty property_orientation string
    :return: cleaned property orientation string; one of 'N', 'S', 'W', 'E'
    """

    if not isinstance(property_orientation, str):
        raise TypeError("Only strings are allowed")

    property_orientation = property_orientation.lower()

    if "n" in property_orientation:
        return "N"
    elif "s" in property_orientation:
        return "S"
    elif "w" in property_orientation:
        return "W"
    elif "e" in property_orientation:
        return "E"


# Data Cleaning Code
df = df.replace("NA", pd.NA).dropna()  # remove all rows with NA

df['ward_num'] = df['ward_num'].str.extract('(\\d+)').astype(int)

df["size_group"] = df["size_group"].apply(convert_size_to_group)
df["property_orientation"] = df["property_orientation"].apply(clean_property_orientation)

# Encode categorical columns
df["has_den"] = df["has_den"].map({"YES": True, "No": False})
df["has_parking"] = df["has_parking"].map({"Yes": True, "N": False})  # Assuming 'N' means No

# Save the cleaned dataset
df.to_csv("cleaned_real_estate_data.csv", index=False)

# Display cleaned data info
df.info()
