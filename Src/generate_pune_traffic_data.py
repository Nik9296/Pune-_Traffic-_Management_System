import pandas as pd
import random

# Define parameters
num_entries = 5500  # More than 5000 entries

# Define data options
time_slots = [f"{hour:02d}:00" for hour in range(24)]  # 24-hour format
days = ["Weekday", "Weekend"]
locations = [
    "Shivajinagar", "Hinjawadi", "Baner", "Viman Nagar", "Kothrud", "Magarpatta",
    "Pimple Saudagar", "Wakad", "Hadapsar", "FC Road", "Deccan", "Koregaon Park"
]
traffic_levels = ["Low", "Medium", "High", "Severe"]
accidents = ["Yes", "No"]
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Foggy"]

# Generate data
data = {
    "Time": [random.choice(time_slots) for _ in range(num_entries)],
    "Day": [random.choice(days) for _ in range(num_entries)],
    "Location": [random.choice(locations) for _ in range(num_entries)],
    "Vehicles Count": [random.randint(50, 500) for _ in range(num_entries)],
    "Traffic Level": [random.choice(traffic_levels) for _ in range(num_entries)],
    "Accidents Reported": [random.choice(accidents) for _ in range(num_entries)],
    "Weather": [random.choice(weather_conditions) for _ in range(num_entries)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv(r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\pune_traffic_data.csv", index=False)
print("✅ Pune traffic dataset generated successfully with 5500+ entries!")
