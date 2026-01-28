import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_model():
    # Load dataset
    data_path = "landslide_prediction/data/landslide_data.csv"
    df = pd.read_csv(data_path)
    
    # Features and Target
    X = df[["rainfall", "soil_moisture", "vibration", "humidity", "temperature"]]
    y = df["risk"]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    
    # Save model
    model_path = "landslide_prediction/ml/model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(clf, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
