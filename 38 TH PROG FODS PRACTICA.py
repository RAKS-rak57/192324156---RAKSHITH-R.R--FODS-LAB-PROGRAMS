import pandas as pd
import numpy as np

# Sample dataset: Simulate daily temperatures for 3 cities over 365 days
np.random.seed(42)
days = pd.date_range(start='2024-01-01', periods=365)

data = {
    'Date': np.tile(days, 3),
    'City': ['CityA'] * 365 + ['CityB'] * 365 + ['CityC'] * 365,
    'Temperature': np.concatenate([
        np.random.normal(loc=25, scale=3, size=365),  # CityA
        np.random.normal(loc=30, scale=7, size=365),  # CityB
        np.random.normal(loc=20, scale=2, size=365)   # CityC
    ])
}

df = pd.DataFrame(data)

# Group by city and calculate statistics
grouped = df.groupby('City')['Temperature']
mean_temp = grouped.mean()
std_temp = grouped.std()
temp_range = grouped.max() - grouped.min()

# Identify cities based on criteria
city_highest_range = temp_range.idxmax()
city_most_consistent = std_temp.idxmin()

# Display results
print("📊 Temperature Variability Analysis:\n")
print("Mean Temperature (°C):")
print(mean_temp.round(2), "\n")

print("Standard Deviation (°C):")
print(std_temp.round(2), "\n")

print("Temperature Range (°C):")
print(temp_range.round(2), "\n")

print(f"🔥 City with Highest Temperature Range: {city_highest_range}")
print(f"❄️ City with Most Consistent Temperature: {city_most_consistent}")
