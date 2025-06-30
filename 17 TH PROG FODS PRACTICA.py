import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already present
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("data.csv")

# Combine all feedback into one string
text = " ".join(df['feedback'].dropna()).lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize and remove stopwords
words = text.split()
filtered_words = [word for word in words if word not in stopwords.words('english')]

# Count word frequencies
word_freq = Counter(filtered_words)

# Ask user for N
N = int(input("Enter the number of top frequent words to display: "))
top_words = word_freq.most_common(N)

# Display results
print(f"\nTop {N} most frequent words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Plot bar chart
labels, values = zip(*top_words)
plt.figure(figsize=(10, 5))
bars = plt.bar(labels, values, color='mediumseagreen')
plt.title(f"Top {N} Word Frequencies in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.bar_label(bars)
plt.tight_layout()
plt.show()
