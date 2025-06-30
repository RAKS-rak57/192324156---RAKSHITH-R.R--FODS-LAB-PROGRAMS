import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset: [Age, Annual Income (k$), Spending Score (1–100)]
data = {
    'CustomerID': range(1, 11),
    'Age': [19, 35, 26, 27, 19, 27, 27, 32, 25, 35],
    'AnnualIncome': [15, 35, 25, 40, 20, 35, 45, 20, 30, 60],
    'SpendingScore': [39, 81, 6, 77, 40, 76, 6, 94, 3, 40]
}

df = pd.DataFrame(data)

# Features for clustering
X = df[['Age', 'AnnualIncome', 'SpendingScore']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine optimal number of clusters using Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Curve
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o', color='teal')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.tight_layout()
plt.show()

# Apply KMeans with chosen k (e.g., 3)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
df['Segment'] = kmeans.fit_predict(X_scaled)

# Visualize clusters
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='AnnualIncome', y='SpendingScore', hue='Segment', palette='Set2', s=100)
plt.title("Customer Segments Based on Income and Spending")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1–100)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Display segmented data
print("\n📊 Segmented Customer Data:")
print(df[['CustomerID', 'Age', 'AnnualIncome', 'SpendingScore', 'Segment']])
