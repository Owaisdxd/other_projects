from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['target'] = iris_data.target
#print(df.head())
# Define features and target
X = df.drop('target', axis=1)
print(f"Value of X is >> {X}")
y = df['target']
print(f"Value of y is >> {y}")
# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")
model = LogisticRegression(max_iter=200)
# Perform 5-fold cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean()}")
model.fit(X_train, y_train)
# Evaluate on the test set
test_score = model.score(X_test, y_test)
print(f"Test score (train-test split): {test_score}")

