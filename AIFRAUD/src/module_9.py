"""
Builds and executes an end-to-end fraud detection pipeline.
"""
from module_2 import load_data
from module_3 import log_transform
from module_4 import train_random_forest
from module_5 import evaluate_model

def run_pipeline():
    df = load_data("data/data_1.csv")
    df = log_transform(df, "feature")
    model = train_random_forest(df[["feature", "log_feature"]], df["label"])
    print(evaluate_model(model, df[["feature", "log_feature"]], df["label"]))

if __name__ == "__main__":
    run_pipeline()
