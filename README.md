# 🛡️ IDS Analysis Using Exploratory Data Analysis (EDA)

This project performs **Exploratory Data Analysis (EDA)** on the **KDD Intrusion Detection Dataset** to understand network traffic behavior and identify patterns that may indicate malicious activity.

The goal is to analyze network features, detect anomalies, and gain insights into potential attack patterns before applying machine learning models.

---

## 📊 Project Overview

Intrusion Detection Systems (IDS) help monitor network traffic and detect suspicious or malicious activities.

In this project, we perform **step-by-step exploratory data analysis** to:

- Understand the distribution of network features
- Detect outliers and anomalies
- Identify relationships between variables
- Prepare the dataset for machine learning

---

## 📂 Project Structure

```
IDS-Analysis-Using-EDA
│
├── data
│   └── KDDTrain+.txt
│
├── src
│   ├── 01_data_loading_and_overview.py
│   ├── 02_missing_value_handling.py
│   ├── 03_variable_extraction.py
│   ├── 04_encoding_categorical_variables.py
│   ├── 05_train_test_split.py
│   ├── 06_feature_scaling.py
│   ├── 07_univariate_analysis.py
│   ├── 08_bivariate_analysis.py
│   ├── 09_multivariate_analysis.py
│   ├── 10_outlier_detection_and_feature_engineering.py
│   └── kdd_column_names.py
│
├── questions.txt
│
├── outputs
│   └── (EDA visualizations and plots)
│
├── requirements.txt
└── README.md
```

---

## 🔍 Exploratory Data Analysis

### Univariate Analysis
Analyzing individual features to understand their distribution.

Examples:
- Histogram of `src_bytes`
- Boxplot for outlier detection
- Skewness analysis

---

### Bivariate Analysis
Examining relationships between two variables.

Examples:
- Scatter plots
- Pearson correlation
- Violin plots

---

### Multivariate Analysis
Understanding relationships among multiple features.

Examples:
- Correlation heatmap
- Feature interaction analysis

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy

---

## 📊 Dataset

This project uses the **KDD Cup 1999 Intrusion Detection Dataset**.

The dataset contains simulated network traffic including:

- Normal connections
- Various types of cyber attacks

It is widely used for **Intrusion Detection System (IDS) research**.

---

## 🎯 Project Objective

The objective of this project is to:

- Analyze network traffic patterns
- Identify abnormal behavior
- Understand features useful for intrusion detection
- Prepare the dataset for machine learning models

---

## 🚀 Future Improvements

Future enhancements may include:

- Machine learning based intrusion detection
- Attack classification models
- Feature importance analysis
- Automated anomaly detection

---

## 👨‍💻 Author

**Ayush Kumar**

📧 Email: ayush.vaishnav@outlook.com  
🔗 LinkedIn: https://linkedin.com/in/ayushvaishnav26  
💻 GitHub: https://github.com/ayushvaishnav26  

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository  
🔗 Share it with others learning cybersecurity and data analysis