import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create a small dataset
data = {'Size': [1500, 1600, 1700, 1800, 1900, 2000, 2100],
        'Price': [250000, 270000, 290000, 310000, 330000, 350000, 370000]}
df = pd.DataFrame(data)

# Display the dataset
print(df)
X = df[['Size']]
y = df['Price']
# Create a LinearRegression object
model = LinearRegression()

# Fit the model
model.fit(X, y)

coefficient = model.coef_[0]
intercept = model.intercept_
print(f"Coefficient (Slope): {coefficient}")
print(f"Intercept: {intercept}")
# Plot data points
plt.scatter(X, y, color='blue', label='Data Points')

# Plot regression line
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')

plt.xlabel('Size Of House  (sq ft)')
plt.ylabel('Price Of House (USD)')
plt.title('Simple Linear Regression: House Size vs House Price')
plt.legend()
plt.show()
