# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset from local file
insurance_data = pd.read_csv("insurance.csv")

# Convert categorical variables to numerical values
insurance_data['sex'] = insurance_data['sex'].apply({'male': 0, 'female': 1}.get)
insurance_data['smoker'] = insurance_data['smoker'].apply({'yes': 0, 'no': 1}.get)
insurance_data['region'] = insurance_data['region'].apply({'northwest': 1, 'southeast': 2, 'northeast': 3, 'southwest': 4}.get)

# Feature Selection
X = insurance_data.drop(['charges', 'sex'], axis=1)
y = insurance_data['charges']

# Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model Training
insurance_model = LinearRegression()
insurance_model.fit(X_train, y_train)

# Prediction for New Customer
new_customer_info = {'age': 50, 'bmi': 25, 'children': 2, 'smoker': 1, 'region': 2}
new_customer_df = pd.DataFrame([new_customer_info])

# Predict insurance cost for the new customer
predicted_cost = insurance_model.predict(new_customer_df)
print("The medical insurance cost of the given customer is:", predicted_cost[0])
