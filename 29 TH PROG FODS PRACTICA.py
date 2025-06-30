import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Sample dataset
data = {
    'Age': [25, 32, 47, 51, 62, 23, 34, 45, 52, 48],
    'Salary': [50000, 60000, 80000, 82000, 90000, 45000, 52000, 75000, 88000, 79000],
    'Purchased': [0, 1, 1, 1, 1, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)

# Show available columns
print("Available columns:", list(df.columns))

# User input
features_input = input("Enter feature column names (comma-separated): ")
target_input = input("Enter target column name: ")

# Parse input
feature_cols = [col.strip() for col in features_input.split(',')]
target_col = target_input.strip()

# Split data
X = df[feature_cols]
y = df[target_col]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

# Output
print("\n📊 Model Evaluation Metrics:")
print(f"Accuracy  : {acc:.2f}")
print(f"Precision : {prec:.2f}")
print(f"Recall    : {rec:.2f}")
print(f"F1 Score  : {f1:.2f}")
