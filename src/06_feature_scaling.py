import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from kdd_column_names import column_names

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")

df = pd.read_csv(data_path, names=column_names)

X = df.select_dtypes(include=['int64','float64'])

minmax = MinMaxScaler()
X_minmax = minmax.fit_transform(X)

standard = StandardScaler()
X_standard = standard.fit_transform(X)

print("Feature Scaling Completed")
