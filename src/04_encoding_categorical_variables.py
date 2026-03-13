import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from kdd_column_names import column_names

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")

df = pd.read_csv(data_path, names=column_names)

# Encode target
le = LabelEncoder()
df['class'] = le.fit_transform(df['class'])

# One-hot encoding
df = pd.get_dummies(df, columns=['protocol_type','service','flag'])

print("Encoding Successful")
