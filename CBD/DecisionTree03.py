import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

# Load the dataset
path = 'C:\\CBD\\All_cases.csv'
data = pd.read_csv(path, encoding='utf-8')

# Extract features and target
code = data['code']
colour = data['colour']
symptoms = data.drop(columns=['code', 'colour'])

# Encode the target labels
label_encoder = LabelEncoder()
colour_encoded = label_encoder.fit_transform(colour)

# Define X and y for prediction
X = symptoms
y = colour_encoded  # Encoded target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to the training data
smote = SMOTE(random_state=42)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

# Initialize XGBClassifier
xgb_clf = XGBClassifier(random_state=42)

# Train the model
xgb_clf.fit(X_train_sm, y_train_sm)

# Predict on the test set
y_pred = xgb_clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))
