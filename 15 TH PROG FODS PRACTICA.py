import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset: Post IDs and Like counts
data = {
    'PostID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Likes': [5, 12, 5, 18, 12, 25, 5, 30, 18, 25]
}

df = pd.DataFrame(data)

# Frequency distribution of likes
like_freq = df['Likes'].value_counts().sort_index()

# Display frequency table
print("Frequency Distribution of Likes per Post:")
print(like_freq)

# Plot the distribution
plt.figure(figsize=(8, 5))
bars = plt.bar(like_freq.index.astype(str), like_freq.values, color='coral')
plt.title("Frequency Distribution of Likes Across Posts")
plt.xlabel("Number of Likes")
plt.ylabel("Number of Posts")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.bar_label(bars)
plt.tight_layout()
plt.show()
