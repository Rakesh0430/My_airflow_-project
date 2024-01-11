# Model training script
# Train machine learning models using processed data

# Example:
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#processed_data_path = 'data/processed/processed_data.csv

output_model_path = 'data/trained_models/model.pkl'
input_path='data/raw/dataset2.csv'


processed_data = pd.read_csv(input_path)

# Assume 'target' is the target column
X = processed_data.drop('Target', axis=1)
y = processed_data['Target']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, output_model_path)
