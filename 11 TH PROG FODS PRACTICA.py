import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load data
df = pd.read_csv('sales_over_time.csv')

# GUI setup
root = tk.Tk()
root.title("Sales Over Time Visualizer")
root.geometry("750x550")

tk.Label(root, text="Monthly Sales Visualization", font=("Arial", 16)).pack(pady=10)

# Matplotlib figure
fig, ax = plt.subplots(figsize=(7, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Plot functions
def plot_line():
    ax.clear()
    ax.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='teal')
    ax.set_title("Line Plot - Monthly Sales")
    ax.set_ylabel("Sales (₹)")
    ax.set_xlabel("Month")
    ax.grid(True)
    canvas.draw()

def plot_scatter():
    ax.clear()
    ax.scatter(df['Month'], df['Sales'], color='darkorange', s=100)
    ax.set_title("Scatter Plot - Monthly Sales")
    ax.set_ylabel("Sales (₹)")
    ax.set_xlabel("Month")
    ax.grid(True)
    canvas.draw()

def plot_bar():
    ax.clear()
    bars = ax.bar(df['Month'], df['Sales'], color='orchid')
    ax.set_title("Bar Plot - Monthly Sales")
    ax.set_ylabel("Sales (₹)")
    ax.set_xlabel("Month")
    ax.bar_label(bars, fmt='₹%d')
    canvas.draw()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Line Plot", font=("Arial", 12), command=plot_line).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Scatter Plot", font=("Arial", 12), command=plot_scatter).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Bar Plot", font=("Arial", 12), command=plot_bar).grid(row=0, column=2, padx=10)

# Start with line plot
plot_line()

root.mainloop()
