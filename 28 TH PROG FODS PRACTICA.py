import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample dataset: [Annual Income (k$), Spending Score (1–100)]
data = {
    'AnnualIncome': [15, 16, 17, 18, 19, 20, 70, 75, 80, 85, 90, 95],
    'SpendingScore': [39, 81, 6, 77, 40, 76, 6, 94, 3, 93, 5, 90]
}

df = pd.DataFrame(data)

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Train K-Means model
k = 3  # Number of customer segments
model = KMeans(n_clusters=k, random_state=42)
model.fit(X_scaled)

# User input
print("Enter new customer details:")
income = float(input("Annual Income (in $1000s): "))
score = float(input("Spending Score (1–100): "))

# Prepare and scale input
new_customer = np.array([[income, score]])
new_scaled = scaler.transform(new_customer)

# Predict cluster
cluster = model.predict(new_scaled)[0]
print(f"\n🧠 The new customer belongs to Segment {cluster}")
