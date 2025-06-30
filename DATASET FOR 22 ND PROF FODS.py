import pandas as pd

data = {
    'Date': ['2023-01-05', '2023-01-15', '2023-02-10', '2023-02-20',
             '2023-03-12', '2023-03-25', '2023-04-08', '2023-04-22',
             '2023-05-05', '2023-05-18', '2023-06-09', '2023-06-21'],
    'Temperature': [14.2, 15.1, 16.5, 17.0, 20.3, 21.1, 25.0, 24.5, 28.2, 29.0, 31.5, 32.1]
}

df = pd.DataFrame(data)
df.to_csv('temperature_data.csv', index=False)
print("CSV file 'temperature_data.csv' created successfully.")
