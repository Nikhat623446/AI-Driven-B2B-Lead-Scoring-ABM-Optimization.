# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LMpAoVNWesE88M6ZidJ4lBbtSk2u1qYF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the dataset
data = pd.read_csv('/content/advertising.csv')  # Replace with your dataset file

# Step 2: Data Understanding
print("First 5 rows of the data:")
print(data.head())
print("\nData Info:")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())

# Step 3: Data Cleaning
# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Drop rows with missing values (if any)
data = data.dropna()

# Check for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
if data.duplicated().sum() > 0:
    data = data.drop_duplicates()
# Step 4: Exploratory Data Analysis (EDA)

plt.figure(figsize=(10, 6))
# Assuming the column is named 'TV', 'Radio', or 'Newspaper'
# Replace 'TV' with the correct column name if needed
sns.scatterplot(data=data, x='TV', y='Sales')  # Changed column name to 'TV'
plt.title('Sales vs Advertising')
plt.xlabel('Advertising') # You may want to change xlabel as well
plt.ylabel('Sales')
plt.show()

# ... rest of your code ...
# Correlation matrix
correlation = data.corr()
print("\nCorrelation Matrix:")
print(correlation)

# Step 5: Feature Selection and Preparation
X = data[['TV']]  # Independent variable (replace with relevant column) # Independent variable (replace with relevant column)
y = data['Sales']  # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Model Building
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Model Evaluation
# Predict on test data
y_pred = model.predict(X_test)

# Model coefficients
print("\nModel Coefficients:")
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nModel Evaluation:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Step 8: Visualization of Results
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Sales')
plt.plot(X_test, y_pred, color='red', label='Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Advertising')
plt.ylabel('Sales')
plt.legend()
plt.show()