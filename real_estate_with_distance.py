# Import necessary libraries
import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import Point

# Load real estate data
real_estate_df = pd.read_csv('/mnt/data/updated_real_estate_data.csv')

# Load subway station data (assuming processed format)
subway_stations_gdf = gpd.read_file('/mnt/data/DMTI2012_Subway.shp')

# Convert real estate data into a GeoDataFrame
real_estate_gdf = gpd.GeoDataFrame(real_estate_df, geometry=gpd.points_from_xy(real_estate_df.longitude, real_estate_df.latitude))

# Define the Toronto map
toronto_map = folium.Map(location=[43.7, -79.4], zoom_start=12)

# Add real estate properties to the map
for _, row in real_estate_gdf.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=4,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=f"Price: ${row['price']:,.0f}\nSize: {row['size']} sqft\nBeds: {row['beds']}\nBaths: {row['baths']}",
    ).add_to(toronto_map)

# Add subway stations to the map
for _, row in subway_stations_gdf.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        icon=folium.Icon(color="red", icon="train", prefix="fa"),
        popup=row['NAME'],  # Assuming station name column
    ).add_to(toronto_map)

# Save map as HTML file
toronto_map.save('/mnt/data/Real_Estate_Subway_Map.html')

# Display message
print("Map created successfully! You can open 'Real_Estate_Subway_Map.html' to view it.")
