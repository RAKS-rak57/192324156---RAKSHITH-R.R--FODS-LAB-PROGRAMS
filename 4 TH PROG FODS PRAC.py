import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Sales data
sales_data = np.array([15000, 18000, 21000, 25000])
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
colors = ['skyblue', 'lightgreen', 'orange', 'salmon']

# Calculate total and percentage increase
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

# Tkinter GUI setup
root = tk.Tk()
root.title("Quarterly Sales Growth")
root.geometry("600x500")

# Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(quarters, [0, 0, 0, 0], color=colors)
ax.set_ylim(0, max(sales_data) + 5000)
ax.set_ylabel("Sales Amount")
ax.set_title("Quarterly Sales Bar Graph")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Button click handlers
def show_bar(index):
    bars[index].set_height(sales_data[index])
    canvas.draw()

# Create buttons for each quarter
frame = tk.Frame(root)
frame.pack(pady=10)

for i in range(4):
    btn = tk.Button(frame, text=f"Show {quarters[i]}", width=12, 
                    command=lambda i=i: show_bar(i))
    btn.grid(row=0, column=i, padx=5)

# Display total and percentage increase
summary = f"Total Sales: ${total_sales}\nPercentage Increase (Q1 to Q4): {percentage_increase:.2f}%"
tk.Label(root, text=summary, font=("Arial", 12), pady=10).pack()

root.mainloop()
