import pandas as pd
import os
import numpy as np
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from kdd_column_names import column_names

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")

df = pd.read_csv(data_path, names=column_names)

numeric_cols = df.select_dtypes(include=['int64','float64'])

# Z-score
z_scores = np.abs(zscore(numeric_cols))
print("Z-score outliers:", (z_scores > 3).sum().sum())

# Isolation Forest
iso = IsolationForest(contamination=0.05, random_state=0)
outliers_iso = iso.fit_predict(numeric_cols)
print("Isolation Forest outliers:", sum(outliers_iso == -1))

# LOF
numeric_cols = numeric_cols.fillna(numeric_cols.mean())
lof = LocalOutlierFactor()
outliers_lof = lof.fit_predict(numeric_cols)
print("LOF outliers:", sum(outliers_lof == -1))
