"""
Configuration file for directories and constants.
"""
import os

DATA_DIR = os.getenv("DATA_DIR", "data/")
MODEL_DIR = os.getenv("MODEL_DIR", "models/")
NOTEBOOK_DIR = os.getenv("NOTEBOOK_DIR", "notebooks/")

def get_paths():
    return {
        "data": DATA_DIR,
        "models": MODEL_DIR,
        "notebooks": NOTEBOOK_DIR
    }
