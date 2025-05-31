"""
Trains a Random Forest classifier on input features and labels.
"""
from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def save_model(model, filepath):
    import joblib
    joblib.dump(model, filepath)
