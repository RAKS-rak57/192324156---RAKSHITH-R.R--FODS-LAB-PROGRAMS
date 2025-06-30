import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Sample dataset
data = {
    'Area': [1200, 1500, 1800, 2400, 3000, 3500],
    'Bedrooms': [2, 3, 3, 4, 4, 5],
    'Location': ['Chennai', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Price': [5000000, 7500000, 7200000, 9500000, 12000000, 11500000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Area', 'Bedrooms', 'Location']]
y = df['Price']

# Preprocessing: One-hot encode 'Location'
preprocessor = ColumnTransformer(
    transformers=[('loc', OneHotEncoder(), ['Location'])],
    remainder='passthrough'
)

# Pipeline: preprocessing + model
model = Pipeline([
    ('preprocess', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model
model.fit(X, y)

# User input
print("Enter details of the new house:")
area = float(input("Area (in sq.ft): "))
bedrooms = int(input("Number of bedrooms: "))
location = input("Location (Chennai/Mumbai/Delhi): ")

# Predict
new_house = pd.DataFrame([[area, bedrooms, location]], columns=['Area', 'Bedrooms', 'Location'])
predicted_price = model.predict(new_house)[0]

# Output
print(f"\n🏠 Predicted Price: ₹{predicted_price:,.0f}")
