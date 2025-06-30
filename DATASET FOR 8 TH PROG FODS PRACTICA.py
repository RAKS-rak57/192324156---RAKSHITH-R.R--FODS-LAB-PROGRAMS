import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Mouse', 'Laptop', 'Monitor'],
    'Quantity': [2, 5, 3, 1, 4, 2, 2, 3, 1, 1]
}

df = pd.DataFrame(data)
df.to_csv('monthly_sales.csv', index=False)
print("Sample dataset saved as 'monthly_sales.csv'")
