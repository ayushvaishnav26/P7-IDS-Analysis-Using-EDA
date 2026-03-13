import pandas as pd
import os
from kdd_column_names import column_names

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")

df = pd.read_csv(data_path, names=column_names)

print("Missing Values:")
print(df.isnull().sum())

numeric_cols = df.select_dtypes(include=['int64','float64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

df = df.dropna()

print("Missing values handled successfully.")
