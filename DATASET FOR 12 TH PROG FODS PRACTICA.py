import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [22.5, 24.0, 27.5, 30.0, 32.5, 34.0,
                    33.5, 33.0, 31.0, 28.0, 25.0, 23.0],
    'Rainfall': [12, 8, 15, 25, 60, 120,
                 180, 160, 90, 40, 20, 10]
}

df = pd.DataFrame(data)
df.to_csv('weather_data.csv', index=False)
print("Dataset 'weather_data.csv' created.")
