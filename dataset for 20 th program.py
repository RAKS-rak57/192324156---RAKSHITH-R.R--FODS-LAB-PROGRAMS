import pandas as pd

# Generate sample customer data
data = {
    'Customer ID': range(1001, 1021),
    'Age': [25, 34, 45, 23, 40, 36, 50, 29, 31, 42, 60, 27, 37, 48, 22, 55, 32, 39, 41, 26],
    'Total Spending': [500, 1200, 750, 300, 950, 1100, 680, 400, 1050, 890, 1500, 460, 1250, 770, 280, 1400, 620, 980, 890, 340]
}

df = pd.DataFrame(data)
df.to_csv('customer_data.csv', index=False)

print(df)
