import pandas as pd

# Read in the data
banking_df = pd.read_csv('subscription_prediction.csv')

# Look at the first few observations in the dataset
print(banking_df.head())

# Identify the number of categorical and numerical features in the dataset
categorical_features = banking_df.select_dtypes(include=['object']).columns
numerical_features = banking_df.select_dtypes(include=['int64', 'float64']).columns
print(f'Number of categorical features: {len(categorical_features)}')
print(f'Number of numerical features: {len(numerical_features)}')

# Print out the number of features and observations
print(f'Number of features: {banking_df.shape[1]}')
print(f'Number of observations: {banking_df.shape[0]}')

# Calculate and print the number of missing values in each column
print(banking_df.isnull().sum())

# Calculate and print the number of customers who subscribed to the term deposit and the number of customers who didn't
print(banking_df['subscribed'].value_counts())

# Display the summary statistics for the dataset
print(banking_df.describe())
