import matplotlib.pyplot as plt
import seaborn as sns

def plot_traffic_distribution(df):
    sns.countplot(data=df, x='Traffic Level')
    plt.show()
