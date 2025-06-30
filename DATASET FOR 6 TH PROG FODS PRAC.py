import pandas as pd

data = {
    'Customer Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Items': [['Milk', 'Bread'], ['Eggs', 'Juice'], ['Rice', 'Oil'], ['Fruits', 'Snacks']],
    'Prices': [[40, 30], [60, 80], [100, 120], [50, 70]],
    'Quantities': [[2, 1], [1, 2], [3, 2], [2, 3]],
    'Discount (%)': [10, 5, 15, 8],
    'Tax (%)': [5, 5, 5, 5]
}

df = pd.DataFrame(data)
df.to_csv('customer_purchases.csv', index=False)
print("Sample dataset saved as 'customer_purchases.csv'")
