import pandas as pd
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load dataset
df = pd.read_csv('order_data.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Analysis
orders_per_customer = df.groupby('CustomerID').size()
avg_quantity_per_product = df.groupby('Product')['Quantity'].mean()
earliest_date = df['OrderDate'].min()
latest_date = df['OrderDate'].max()

# GUI setup
root = tk.Tk()
root.title("Order Data Analyzer")
root.geometry("750x550")

tk.Label(root, text="Customer Order Summary", font=("Arial", 14)).pack(pady=10)

# Plotting total orders per customer
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(orders_per_customer.index, orders_per_customer.values, color='skyblue')
ax.set_title("Total Orders by Customer")
ax.set_ylabel("Number of Orders")
ax.set_xlabel("Customer ID")
ax.bar_label(ax.containers[0])
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Summary popup
def show_summary():
    summary = (
        "1. Total Orders by Customer:\n" +
        "\n".join(f"{cid}: {count}" for cid, count in orders_per_customer.items()) +
        "\n\n2. Average Quantity per Product:\n" +
        "\n".join(f"{prod}: {qty:.2f}" for prod, qty in avg_quantity_per_product.items()) +
        f"\n\n3. Earliest Order Date: {earliest_date.date()}\n"
        f"   Latest Order Date: {latest_date.date()}"
    )
    messagebox.showinfo("Order Summary", summary)

tk.Button(root, text="Show Summary", font=("Arial", 12), command=show_summary).pack(pady=15)

root.mainloop()
