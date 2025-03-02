"""
Visualization of Correlation Between Real Estate Price and Distance to Subway

This script creates a map visualizing the relationship between the real estate price
and distance to the subway. It uses data from the TTC. The visualization shows that there is
no strong correlation between the two variables, therefore distance to the subway was not included
in our model.

Author: Lillian Toe
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
import os
import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import Point, LineString

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
real_estate_file_path = os.path.join(project_root, "data", "real_estate_with_subway_distance.csv")

# Load real estate data
real_estate_df = pd.read_csv(real_estate_file_path)

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
subway_file_path = os.path.join(project_root, "data", "DMTI2012_Subway.shp")

# Load subway station data
subway_stations_gdf = gpd.read_file(subway_file_path)

# Convert real estate data into a GeoDataFrame
real_estate_gdf = gpd.GeoDataFrame(real_estate_df,
                                   geometry=gpd.points_from_xy(real_estate_df.longitude, real_estate_df.latitude))

# **Filter only Point geometries**
real_estate_gdf = real_estate_gdf[real_estate_gdf.geometry.type == "Point"]
subway_stations_gdf = subway_stations_gdf[subway_stations_gdf.geometry.type == "Point"]

# Define the Toronto map
toronto_map = folium.Map(location=[43.7, -79.4], zoom_start=12)

# **Step 1: Draw subway lines by connecting stations**
# Assuming 'LINE' column in subway data indicates which subway line a station belongs to
if 'LINE' in subway_stations_gdf.columns:
    grouped_lines = subway_stations_gdf.groupby('LINE')

    for line, stations in grouped_lines:
        # Sort stations based on approximate order (you may need a better sorting method if available)
        stations = stations.sort_values(by='geometry', key=lambda g: g.y)

        # Create a LineString from station points
        line_geom = LineString(stations.geometry.tolist())

        # Convert to GeoDataFrame
        line_gdf = gpd.GeoDataFrame(geometry=[line_geom])

        # Add to folium map
        folium.PolyLine(locations=[(point.y, point.x) for point in line_geom.coords],
                        color="red", weight=5, opacity=0.8).add_to(toronto_map)

# **Step 2: Add real estate properties to the map**
for _, row in real_estate_gdf.iterrows():
    price = row['listing_price']

    # Assign color based on price range
    if price < 500000:
        color = 'green'
    elif 500000 <= price < 1000000:
        color = 'orange'
    else:
        color = 'red'

    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=3,  # Keeping it small to prevent overlaps
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f"Listing_Price: ${price:,.0f}\nSize: {row['size_group']} sqft\nBeds: {row['num_beds']}\nBaths: {row['num_baths']}\nDistance to TTC: {row['distance_to_subway']}m",
    ).add_to(toronto_map)

# Save map as HTML file
toronto_map.save('Real_Estate_Subway_Map.html')

# Display message
print("Map created successfully! You can open 'Real_Estate_Subway_Map.html' to view it.")
