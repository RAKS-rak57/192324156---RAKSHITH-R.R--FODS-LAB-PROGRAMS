import numpy as np
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample fuel efficiency data (MPG) for 6 car models
fuel_efficiency = np.array([25.0, 30.0, 22.5, 27.5, 31.0, 29.5])
model_names = [f"Model {i+1}" for i in range(len(fuel_efficiency))]

# GUI setup
root = tk.Tk()
root.title("Fuel Efficiency Analyzer")
root.geometry("750x550")

tk.Label(root, text="Select Two Car Models to Compare", font=("Arial", 14)).pack(pady=10)

# Dropdowns for model selection
selected1 = tk.StringVar(value=model_names[0])
selected2 = tk.StringVar(value=model_names[1])

frame = tk.Frame(root)
frame.pack()

tk.OptionMenu(frame, selected1, *model_names).grid(row=0, column=0, padx=10)
tk.OptionMenu(frame, selected2, *model_names).grid(row=0, column=1, padx=10)

# Plotting
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(model_names, fuel_efficiency, color='lightblue')
ax.set_ylabel("Fuel Efficiency (MPG)")
ax.set_title("Fuel Efficiency of Car Models")
ax.bar_label(ax.containers[0], fmt='%.1f')
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Button action
def show_summary():
    idx1 = model_names.index(selected1.get())
    idx2 = model_names.index(selected2.get())
    mpg1 = fuel_efficiency[idx1]
    mpg2 = fuel_efficiency[idx2]
    avg_eff = np.mean(fuel_efficiency)
    improvement = ((mpg2 - mpg1) / mpg1) * 100

    # Highlight selected bars
    for i, bar in enumerate(bars):
        bar.set_color('lightblue')
    bars[idx1].set_color('orange')
    bars[idx2].set_color('green')
    canvas.draw()

    summary = (
        f"Average Fuel Efficiency: {avg_eff:.2f} MPG\n\n"
        f"{selected1.get()}: {mpg1:.2f} MPG\n"
        f"{selected2.get()}: {mpg2:.2f} MPG\n\n"
        f"Percentage Improvement from {selected1.get()} to {selected2.get()}:\n"
        f"{improvement:.2f}%"
    )
    messagebox.showinfo("Fuel Efficiency Summary", summary)

tk.Button(root, text="Compare Models", font=("Arial", 12), command=show_summary).pack(pady=15)

root.mainloop()
