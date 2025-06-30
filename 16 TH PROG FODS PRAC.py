import string, pandas as pd
from collections import Counter
import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.corpus import stopwords

# Download stopwords once
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Sample dataset
df = pd.DataFrame({'ReviewID': [1, 2, 3, 4], 
                   'ReviewText': ["Great product, really loved it!", 
                                  "Good quality but too expensive.", 
                                  "Worth the price.", 
                                  "Not bad, but expected better quality."]})

# Function to run on button click
def analyze_reviews():
    words = ' '.join(df['ReviewText']).lower().translate(str.maketrans('', '', string.punctuation)).split()
    filtered_words = [word for word in words if word not in stop_words]
    word_freq = Counter(filtered_words)
    result = "\n".join(f"{word}: {count}" for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    messagebox.showinfo("Enhanced Word Frequency Distribution", result)

# GUI setup
root = tk.Tk()
root.title("Text Reviewer")
root.geometry("400x200")

button = tk.Button(root, text="Begin", font=("Arial", 14), command=analyze_reviews)
button.pack(pady=60)

root.mainloop()
