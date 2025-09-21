from sklearn.model_selection import train_test_split #Imports scikit-learn modules for machine learning.
from sklearn.tree import DecisionTreeClassifier #is used to bring the Decision Tree algorithm into your code so you can build a machine learning model.

def predict_traffic(df):
    df = df.replace({'Day': {'Weekday': 0, 'Weekend': 1}})
    X = df[['Time', 'Day', 'Vehicles Count']]
    y = df['Traffic Level']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    print(f"Accuracy: {model.score(X_test, y_test) * 100:.2f}%")
