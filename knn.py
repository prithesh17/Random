from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(x_train,y_train)

for i in range(len(x_test)):
    x = x_test[i]
    x_new = np.array([x])
    prediction = kn.predict(x_new)
    print(f"\n Actual: {y_test[i]} {iris_dataset['target_names'][y_test[i]]}, Predicted: {prediction} {iris_dataset['target_names'][prediction]}")

print(f"\n TEST SCORE [Accuracy]: {kn.score(x_test, y_test):.2f}\n")
