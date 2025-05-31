"""
Model Inference Script for fraud-detection-federated
Loads a trained model and performs inference on sample transaction amounts.
"""
import numpy as np
from tensorflow.keras.models import load_model

# Load a pre-trained model
model = load_model("../models/simple_model.h5")

# Simulate new transaction amounts (e.g., in dollars)
sample_transactions = np.array([[120.0], [5000.0], [75.5]])

# Perform prediction
predictions = model.predict(sample_transactions)

# Print results
for i, amount in enumerate(sample_transactions):
    print(f"Transaction: ${amount[0]:.2f} -> Fraud Probability: {predictions[i][0]:.4f}")

def load_sample_transactions():
    return np.array([[300.0], [720.5], [45.0], [9500.0]])
