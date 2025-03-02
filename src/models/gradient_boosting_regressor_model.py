"""
Real Estate Price Prediction using Gradient Boosting Regressor

This script loads a cleaned real estate dataset, trains a Gradient Boosting Regressor model,
and evaluates its performance in predicting listing prices.

Steps:
1. Load the dataset from a CSV file.
2. Define features (independent variables) and target (dependent variable).
3. Split the data into training (80%) and testing (20%) sets.
4. Train a Gradient Boosting Regressor model on the training set.
5. Make predictions on the test set.
6. Evaluate the model's performance using R² Score and Mean Absolute Error (MAE).

Author: Vennise Ho
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import joblib

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
file_path = os.path.join(project_root, "data", "cleaned_real_estate_data_numerical.csv")

# Load dataset
df = pd.read_csv(file_path)

# Define features (independent variables) and target (dependent variable)
features = ["num_beds", "num_baths", "monthly_maintenance_fee", "size_group"]  # Features used for prediction
target = "listing_price"  # Target variable (house listing price)

# Split data into training (80%) and testing (20%) sets
X = df[features]  # Feature matrix (independent variables)
y = df[target]  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Gradient Boosting Regressor
# - n_estimators: Number of boosting stages (trees)
# - learning_rate: Controls contribution of each tree to the final prediction
# - random_state: Ensures reproducibility of results
gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
gb_model.fit(X_train, y_train)  # Train the model on the training data

# Save the trained model
model_filename = "real_estate_model.pkl"
joblib.dump(gb_model, model_filename)

print(f"Model saved as {model_filename}")
