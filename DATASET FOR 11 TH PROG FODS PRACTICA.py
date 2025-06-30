import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [12000, 13500, 15000, 16000, 17000, 18000]
}

df = pd.DataFrame(data)
df.to_csv('sales_over_time.csv', index=False)
print("Dataset 'sales_over_time.csv' created.")
