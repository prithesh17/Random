# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset from local file
insurance_data = pd.read_csv("insurance.csv")

# Convert categorical variables to numerical values
# Mapping 'sex' to numerical values
insurance_data['sex'] = insurance_data['sex'].apply({'male': 0, 'female': 1}.get)
# Mapping 'smoker' to numerical values
insurance_data['smoker'] = insurance_data['smoker'].apply({'yes': 0, 'no': 1}.get)
# Mapping 'region' to numerical values
insurance_data['region'] = insurance_data['region'].apply({'northwest': 1, 'southeast': 2, 'northeast': 3, 'southwest': 4}.get)

# Feature Selection
# Dropping 'charges' and 'sex' columns from features
X = insurance_data.drop(['charges','sex'], axis=1)
# Target variable
y = insurance_data['charges']

# Data Splitting
# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Model Training
# Creating an instance of Linear Regression model
insurance_model = LinearRegression()
# Training the model
insurance_model.fit(X_train, y_train)

# Prediction for New Customer
# Information about the new customer
new_customer_info = {'age': 50, 'bmi': 25, 'children': 2, 'smoker': 1, 'region': 1}
# Creating a DataFrame for the new customer
new_customer_df = pd.DataFrame([new_customer_info])

# Predict insurance cost for the new customer
# Making prediction using trained model
predicted_cost = insurance_model.predict(new_customer_df)
# Displaying the predicted insurance cost for the new customer
print("The medical insurance cost of the given customer is:", predicted_cost)
