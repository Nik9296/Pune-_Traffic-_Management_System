import pandas as pd
import folium #Create interactive maps in Python.
import osmnx as ox #Download and work with street networks from OpenStreetMap.
import networkx as nx #Analyze and manipulate graphs and networks.
from geopy.geocoders import Nominatim #Convert place names to latitude and longitude (geocoding).
from geopy.distance import geodesic #Calculate distance between two geographic points.
import time

# -------------------------
# Load traffic data
# -------------------------
file_path = r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\pune_traffic_data.csv"
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip().str.lower()
print("Columns in dataset:", df.columns.tolist())

# -------------------------
# Geocoder setup
# -------------------------
geolocator = Nominatim(user_agent="route_planner")

# -------------------------
# Pre-geocode dataset locations (once)
# -------------------------
location_coords = {}
for loc_name in df['location'].unique():
    try:
        loc = geolocator.geocode(f"{loc_name}, Pune, India", timeout=10)
        if loc:
            location_coords[loc_name] = (loc.latitude, loc.longitude)
        time.sleep(1)  # avoid Nominatim rate limit
    except:
        continue

if not location_coords:
    print("❌ No dataset locations could be geocoded.")
    exit()

# -------------------------
# User input
# -------------------------
start_location = input("Enter your current location (e.g., Hadapsar): ")
end_location = input("Enter your destination (e.g., Kothrud): ")

start_coords = geolocator.geocode(f"{start_location}, Pune, India")
end_coords = geolocator.geocode(f"{end_location}, Pune, India")

if not start_coords or not end_coords:
    print("❌ Unable to find one of the locations.")
    exit()

start_lat, start_lon = start_coords.latitude, start_coords.longitude
end_lat, end_lon = end_coords.latitude, end_coords.longitude

# -------------------------
# Create map
# -------------------------
pune_map = folium.Map(location=[start_lat, start_lon], zoom_start=12)

# -------------------------
# Download Pune road network
# -------------------------
G = ox.graph_from_place("Pune, India", network_type='drive')
start_node = ox.distance.nearest_nodes(G, start_lon, start_lat)
end_node = ox.distance.nearest_nodes(G, end_lon, end_lat)

# -------------------------
# Shortest path
# -------------------------
route = nx.shortest_path(G, start_node, end_node, weight='length')

# -------------------------
# Traffic check function
# -------------------------
def is_traffic_high(lat, lon):
    # Find nearest pre-geocoded dataset location
    nearest_loc = min(location_coords.items(), key=lambda x: geodesic((lat, lon), x[1]).meters)[0]
    traffic_col = [c for c in df.columns if 'traffic' in c.lower()][0]
    traffic_level = df[df['location'] == nearest_loc][traffic_col].iloc[0]
    return traffic_level.lower() == 'high'

# -------------------------
# Plot route and traffic
# -------------------------
route_coords = []
high_traffic_coords = []

for i in range(len(route)-1):
    lat1, lon1 = G.nodes[route[i]]['y'], G.nodes[route[i]]['x']
    lat2, lon2 = G.nodes[route[i+1]]['y'], G.nodes[route[i+1]]['x']
    route_coords.append(((lat1, lon1), (lat2, lon2)))
    if is_traffic_high(lat1, lon1) or is_traffic_high(lat2, lon2):
        high_traffic_coords.append(((lat1, lon1), (lat2, lon2)))

# Draw main route
for segment in route_coords:
    color = 'green' if segment not in high_traffic_coords else 'red'
    folium.PolyLine([segment[0], segment[1]], color=color, weight=5).add_to(pune_map)

# Draw high traffic segments with dashed red
for segment in high_traffic_coords:
    folium.PolyLine([segment[0], segment[1]], color='red', weight=5, dash_array='5,5').add_to(pune_map)

# Add markers
folium.Marker([start_lat, start_lon], popup=start_location, icon=folium.Icon(color="blue")).add_to(pune_map)
folium.Marker([end_lat, end_lon], popup=end_location, icon=folium.Icon(color="blue")).add_to(pune_map)

# Save map
route_file = r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\optimized_route.html"
pune_map.save(route_file)
print(f"✅ Optimized route map created: {route_file}")
