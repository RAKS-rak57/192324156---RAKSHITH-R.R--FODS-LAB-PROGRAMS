import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset: Customer IDs and Ages
data = {
    'CustomerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010'],
    'Age': [25, 32, 25, 40, 29, 32, 40, 25, 29, 35]
}

# Create DataFrame
df = pd.DataFrame(data)

# Frequency distribution of ages
age_freq = df['Age'].value_counts().sort_index()

# Display frequency table
print("Frequency Distribution of Customer Ages:")
print(age_freq)

# Plot histogram
plt.figure(figsize=(8, 5))
bars = plt.bar(age_freq.index.astype(str), age_freq.values, color='skyblue')
plt.title("Customer Age Frequency Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.bar_label(bars)
plt.tight_layout()
plt.show()
