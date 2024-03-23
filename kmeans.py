import pandas as pd
import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Read Cleveland Heart Disease data
heartDisease = pd.read_csv('heart.csv')
heartDisease = heartDisease.replace('?', np.nan)

# Model Bayesian Network
model = BayesianNetwork([('age', 'trestbps'), ('age', 'fbs'),
                         ('sex', 'trestbps'), ('exang', 'trestbps'), ('trestbps', 'heartdisease'),
                         ('fbs', 'heartdisease'), ('heartdisease', 'restecg'),
                         ('heartdisease', 'thalach'), ('heartdisease', 'chol')])

# Learning CPDs using Maximum Likelihood Estimators
print('\n Learning CPD using Maximum likelihood estimators')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

# Inferencing with Bayesian Network
print('\n Inferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)

# Computing the Probability of HeartDisease given Age
print('\n 1. Probability of HeartDisease given Age=50')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 50})
print(q)

# Accessing specific values from the DiscreteFactor object
print("Probability of Heart Disease given Age=50:", q.values[1])

# Computing the Probability of HeartDisease given cholesterol
print('\n 2. Probability of HeartDisease given cholesterol=200')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'chol': 200})
print(q)

# Accessing specific values from the DiscreteFactor object
print("Probability of Heart Disease given cholesterol=200 (Heart Disease = 1):", q.values[1])
