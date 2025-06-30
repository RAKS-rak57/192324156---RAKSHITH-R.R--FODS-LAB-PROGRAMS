import numpy as np
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample 3x3 matrix: rows = products, columns = individual sale prices
sales_data = np.array([
    [120.5, 130.0, 125.7],
    [95.0,  98.5, 102.0],
    [150.2, 145.9, 149.0]
])

product_names = ['Product A', 'Product B', 'Product C']
product_averages = sales_data.mean(axis=1)
overall_average = sales_data.mean()

# GUI Setup
root = tk.Tk()
root.title("Monthly Sales Analyzer")
root.geometry("700x500")

tk.Label(root, text="Average Prices per Product", font=("Arial", 14)).pack(pady=10)

# Plot average price per product
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(product_names, product_averages, color='orchid')
for i, val in enumerate(product_averages):
    ax.text(i, val + 0.5, f"{val:.2f}", ha='center')

ax.axhline(y=overall_average, color='gray', linestyle='--', label="Overall Average")
ax.legend()
ax.set_ylabel("Average Price")
ax.set_title("Price Analysis")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Button to show the overall average in a popup
def show_summary():
    messagebox.showinfo("Overall Average Price", f"Average Price Across All Sales:\n₹{overall_average:.2f}")

tk.Button(root, text="Show Overall Average", font=("Arial", 12), command=show_summary).pack(pady=15)

root.mainloop()
