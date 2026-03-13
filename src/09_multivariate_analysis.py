import pandas as pd
import os
import seaborn as sns  
import matplotlib.pyplot as plt
from kdd_column_names import column_names

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "KDDTrain+.txt")
 
df = pd.read_csv(data_path, names=column_names)

sns.pairplot(df[['src_bytes','dst_bytes','count','srv_count']])
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(df.select_dtypes(include=['number']).corr(), cmap='coolwarm')
plt.show()
