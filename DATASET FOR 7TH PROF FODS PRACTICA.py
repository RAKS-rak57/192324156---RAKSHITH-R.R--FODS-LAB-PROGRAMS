import pandas as pd

data = {
    'CustomerID': ['C001', 'C002', 'C001', 'C003', 'C002', 'C004', 'C001', 'C003'],
    'OrderDate': ['2023-01-10', '2023-01-12', '2023-02-05', '2023-02-20',
                  '2023-03-15', '2023-03-18', '2023-04-01', '2023-04-10'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Keyboard', 'Mouse', 'Mouse', 'Laptop'],
    'Quantity': [1, 2, 1, 1, 3, 2, 1, 2]
}

df = pd.DataFrame(data)
df.to_csv('order_data.csv', index=False)
print("Sample dataset saved as 'order_data.csv'")
