from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Train the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# User input
print("Enter measurements of the new Iris flower:")
sepal_length = float(input("Sepal length (cm): "))
sepal_width = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))
petal_width = float(input("Petal width (cm): "))

# Prepare input and predict
new_sample = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(new_sample)

# Output result
print(f"\n🌸 Predicted Iris species: {target_names[prediction[0]].capitalize()}")
