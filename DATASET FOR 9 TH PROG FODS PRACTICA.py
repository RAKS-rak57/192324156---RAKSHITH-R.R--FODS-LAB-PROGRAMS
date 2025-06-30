import pandas as pd

data = {
    'PropertyID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'Location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai', 'Delhi'],
    'Bedrooms': [3, 5, 4, 6, 2, 5],
    'AreaSqFt': [1500, 2200, 1800, 3000, 1200, 2800],
    'ListingPrice': [7500000, 12500000, 8200000, 15000000, 6000000, 14000000]
}

df = pd.DataFrame(data)
df.to_csv('property_data.csv', index=False)
print("Sample dataset saved as 'property_data.csv'")
