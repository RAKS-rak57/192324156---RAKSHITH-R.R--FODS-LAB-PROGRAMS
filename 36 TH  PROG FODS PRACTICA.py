import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load stock data
df = pd.read_csv('stock_data.csv', parse_dates=['Date'])

# Calculate daily returns
df['Daily Return'] = df['Close'].pct_change()

# Calculate standard deviation (volatility)
volatility = df['Daily Return'].std()
mean_return = df['Daily Return'].mean()

# Display insights
print("📈 Stock Price Variability Analysis")
print(f"Mean Daily Return     : {mean_return:.4f}")
print(f"Standard Deviation    : {volatility:.4f}")
print(f"Annualized Volatility : {volatility * np.sqrt(252):.4f}")

# Plot closing prices
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='teal')
plt.title("Stock Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot daily returns
plt.figure(figsize=(10, 5))
plt.hist(df['Daily Return'].dropna(), bins=20, color='coral', edgecolor='black')
plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
