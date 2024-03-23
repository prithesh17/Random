from sklearn.datasets import load_iris  # Import function to load Iris dataset
from sklearn.neighbors import KNeighborsClassifier  # Import K-Nearest Neighbors classifier
import numpy as np  # Import NumPy library for array operations
from sklearn.model_selection import train_test_split  # Import function for train-test splitting

# Load Iris dataset
iris_dataset = load_iris()

# Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
# Initialize K-Nearest Neighbors classifier with k=1
kn = KNeighborsClassifier(n_neighbors=1)

# Train the classifier on the training data
kn.fit(x_train, y_train)

# Make predictions and evaluate the model
for i in range(len(x_test)):
    x = x_test[i]  # Get a single test data point
    x_new = np.array([x])  # Reshape the test data point
    prediction = kn.predict(x_new)  # Make prediction using the trained classifier
    print(f"\n Actual: {y_test[i]} {iris_dataset['target_names'][y_test[i]]}, Predicted: {prediction} {iris_dataset['target_names'][prediction]}")

# Calculate and print test score (accuracy) of the model
print(f"\n TEST SCORE [Accuracy]: {kn.score(x_test, y_test).2f}\n")
