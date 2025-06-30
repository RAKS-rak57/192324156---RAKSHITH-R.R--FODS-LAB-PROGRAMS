import numpy as np
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 4x4 matrix (each row = student, each column = subject)
# You can expand this to 32x4 for full analysis
student_scores = np.array([
    [78, 85, 90, 72],
    [88, 79, 85, 80],
    [91, 92, 89, 86],
    [76, 81, 77, 84]
])

subjects = ['Math', 'Science', 'English', 'History']
avg_scores = student_scores.mean(axis=0)
top_index = np.argmax(avg_scores)
top_subject = subjects[top_index]

# GUI
root = tk.Tk()
root.title("Student Performance Analyzer")
root.geometry("700x500")

tk.Label(root, text="Subject-wise Average Scores", font=("Arial", 14)).pack(pady=10)

# Matplotlib plot
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(subjects, avg_scores, color='skyblue')
bars[top_index].set_color('orange')  # Highlight top subject
ax.set_ylabel("Average Score")
ax.set_title("Average Scores per Subject")
for i, score in enumerate(avg_scores):
    ax.text(i, score + 0.5, f"{score:.1f}", ha='center')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Button action
def show_results():
    result = "\n".join(f"{subjects[i]}: {avg_scores[i]:.2f}" for i in range(len(subjects)))
    messagebox.showinfo("Subject Averages", f"{result}\n\nTop Scoring Subject: {top_subject}")

tk.Button(root, text="Show Summary", font=("Arial", 12), command=show_results).pack(pady=15)

root.mainloop()
