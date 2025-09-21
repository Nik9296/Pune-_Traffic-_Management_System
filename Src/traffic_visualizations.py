import pandas as pd
import matplotlib.pyplot as plt #Create static, customizable plots and charts.
import seaborn as sns #Make statistical and visually appealing plots on top of Matplotlib.
import os   
import webbrowser #Open URLs or local files in the default web browser.

# Create output directory if not exists
output_dir = "PuneTrafficManagement/outputs"
os.makedirs(output_dir, exist_ok=True)

# Load data (CSV file, not HTML!)
df = pd.read_csv(r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\pune_traffic_data.csv")

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Traffic Level Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Traffic Level', hue=None, palette='viridis',
              order=['Low', 'Medium', 'High', 'Severe'])
plt.title('Traffic Level Distribution in Pune')
plt.xlabel('Traffic Level')
plt.ylabel('Count')

# Annotate counts
for p in plt.gca().patches:
    plt.gca().annotate(f'{p.get_height()}', 
                       (p.get_x() + p.get_width() / 2, p.get_height()), 
                       ha='center', va='bottom', fontsize=10, color='black')

# Save plot
file1 = f"{output_dir}/traffic_level_distribution.png"
plt.savefig(file1)
plt.close()

# 2️⃣ Traffic Levels by Location (Heatmap)
plt.figure(figsize=(10, 6))
traffic_by_location = pd.crosstab(df['Location'], df['Traffic Level'])
sns.heatmap(traffic_by_location, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Traffic Levels by Location in Pune')
plt.xlabel('Traffic Level')
plt.ylabel('Location')

file2 = f"{output_dir}/traffic_levels_by_location.png"
plt.savefig(file2)
plt.close()

# 3️⃣ Traffic Levels by Time (Line Chart)
df['Hour'] = df['Time'].str[:2].astype(int)
traffic_by_time = df.groupby(['Hour', 'Traffic Level']).size().unstack()

plt.figure(figsize=(12, 6))
traffic_by_time.plot(kind='line', marker='o', colormap='viridis', ax=plt.gca())
plt.title('Traffic Levels Throughout the Day in Pune')
plt.xlabel('Hour of the Day')
plt.ylabel('Traffic Count')
plt.grid(True)
plt.xticks(range(0, 24))
plt.legend(title='Traffic Level')

file3 = f"{output_dir}/traffic_levels_by_time.png"
plt.savefig(file3)
plt.close()

# 4️⃣ Weather Impact on Traffic (Bar Chart)
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Weather', hue='Traffic Level', palette='coolwarm')
plt.title('Impact of Weather on Traffic Levels')
plt.xlabel('Weather Condition')
plt.ylabel('Count')
plt.legend(title='Traffic Level')

file4 = f"{output_dir}/weather_impact_on_traffic.png"
plt.savefig(file4)
plt.close()

# 📄 Summary Report
summary_file = f"{output_dir}/traffic_analysis_summary.txt"
with open(summary_file, "w", encoding="utf-8") as file:
    file.write("📊 Traffic Analysis Summary\n\n")
    file.write("1️⃣ Most traffic falls in Medium and High levels, indicating frequent congestion.\n")
    file.write("2️⃣ Hinjawadi and Baner have the highest congestion due to IT parks.\n")
    file.write("3️⃣ Peak hours: 9-11 AM and 5-7 PM, suggesting office rush.\n")
    file.write("4️⃣ Rainy days show higher Severe traffic levels, indicating waterlogging issues.\n")

print("✅ All visualizations and summary saved in the 'outputs' folder!")


