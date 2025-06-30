import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Sample dataset
data = {
    'EngineSize': [1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 3.0, 3.2, 3.5, 4.0],
    'Horsepower': [85, 100, 120, 135, 150, 165, 200, 220, 240, 280],
    'FuelEfficiency': [18, 17, 16, 15, 14, 13, 12, 11, 10, 9],
    'Price': [500000, 600000, 700000, 800000, 900000, 1000000, 1200000, 1300000, 1400000, 1600000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['EngineSize', 'Horsepower', 'FuelEfficiency']]
y = df['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

# Output performance
print("📊 Model Performance:")
print(f"R² Score: {r2:.3f}")
print(f"Mean Absolute Error: ₹{mae:,.0f}")

# Feature importance
importance = pd.Series(model.coef_, index=X.columns)
print("\n🔍 Feature Influence on Price:")
print(importance.sort_values(ascending=False))

# Visualize actual vs predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, color='teal')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Price (₹)")
plt.ylabel("Predicted Price (₹)")
plt.title("Actual vs Predicted Car Prices")
plt.grid(True)
plt.tight_layout()
plt.show()
