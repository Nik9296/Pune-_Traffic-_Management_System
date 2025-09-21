import pandas as pd
import folium  #Create interactive maps in Python.

# Load the dataset
file_path = r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\pune_traffic_data.csv"
df = pd.read_csv(file_path)

# Normalize column names (lowercase + remove spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("✅ Columns after cleaning:", df.columns.tolist())

# Create a map centered around Pune
pune_map = folium.Map(location=[18.5204, 73.8567], zoom_start=12)

# Define color mapping
def get_color(traffic_level):
    if traffic_level.lower() == "low":
        return "green"
    elif traffic_level.lower() == "medium":
        return "yellow"
    else:
        return "red"

# Filter by traffic levels safely
if "traffic_level" in df.columns and "latitude" in df.columns and "longitude" in df.columns:
    low_traffic = df[df['traffic_level'].str.lower() == 'low'].sample(min(10, len(df)))
    medium_traffic = df[df['traffic_level'].str.lower() == 'medium'].sample(min(10, len(df)))
    high_traffic = df[df['traffic_level'].str.lower().isin(['high', 'severe'])].sample(min(10, len(df)))

    filtered_df = pd.concat([low_traffic, medium_traffic, high_traffic])

    # Plot points
    for _, row in filtered_df.iterrows():
        folium.CircleMarker(
            location=(row['latitude'], row['longitude']),
            radius=7,
            color=get_color(row['traffic_level']),
            fill=True,
            fill_color=get_color(row['traffic_level']),
            fill_opacity=0.7
        ).add_to(pune_map)

    # Save map
    heatmap_file = r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\traffic_heatmap.html"
    pune_map.save(heatmap_file)
    print(f"✅ Focused traffic heatmap created: {heatmap_file}")
else:
    print("❌ Your dataset does not have required columns (latitude, longitude, traffic_level).")
