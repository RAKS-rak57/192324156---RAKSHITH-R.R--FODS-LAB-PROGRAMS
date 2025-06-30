import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset: CustomerID, TotalSpent (₹), ItemsPurchased
data = {
    'CustomerID': range(1, 11),
    'TotalSpent': [1200, 2500, 800, 3000, 1500, 4000, 600, 2200, 1800, 3500],
    'ItemsPurchased': [2, 5, 1, 6, 3, 8, 1, 4, 3, 7]
}

df = pd.DataFrame(data)

# Features for clustering
X = df[['TotalSpent', 'ItemsPurchased']]

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
sns.scatterplot(data=df, x='TotalSpent', y='ItemsPurchased', hue='Segment', palette='Set2', s=100)
plt.title("Customer Segments Based on Spending and Purchase Volume")
plt.xlabel("Total Spent (₹)")
plt.ylabel("Items Purchased")
plt.grid(True)
plt.tight_layout()
plt.show()

# Display segmented data
print("\n📊 Segmented Customer Data:")
print(df[['CustomerID', 'TotalSpent', 'ItemsPurchased', 'Segment']])
