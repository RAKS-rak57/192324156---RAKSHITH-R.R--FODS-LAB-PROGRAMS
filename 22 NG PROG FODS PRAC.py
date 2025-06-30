import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Load and process data
df = pd.read_csv('temperature_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Month')['Temperature'].mean().reset_index()
monthly_avg['Month'] = monthly_avg['Month'].dt.to_timestamp()

# GUI setup
root = tk.Tk()
root.title("Monthly Temperature Viewer")
root.geometry("700x600")

# Matplotlib figure
fig, ax = plt.subplots(figsize=(7, 4))
line, = ax.plot(monthly_avg['Month'], monthly_avg['Temperature'], marker='o', color='teal')
ax.set_title("Average Monthly Temperature")
ax.set_xlabel("Month")
ax.set_ylabel("Temperature (°C)")
fig.autofmt_xdate()

# Tooltip annotation
annot = ax.annotate("", xy=(0,0), xytext=(15,15), textcoords="offset points",
                    bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.8),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

# Hover function
def update_annot(ind):
    x, y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    date_str = pd.to_datetime(x[ind["ind"][0]]).strftime('%B %Y')
    annot.set_text(f"{date_str}\n{y[ind['ind'][0]]:.2f} °C")

def on_hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = line.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        elif vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", on_hover)

# Embed plot in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Month buttons
frame = tk.Frame(root)
frame.pack(pady=10)

def show_month(index):
    month = monthly_avg['Month'][index].strftime('%B %Y')
    temp = monthly_avg['Temperature'][index]
    tk.messagebox.showinfo("Monthly Average", f"{month}: {temp:.2f}°C")

for i, row in monthly_avg.iterrows():
    btn = tk.Button(frame, text=row['Month'].strftime('%b'), width=8,
                    command=lambda i=i: show_month(i))
    btn.grid(row=0, column=i, padx=5)

root.mainloop()
