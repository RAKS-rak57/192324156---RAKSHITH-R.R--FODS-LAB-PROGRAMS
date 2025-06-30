import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor, _tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Sample dataset
data = {
    'Mileage': [15000, 30000, 45000, 60000, 75000, 90000],
    'Age': [1, 2, 3, 4, 5, 6],
    'Brand': ['Toyota', 'Honda', 'Ford', 'Toyota', 'Ford', 'Honda'],
    'EngineType': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel'],
    'Price': [850000, 750000, 650000, 600000, 550000, 500000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Mileage', 'Age', 'Brand', 'EngineType']]
y = df['Price']

# Preprocessing: One-hot encode categorical features
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(), ['Brand', 'EngineType'])],
    remainder='passthrough'
)

# CART model pipeline
model = Pipeline([
    ('preprocess', preprocessor),
    ('regressor', DecisionTreeRegressor(random_state=42))
])

# Train the model
model.fit(X, y)

# User input
print("Enter details of the car to predict its price:")
mileage = float(input("Mileage (in km): "))
age = int(input("Age (in years): "))
brand = input("Brand (Toyota/Honda/Ford): ")
engine = input("Engine Type (Petrol/Diesel): ")

# Prepare input
new_car = pd.DataFrame([[mileage, age, brand, engine]], columns=['Mileage', 'Age', 'Brand', 'EngineType'])
predicted_price = model.predict(new_car)[0]

# Output prediction
print(f"\n🚗 Predicted Price: ₹{predicted_price:,.0f}")

# Extract decision path
tree = model.named_steps['regressor']
encoder = model.named_steps['preprocess'].named_transformers_['cat']
feature_names = list(encoder.get_feature_names_out(['Brand', 'EngineType'])) + ['Mileage', 'Age']
sample_transformed = model.named_steps['preprocess'].transform(new_car)
node_indicator = tree.decision_path(sample_transformed)
leaf_id = tree.apply(sample_transformed)

print("\n🧭 Decision Path:")
for node_id in node_indicator.indices:
    if leaf_id[0] == node_id:
        continue
    threshold = tree.tree_.threshold[node_id]
    feature = feature_names[tree.tree_.feature[node_id]]
    value = sample_transformed[0, tree.tree_.feature[node_id]]
    direction = "≤" if value <= threshold else ">"
    print(f"• {feature} {direction} {threshold:.2f}")
