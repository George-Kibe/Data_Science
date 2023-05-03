import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load breast cancer dataset
cancer_data = load_breast_cancer(as_frame=True)

# Create a DataFrame from the data and target attributes
cancer_df = cancer_data['data']
cancer_df['target'] = cancer_data['target']

# Explore the dataset
print(cancer_df.head()) # First few observations
print(cancer_df.shape) # Number of features and observations
print(cancer_df.isna().sum()) # Number of missing values in each column
print(cancer_df['target'].value_counts()) # Number of patients with benign and malignant tumors
print(cancer_df.describe()) # Summary statistics


import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

# Define the feature columns and target column
X = cancer_df.drop('target', axis=1)
y = cancer_df['target']

# Split the data into training and testing sets
# Since the data is split randomly, setting a random_state to a specific number allows us to reproduce the same results every time we run the code.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=417)


import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

X = cancer_df.drop(["target"], axis=1)
y = cancer_df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)
# Create an instance of LinearSVC
model = LinearSVC(penalty='l2', loss='squared_hinge', C=10,  max_iter=3500, random_state=417)

# Fit the model to the training data
model.fit(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(test_accuracy)





