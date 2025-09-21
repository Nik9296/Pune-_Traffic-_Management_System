import pandas as pd

# Load the data
data = pd.read_csv(r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\pune_traffic_data.csv")

# Print all column names to find the correct one
print("Available Columns:")
print(data.columns)

# Display a few rows to understand the structure
print("\nSample Data:")
print(data.head())
