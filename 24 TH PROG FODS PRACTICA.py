import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Sample dataset: [fever, cough, fatigue, headache]
# Labels: 0 = No condition, 1 = Has condition
X = np.array([
    [98.6, 0, 0, 0],
    [101.2, 1, 1, 1],
    [99.1, 1, 0, 0],
    [102.5, 1, 1, 1],
    [97.9, 0, 0, 0],
    [100.4, 1, 1, 0],
    [98.2, 0, 1, 0],
    [103.0, 1, 1, 1],
    [99.5, 1, 0, 1],
    [98.0, 0, 0, 1]
])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 1, 0])

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split (not strictly needed here, but good practice)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# User input
print("Enter new patient symptoms:")
fever = float(input("Fever (°F): "))
cough = int(input("Cough (0 = No, 1 = Yes): "))
fatigue = int(input("Fatigue (0 = No, 1 = Yes): "))
headache = int(input("Headache (0 = No, 1 = Yes): "))
k = int(input("Enter number of neighbors (k): "))

# Prepare input
new_patient = np.array([[fever, cough, fatigue, headache]])
new_patient_scaled = scaler.transform(new_patient)

# Train and predict
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)
prediction = model.predict(new_patient_scaled)

# Output
print("\nPrediction:")
print("🩺 Patient likely HAS the condition." if prediction[0] == 1 else "✅ Patient likely does NOT have the condition.")
