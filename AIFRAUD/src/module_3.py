"""
Performs feature engineering operations.
"""
import numpy as np

def log_transform(df, column):
    df[f"log_{column}"] = np.log(df[column] + 1)
    return df

def create_ratio_feature(df, num_col, denom_col):
    df[f"{num_col}_to_{denom_col}"] = df[num_col] / (df[denom_col] + 1e-5)
    return df
