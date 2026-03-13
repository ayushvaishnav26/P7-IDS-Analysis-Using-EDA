import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
from kdd_column_names import column_names

# Set plot style
sns.set_style("whitegrid")

# File path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")

# Load dataset
df = pd.read_csv(data_path, names=column_names)

# Select feature for analysis
feature = 'src_bytes'

# -------------------------------
# 1. Histogram with KDE
# -------------------------------
plt.figure(figsize=(10,6))
sns.histplot(df[feature], kde=True, bins=100)

plt.title("Histogram with KDE of src_bytes")
plt.xlabel("src_bytes")
plt.ylabel("Frequency")

plt.show()

# -------------------------------
# 2. Box Plot (Outlier Detection)
# -------------------------------
plt.figure(figsize=(10,4))
sns.boxplot(x=df[feature])

plt.title("Boxplot of src_bytes (Outlier Detection)")
plt.xlabel("src_bytes")

plt.show()

# -------------------------------
# 3. Calculate Skewness
# -------------------------------
skew_value = skew(df[feature])
print("Skewness of src_bytes:", skew_value)

# -------------------------------
# 4. Statistical Summary
# -------------------------------
print("\nStatistical Summary:")
print(df[feature].describe())