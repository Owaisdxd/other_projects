import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

array = np.array([1, 2, 3, 4, 5])

print("NumPy array :", array)


data = {'Name': ['Alice', 'Bob'], 'Age': [24, 30]}

df = pd.DataFrame(data)

print("Pandas DataFrame:\n", df)

iris = load_iris()

print("Iris dataset, target names:", iris.target_names)


**You Should See Output**

NumPy array : [1 2 3 4 5]
Pandas DataFrame:
     Name  Age
0  Alice   24
1    Bob   30
Iris dataset, target names: ['setosa' 'versicolor' 'virginica']

