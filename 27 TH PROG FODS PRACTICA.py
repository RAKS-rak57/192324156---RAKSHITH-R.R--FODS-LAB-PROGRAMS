import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Sample dataset: [usage_minutes, contract_duration_months, support_calls]
data = {
    'UsageMinutes': [300, 120, 450, 200, 600, 100, 350, 400, 250, 150],
    'ContractMonths': [12, 1, 24, 6, 36, 1, 18, 24, 6, 3],
    'SupportCalls': [1, 5, 0, 3, 0, 6, 2, 1, 4, 5],
    'Churn': [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[['UsageMinutes', 'ContractMonths', 'SupportCalls']]
y = df['Churn']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_scaled, y)

# User input
print("Enter new customer details:")
usage = float(input("Usage minutes per month: "))
contract = int(input("Contract duration (months): "))
calls = int(input("Number of support calls: "))

# Prepare and scale input
new_customer = pd.DataFrame([[usage, contract, calls]], columns=X.columns)
new_scaled = scaler.transform(new_customer)

# Predict
prediction = model.predict(new_scaled)[0]
prob = model.predict_proba(new_scaled)[0][1]

# Output
print("\n📊 Prediction:")
print("🔁 Customer is likely to CHURN." if prediction == 1 else "✅ Customer is likely to STAY.")
print(f"Probability of churn: {prob:.2%}")
