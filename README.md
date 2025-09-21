

# 🚦 Pune Traffic Management System

This repository contains a Python-based project for visualizing and managing traffic in Pune city. The system leverages real-time traffic data and geospatial analysis to help monitor congestion, suggest alternative routes, and optimize traffic flow using Python, Pandas, Folium, and other data science tools.

---

## 📂 Dataset

The traffic dataset includes the following features:
- Latitude & Longitude of locations
- Traffic Level (Low, Medium, High)
- Vehicles Count
- Time and Day of record

The dataset is stored in a CSV file, e.g. `pune_traffic_data.csv`. Ensure that the path in the code matches your local setup.

---

## 🏗️ System Features

- **Traffic Visualization:** Interactive maps using Folium to visualize congestion across Pune.  
- **Alternative Routes Suggestion:** Suggests less congested paths using Dijkstra's algorithm.  
- **Heatmaps:** Displays traffic density using visual heatmaps for better planning.  
- **Real-Time Data Analysis:** Provides insights into traffic patterns based on time and location.  

---

## 🧪 Implementation Details

- **Programming Language:** Python 3.x  
- **Libraries Used:** Pandas, Folium, OSRMX, NetworkX, Geopy, Matplotlib, Seaborn  
- **Traffic Analysis:** Calculating congestion, average traffic, and suggesting alternative routes  
- **Visualization:** Heatmaps, interactive maps, charts, and graphs

---

## 💻 How to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/pune-traffic-management.git
   cd pune-traffic-management
   ```

2. **Install Dependencies**

   ```bash
   pip install pandas folium osmnx networkx geopy matplotlib seaborn
   ```

3. **Update Dataset Path**

   In the Python scripts, update the dataset path, for example:

   ```python
   file_path = r"C:\Users\NIKHIL\Desktop\PuneTrafficManagement\data\pune_traffic_data.csv"
   ```

4. **Run Scripts**

   ```bash
   python route_suggestion.py
   python traffic_visualizations.py
   python alternative_map_suggest.py
   python heatmap.py
   html optimized_route.html
   html traffic_heatmap.html
   html traffic_route_map.html
   
   ```

---

## 📦 Requirements

- Python 3.x  
- Pandas, Folium, OSRMX, NetworkX, Geopy  
- Matplotlib, Seaborn  

> Optional: A Jupyter Notebook environment for interactive visualization.

---

## 🚀 Future Enhancements

- Integrate **real-time traffic API** for live updates.  
- Implement **traffic prediction models** using Machine Learning.  
- Add **mobile or web app interface** for public accessibility.  
- Optimize **route suggestions** using advanced algorithms.

---


##   Dataset link:-
     https://drive.google.com/file/d/141TSpxlUZ_9QA3w735MK78CtI3rdtSsZ/view?usp=sharing



## 🙌 Acknowledgements

- Pune City Traffic Data contributors  
- Open-source Python libraries (Pandas, Folium, NetworkX, etc.)  
- Inspiration from traffic management research and visualization projects

---

## 📬 Contact

For any questions or feedback, feel free to reach out:  
📧 nikhildivekar041@gmail.com
