import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import tree
import matplotlib.pyplot as plt


# Load the dataset
path = 'C:\\CBD\\All_cases.csv'
data = pd.read_csv(path, encoding='utf-8')

# Extract features and target
code = data['code']
colour = data['colour']
symptoms = data.drop(columns=['code', 'colour'])

# Define X and y for prediction
X = symptoms
y = colour  # Change to 'colour' if you want to predict 'colour'

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the decision tree model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

print('Classification Report:')
print(classification_report(y_test, y_pred))

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Visualize the decision tree
plt.figure(figsize=(15,10))
tree.plot_tree(clf, feature_names=symptoms.columns, class_names=clf.classes_, filled=True)
plt.show()