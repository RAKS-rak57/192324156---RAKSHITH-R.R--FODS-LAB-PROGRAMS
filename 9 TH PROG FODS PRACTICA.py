import pandas as pd
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load dataset
df = pd.read_csv('property_data.csv')

# Analysis
avg_price_by_location = df.groupby('Location')['ListingPrice'].mean()
more_than_4_bedrooms = df[df['Bedrooms'] > 4].shape[0]
largest_area_row = df[df['AreaSqFt'] == df['AreaSqFt'].max()].iloc[0]

# GUI setup
root = tk.Tk()
root.title("Property Data Analyzer")
root.geometry("750x550")

tk.Label(root, text="Real Estate Summary", font=("Arial", 14)).pack(pady=10)

# Plotting average price by location
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(avg_price_by_location.index, avg_price_by_location.values, color='mediumseagreen')
ax.set_ylabel("Avg Listing Price (₹)")
ax.set_title("Average Listing Price by Location")
ax.bar_label(ax.containers[0], fmt='₹%.0f')
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Summary popup
def show_summary():
    summary = (
        "1. Average Listing Price by Location:\n" +
        "\n".join(f"{loc}: ₹{price:,.0f}" for loc, price in avg_price_by_location.items()) +
        f"\n\n2. Properties with >4 Bedrooms: {more_than_4_bedrooms}" +
        f"\n\n3. Property with Largest Area:\n"
        f"   ID: {largest_area_row['PropertyID']}\n"
        f"   Location: {largest_area_row['Location']}\n"
        f"   Area: {largest_area_row['AreaSqFt']} sq.ft\n"
        f"   Price: ₹{largest_area_row['ListingPrice']:,.0f}"
    )
    messagebox.showinfo("Property Summary", summary)

tk.Button(root, text="Show Summary", font=("Arial", 12), command=show_summary).pack(pady=15)

root.mainloop()
