import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data from CSV
data = pd.read_csv('tennis.csv')

# Obtain Train data and Train output
X = data.drop(columns=['play','day'])  # Features
y = data['play']                        # Target variable

# Convert categorical data into numerical data
label_encoders = {}  # Dictionary to hold label encoders for each column
for column in X.columns:
    label_encoders[column] = LabelEncoder()
    X[column] = label_encoders[column].fit_transform(X[column])

# Convert target labels into numerical labels
label_encoder_play = LabelEncoder()
y = label_encoder_play.fit_transform(y)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Train the classifier
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Evaluate the classifier
print("Now the Train data is :\n", X.head())  # Displaying first few rows of the transformed features
print("\nNow the Train output is\n", y)        # Displaying the transformed target variable
print("Accuracy is:", accuracy_score(classifier.predict(X_test), y_test))  # Evaluating accuracy
