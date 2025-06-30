import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [12000, 15000, 13500, 16000, 17000, 15500,
              18000, 17500, 16500, 19000, 20000, 21000]
}

df = pd.DataFrame(data)
df.to_csv('monthly_sales.csv', index=False)
print("Dataset 'monthly_sales.csv' created.")
