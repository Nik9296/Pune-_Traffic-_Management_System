
import pandas as pd #to read CSV data.
import folium  # to draw interactive maps.
from geopy.geocoders import Nominatim #to fetch latitude/longitude for place names.

# Load traffic data
data = pd.read_csv(r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\pune_traffic_data.csv")

print("Columns in CSV:", data.columns)  
print("Unique locations in CSV:", data['Location'].unique())  # Debugging

# Geopy setup
geolocator = Nominatim(user_agent="pune_traffic")

# Function to get coordinates
def get_coordinates(location):
    # Normalize strings for matching
    row = data[data['Location'].str.lower().str.strip() == location.lower().strip()]
    if not row.empty:
        # If CSV already has lat/lon use them
        if 'Latitude' in data.columns and 'Longitude' in data.columns:
            return float(row['Latitude'].values[0]), float(row['Longitude'].values[0])
        else:
            # Otherwise fetch using geopy
            loc = geolocator.geocode(f"{location}, Pune, India")
            if loc:
                return loc.latitude, loc.longitude
            else:
                print(f"⚠️ Could not find coordinates for {location}")
                exit()
    else:
        # Not found in CSV → fallback to geopy
        loc = geolocator.geocode(f"{location}, Pune, India")
        if loc:
            print(f"📍 {location} not in dataset, fetched from Geopy")
            return loc.latitude, loc.longitude
        else:
            print(f"❌ Location '{location}' not found in dataset or geopy.")
            exit()

# Function to estimate travel time
def estimate_time(route_traffic):
    if not route_traffic:
        return 0, 0
    avg_speed = sum([20 if t == 'High' else 40 if t == 'Medium' else 60 for t in route_traffic]) / len(route_traffic)
    distance = len(route_traffic) * 1  # Assume each segment = 1 km
    time = (distance / avg_speed) * 60  # minutes
    return distance, time

# User input
start_location = input("Enter your current location (e.g., Hadapsar): ")
end_location = input("Enter your destination (e.g., Kothrud): ")

start_coords = get_coordinates(start_location)
end_coords = get_coordinates(end_location)

# Create map
map_ = folium.Map(location=start_coords, zoom_start=12)

# Example route traffic conditions
main_route_traffic = ['High', 'Medium', 'Low', 'High', 'Medium']
alt_route_traffic = ['Medium', 'Low', 'Low', 'Medium']

# Estimate times
main_distance, main_time = estimate_time(main_route_traffic)
alt_distance, alt_time = estimate_time(alt_route_traffic)

# Add start/end markers
folium.Marker(start_coords, popup=start_location, icon=folium.Icon(color="blue")).add_to(map_)
folium.Marker(end_coords, popup=end_location, icon=folium.Icon(color="blue")).add_to(map_)

# Draw main route
route_coords = [start_coords]
for traffic in main_route_traffic:
    color = 'red' if traffic == 'High' else 'yellow' if traffic == 'Medium' else 'green'
    next_coord = (route_coords[-1][0] + 0.01, route_coords[-1][1] + 0.01)
    folium.PolyLine([route_coords[-1], next_coord], color=color, weight=5).add_to(map_)
    route_coords.append(next_coord)

folium.Marker(route_coords[-1],
              popup=f"Main Route: {main_distance} km, {main_time:.2f} mins",
              icon=folium.Icon(color="blue")).add_to(map_)

# Draw alternative route
alt_coords = [(start_coords[0] + 0.01, start_coords[1] - 0.01)]
for traffic in alt_route_traffic:
    color = 'red' if traffic == 'High' else 'yellow' if traffic == 'Medium' else 'green'
    next_coord = (alt_coords[-1][0] + 0.01, alt_coords[-1][1] - 0.01)
    folium.PolyLine([alt_coords[-1], next_coord], color=color, weight=5, dash_array='5, 10').add_to(map_)
    alt_coords.append(next_coord)

folium.Marker(alt_coords[-1],
              popup=f"Alt Route: {alt_distance} km, {alt_time:.2f} mins",
              icon=folium.Icon(color="green")).add_to(map_)

# Add traffic legend
legend_html = '''
<div style="position: fixed; bottom: 50px; left: 50px; width: 150px; height: 90px;
     background-color: white; border:2px solid grey; z-index:9999; font-size:14px;">
     <b>&nbsp; Traffic Levels</b><br>
     &nbsp; <i style="color:red;">●</i> High<br>
     &nbsp; <i style="color:yellow;">●</i> Medium<br>
     &nbsp; <i style="color:green;">●</i> Low<br>
</div>
'''
map_.get_root().html.add_child(folium.Element(legend_html))

# Save map
map_.save(r"C:\Users\NIKHIL\Desktop\New folder\data\traffic_route_map.html")
print("✅ Map saved at: C:\\Users\\NIKHIL\\Desktop\\New folder\\data\\traffic_route_map.html")
