import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
from sklearn import tree

# Load the dataset
path = 'C:\\CBD\\All_cases.csv'
data = pd.read_csv(path, encoding='utf-8')

# Extract features and target
code = data['code']
colour = data['colour']
symptoms = data.drop(columns=['code', 'colour'])

# Define X and y for prediction
X = symptoms
y = colour  # We are predicting 'colour'

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to balance the training dataset
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Initialize RandomForestClassifier with class_weight parameter
rf_clf = RandomForestClassifier(random_state=42, class_weight='balanced')

# Train the model
rf_clf.fit(X_train_res, y_train_res)

# Predict on the test set
y_pred = rf_clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Extract a single tree from the forest
estimator = rf_clf.estimators_[0]

plt.figure(figsize=(15,10))
tree.plot_tree(estimator, feature_names=symptoms.columns, class_names=rf_clf.classes_, filled=True)
plt.show()
