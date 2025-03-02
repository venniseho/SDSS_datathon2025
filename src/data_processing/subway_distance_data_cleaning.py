"""
Creation of Real Estate Data With Subway Distance

This script creates a csv file adding the distance from the subway for each real estate
listing. It uses data from the TTC.

Author: Lillian Toe
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from scipy.spatial import cKDTree
import numpy as np

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
real_estate_file_path = os.path.join(project_root, "data", "cleaned_real_estate_data_numerical.csv")

# Load the real estate dataset
real_estate_data = pd.read_csv(real_estate_file_path)

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
subway_file_path = os.path.join(project_root, "data", "DMTI2012_Subway.shp")

# Load the Toronto subway station locations
subway_stations = gpd.read_file(subway_file_path)

# Convert real estate listings to GeoDataFrame
real_estate_data['geometry'] = real_estate_data.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)
real_estate_gdf = gpd.GeoDataFrame(real_estate_data, geometry='geometry', crs=subway_stations.crs)

# Convert LineString geometries to representative Points (midpoints)
subway_stations['geometry'] = subway_stations.geometry.apply(
    lambda geom: geom.interpolate(0.5, normalized=True) if geom.geom_type == 'LineString' else geom
)

# Extract coordinates for real estate listings and subway stations
real_estate_coords = np.array(list(zip(real_estate_gdf.geometry.x, real_estate_gdf.geometry.y)))
subway_coords = np.array(list(zip(subway_stations.geometry.x, subway_stations.geometry.y)))

# Build a KDTree for efficient nearest neighbor search
subway_tree = cKDTree(subway_coords)

# Find the nearest subway station for each real estate listing
distances, _ = subway_tree.query(real_estate_coords)

# Add the computed distances to the dataset
real_estate_data['distance_to_subway'] = distances

# Save the updated dataset with subway distance information
updated_file_path = "../../data/real_estate_data_with_subway_distance.csv"
real_estate_data.to_csv(updated_file_path, index=False)

# Return the new file path
print(f"Updated dataset saved at: {updated_file_path}")
