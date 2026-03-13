import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from kdd_column_names import column_names

# File path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")

# Load dataset
df = pd.read_csv(data_path, names=column_names)

# -----------------------------
# 1. Scatter Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['src_bytes'], df['dst_bytes'])

plt.xlabel("src_bytes")
plt.ylabel("dst_bytes")
plt.title("Scatter Plot between src_bytes and dst_bytes")

plt.show()

# -----------------------------
# 2. Pearson Correlation
# -----------------------------
correlation = df['src_bytes'].corr(df['dst_bytes'])

print("Pearson Correlation between src_bytes and dst_bytes:", correlation)

# -----------------------------
# 3. Violin Plot
# -----------------------------
plt.figure(figsize=(8,5))
sns.violinplot(x=df['src_bytes'])

plt.title("Violin Plot of src_bytes")

plt.show()