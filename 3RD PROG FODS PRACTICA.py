import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load CSV and convert to NumPy
df = pd.read_csv('house_data.csv')
house_data = df.to_numpy()

# Filter houses with more than 4 bedrooms
filtered = house_data[house_data[:, 0] > 4]
avg_price = filtered[:, 2].mean()

# GUI setup
root = tk.Tk()
root.title("House Price Analyzer")
root.geometry("700x500")

tk.Label(root, text="Average Sale Price of Houses with >4 Bedrooms", font=("Arial", 14)).pack(pady=10)

# Plotting
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(['Avg Price'], [avg_price], color='mediumseagreen')
ax.set_ylabel("Sale Price (₹)")
ax.set_title("Average Price for Houses with >4 Bedrooms")
ax.bar_label(ax.containers[0], fmt='₹%.0f', label_type='edge')
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Button to show value in popup
def show_summary():
    messagebox.showinfo("Average Price", f"₹{avg_price:,.2f} is the average sale price\nfor houses with more than 4 bedrooms.")

tk.Button(root, text="Show Summary", font=("Arial", 12), command=show_summary).pack(pady=15)

root.mainloop()
