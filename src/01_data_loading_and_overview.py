import pandas as pd
import os
from kdd_column_names import column_names

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")

df = pd.read_csv(data_path, names=column_names)

print(df.head())
print("Shape:", df.shape)
print(df.info())
