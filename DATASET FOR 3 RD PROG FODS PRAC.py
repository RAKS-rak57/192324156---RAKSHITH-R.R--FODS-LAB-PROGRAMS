import pandas as pd

# Sample housing data: [Bedrooms, Square Footage, Sale Price]
data = {
    'Bedrooms': [3, 5, 4, 6, 2, 5, 3, 7],
    'SquareFootage': [1500, 3000, 2000, 4000, 1200, 2800, 1600, 3500],
    'SalePrice': [250000, 450000, 350000, 550000, 200000, 430000, 260000, 600000]
}

df = pd.DataFrame(data)
df.to_csv('house_data.csv', index=False)
print("CSV file 'house_data.csv' created successfully.")
