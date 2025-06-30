import pandas as pd
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load dataset
df = pd.read_csv('monthly_sales.csv')

# Group and get top 5 products by quantity sold
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)

# GUI setup
root = tk.Tk()
root.title("Top 5 Products Sold")
root.geometry("700x500")

tk.Label(root, text="Top 5 Best-Selling Products", font=("Arial", 14)).pack(pady=10)

# Plotting
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(top_products.index, top_products.values, color='mediumslateblue')
ax.set_ylabel("Total Quantity Sold")
ax.set_title("Top 5 Products by Sales Volume")
ax.bar_label(ax.containers[0])
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Summary popup
def show_summary():
    summary = "\n".join(f"{prod}: {qty} units" for prod, qty in top_products.items())
    messagebox.showinfo("Top 5 Products", summary)

tk.Button(root, text="Show Summary", font=("Arial", 12), command=show_summary).pack(pady=15)

root.mainloop()
