import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Example dataset
data = {'study_hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'pass_fail': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]}

df = pd.DataFrame(data)

plt.scatter(df['study_hours'], df['pass_fail'], color='blue')
plt.xlabel('Study Hours')
plt.ylabel('Pass/Fail')
plt.title('Study Hours vs Pass/Fail')
plt.show()

X = df[['study_hours']]
y = df['pass_fail']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

coeff = model.coef_[0][0]
intercept = model.intercept_[0]
print(f"Coefficient: {coeff}")
print(f"Intercept: {intercept}")

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Plot the decision boundary
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, model.predict_proba(X_test)[:, 1], color='blue', linewidth=2)
plt.xlabel('Study Hours')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression Decision Boundary')
plt.show()
