import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('customer_purchases.csv')
df['Items'] = df['Items'].apply(eval)
df['Prices'] = df['Prices'].apply(eval)
df['Quantities'] = df['Quantities'].apply(eval)

# GUI setup
root = tk.Tk()
root.title("Customer Billing Interface")
root.geometry("600x500")

tk.Label(root, text="Select a Customer", font=("Arial", 14)).pack(pady=10)

# Dropdown for customer selection
selected = tk.StringVar()
selected.set(df['Customer Name'][0])
dropdown = tk.OptionMenu(root, selected, *df['Customer Name'])
dropdown.pack()

# Display details and calculate total
def show_details():
    name = selected.get()
    row = df[df['Customer Name'] == name].iloc[0]
    items, prices, qtys = row['Items'], row['Prices'], row['Quantities']
    discount, tax = row['Discount (%)'], row['Tax (%)']

    subtotal = sum(p * q for p, q in zip(prices, qtys))
    discounted = subtotal * (1 - discount / 100)
    total = discounted * (1 + tax / 100)

    details = f"Customer: {name}\n\nItems Purchased:\n"
    for i in range(len(items)):
        details += f"  {items[i]} - ₹{prices[i]} x {qtys[i]}\n"
    details += f"\nSubtotal: ₹{subtotal:.2f}\nDiscount: {discount}%\nTax: {tax}%\nTotal: ₹{total:.2f}"

    messagebox.showinfo("Customer Bill", details)

tk.Button(root, text="Show Bill", font=("Arial", 12), command=show_details).pack(pady=10)

# Visualization: Regularity based on quantity and discount
def show_chart():
    # Calculate positive regularity score
    regular_score = df['Quantities'].apply(lambda q: sum(q)) - df['Discount (%)']
    regular_score = regular_score.abs()  # Convert all values to positive

    # Plot chart with normal upward bars
    plt.figure(figsize=(8, 5))
    plt.bar(df['Customer Name'], regular_score, color='skyblue')
    plt.ylim(0, regular_score.max() + 2)
    plt.title("Customer Regularity Score (|Quantity - Discount|)")
    plt.ylabel("Score")
    plt.xlabel("Customer")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


tk.Button(root, text="Show Regularity Chart", font=("Arial", 12), command=show_chart).pack(pady=10)

root.mainloop()
5
