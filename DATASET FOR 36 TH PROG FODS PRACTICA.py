import pandas as pd
import numpy as np

# Simulated closing prices for 30 trading days
np.random.seed(42)
closing_prices = np.round(np.random.normal(loc=150, scale=5, size=30), 2)

df = pd.DataFrame({'Date': pd.date_range(start='2024-01-01', periods=30, freq='B'),
                   'Close': closing_prices})

df.to_csv('stock_data.csv', index=False)
print("Sample dataset 'stock_data.csv' created.")
