# train.py
# This file is used for Task 5 — .gitignore practice

import os

# These paths represent where data and models live
DATA_PATH  = "data/loan_default.csv"
MODEL_PATH = "models/best_model.pkl"


def load_data(path):
    if not os.path.exists(path):
        print(f"Data file not found at: {path}")
        print("Place your CSV file in the data/ folder and try again.")
        return None
    print(f"Loading data from {path}...")
    return path


def train_model(data_path):
    if data_path is None:
        return
    print("Training model...")
    print("Model training complete.")
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    data = load_data(DATA_PATH)
    train_model(data)
