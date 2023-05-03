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


import pandas as pd

# Read in the dataset
banking_df = pd.read_csv("subscription_prediction.csv")

# Convert 'yes' and 'no' values in the target column to 1s and 0s
banking_df['y'] = banking_df['y'].map({'yes': 1, 'no': 0})

# Randomly sample 85% of the dataset for training
train_df = banking_df.sample(frac=0.85, random_state=417)

# Assign the remaining rows to test_df
test_df = banking_df.drop(train_df.index)

# Print the distribution of labels as percentages for both train and test datasets
print("Train data distribution:")
print(train_df['y'].value_counts(normalize=True) * 100)
print("\nTest data distribution:")
print(test_df['y'].value_counts(normalize=True) * 100)

# Separate feature columns and target column for training dataset
X_train = train_df.drop('y', axis=1)
y_train = train_df['y']

# Separate feature columns and target column for test dataset
X_test = test_df.drop('y', axis=1)
y_test = test_df['y']