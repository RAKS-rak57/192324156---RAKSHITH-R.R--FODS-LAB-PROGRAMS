import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load data
df = pd.read_csv('weather_data.csv')

# GUI setup
root = tk.Tk()
root.title("Weather Data Visualizer")
root.geometry("750x550")

tk.Label(root, text="Monthly Temperature & Rainfall", font=("Arial", 16)).pack(pady=10)

# Matplotlib figure
fig, ax = plt.subplots(figsize=(7, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Plot functions
def plot_temperature():
    ax.clear()
    ax.plot(df['Month'], df['Temperature'], marker='o', linestyle='-', color='tomato')
    ax.set_title("Line Plot - Monthly Temperature")
    ax.set_ylabel("Temperature (°C)")
    ax.set_xlabel("Month")
    ax.grid(True)
    canvas.draw()

def plot_rainfall():
    ax.clear()
    ax.scatter(df['Month'], df['Rainfall'], color='royalblue', s=100)
    ax.set_title("Scatter Plot - Monthly Rainfall")
    ax.set_ylabel("Rainfall (mm)")
    ax.set_xlabel("Month")
    ax.grid(True)
    canvas.draw()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Show Temperature Line Plot", font=("Arial", 12),
          command=plot_temperature).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Show Rainfall Scatter Plot", font=("Arial", 12),
          command=plot_rainfall).grid(row=0, column=1, padx=10)

# Start with temperature plot
plot_temperature()

root.mainloop()
