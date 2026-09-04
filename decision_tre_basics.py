# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import graphviz
from sklearn import tree

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=0)

# Train the model
clf.fit(X, y)

# Output the accuracy score
accuracy = clf.score(X, y)
print(f"Accuracy of the model: {accuracy:.2f}")

# Print out the tree in textual form
text_representation = tree.export_text(clf, feature_names=iris.feature_names)
print(text_representation)


# Create a visual plot using graphviz
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=iris.feature_names,  
                                class_names=iris.target_names,
                                filled=True, rounded=True,  
                                special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("iris_tree") 
graph.view()

# Extract feature importances
feature_importances = clf.feature_importances_
for feature, importance in zip(iris.feature_names, feature_importances):
    print(f"Feature: {feature}, Importance: {importance:.2f}")

