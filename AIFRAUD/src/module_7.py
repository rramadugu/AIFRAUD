"""
Applies normalization and preprocessing to data.
"""
from sklearn.preprocessing import MinMaxScaler

def normalize_amounts(X):
    scaler = MinMaxScaler()
    return scaler.fit_transform(X)

def standardize_features(X):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    return scaler.fit_transform(X)
