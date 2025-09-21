from src.data_loader import load_data
from src.analysis import analyze_traffic
from src.visualization import plot_traffic_distribution
from src.prediction import predict_traffic

df = load_data(r"C:\Users\NIKHIL\Desktop\New folder\PuneTrafficManagement\data\pune_traffic_data.csv")
analyze_traffic(df)
plot_traffic_distribution(df)
predict_traffic(df)
