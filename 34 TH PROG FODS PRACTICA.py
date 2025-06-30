import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Sample dataset
data = {
    'Age': [45, 50, 38, 60, 55, 42, 36, 48, 52, 40],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female'],
    'BloodPressure': [130, 140, 120, 150, 135, 125, 118, 145, 138, 122],
    'Cholesterol': [220, 250, 200, 270, 240, 210, 190, 260, 230, 205],
    'Outcome': ['Good', 'Bad', 'Good', 'Bad', 'Bad', 'Good', 'Good', 'Bad', 'Bad', 'Good']
}

df = pd.DataFrame(data)

# Encode categorical variable
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Outcome'] = df['Outcome'].map({'Good': 1, 'Bad': 0})

# Features and target
X = df[['Age', 'Gender', 'BloodPressure', 'Cholesterol']]
y = df['Outcome']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Predict
y_pred = knn.predict(X_test_scaled)

# Evaluation
print("📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Bad", "Good"]))

print("🧾 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Show predictions
results = X_test.copy()
results['Actual'] = y_test.map({1: 'Good', 0: 'Bad'}).values
results['Predicted'] = pd.Series(y_pred).map({1: 'Good', 0: 'Bad'}).values
print("\n🔍 Test Set Predictions:")
print(results)
