from collections import Counter
import string
import matplotlib.pyplot as plt

# Read and clean the text
with open("sample_text.txt", "r") as file:
    text = file.read()

# Count spaces before cleaning
space_count = text.count(' ')

# Normalize text for word frequency
cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
words = cleaned_text.split()

# Count word frequencies
word_freq = Counter(words)

# Display top 10 most common words
print("Top 10 most frequent words:")
for word, freq in word_freq.most_common(10):
    print(f"{word}: {freq}")

print(f"\nTotal number of spaces in the text: {space_count}")

# Plot frequency distribution
top_words = word_freq.most_common(10)
labels, values = zip(*top_words)

plt.figure(figsize=(10, 5))
bars = plt.bar(labels, values, color='skyblue')
plt.title("Top 10 Word Frequency Distribution")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.bar_label(bars)
plt.tight_layout()
plt.show()
