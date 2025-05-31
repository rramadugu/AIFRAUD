"""
Loads CSV data into Pandas DataFrames.
"""
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preview_data(df, n=5):
    print("Previewing first few rows:")
    print(df.head(n))
