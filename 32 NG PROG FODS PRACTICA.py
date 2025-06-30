import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Sample dataset: House Size (sqft) vs Price
data = {
    'HouseSize': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200],
    'Price': [300000, 340000, 400000, 460000, 500000, 540000, 600000, 660000, 700000, 740000]
}

df = pd.DataFrame(data)

# Bivariate analysis (scatter plot)
plt.figure(figsize=(8, 5))
plt.scatter(df['HouseSize'], df['Price'], color='teal')
plt.title("Bivariate Analysis: House Size vs Price")
plt.xlabel("House Size (sqft)")
plt.ylabel("Price (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Prepare data for regression
X = df[['HouseSize']]
y = df['Price']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output results
print(f"📈 Coefficient (slope): {model.coef_[0]:.2f}")
print(f"📊 Intercept: {model.intercept_:.2f}")
print(f"✅ R² Score: {r2:.3f}")
print(f"📉 Mean Squared Error: {mse:.2f}")

# Plot regression line
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='skyblue', label='Actual Data')
plt.plot(X, model.predict(X), color='darkorange', linewidth=2, label='Regression Line')
plt.title("Linear Regression: House Size vs Price")
plt.xlabel("House Size (sqft)")
plt.ylabel("Price (₹)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
