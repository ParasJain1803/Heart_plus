# train_model.py

# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Load dataset
data = pd.read_csv('heart_disease.csv')

# Check the column names to verify the target column
print(data.columns)

# Replace 'target' with the actual name of your target column (e.g., 'outcome', 'disease', etc.)
# Assuming 'outcome' is the column name for this example:
target_column = 'outcome'

# Encode categorical columns (like 'sex', 'chest_pain', 'thal')
# Example for 'sex' column (assuming 'sex' has 'Male' and 'Female')
if 'sex' in data.columns:
    data['sex'] = data['sex'].apply(lambda x: 1 if x == 'Male' else 0)

# Encode any other categorical columns
# Use LabelEncoder for categorical columns that have more than two categories
labelencoder = LabelEncoder()
for column in data.select_dtypes(include=['object']).columns:
    data[column] = labelencoder.fit_transform(data[column])

# Features and labels
X = data.drop(target_column, axis=1)
y = data[target_column]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model training: Using RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model and scaler using pickle
with open('heart_disease_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
