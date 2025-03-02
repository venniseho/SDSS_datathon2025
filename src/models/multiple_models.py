"""
Real Estate Price Prediction Comparison of Multiple Models

This script loads a cleaned real estate dataset, trains multiple models,
and evaluates its performance in predicting listing prices.

Steps:
1. Load the dataset from a CSV file.
2. Define features (independent variables) and target (dependent variable).
3. Split the data into training (80%) and testing (20%) sets.
4. Train multiple models on the training set.
5. Make predictions on the test set.
6. Evaluate the model's performance using R² Score and Mean Absolute Error (MAE).

Author: Vennise Ho
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load dataset
file_path = "../../data/cleaned_real_estate_data_numerical.csv"
df = pd.read_csv(file_path)

# Define features (independent variables) and target (dependent variable)
features = ["num_beds", "num_baths", "monthly_maintenance_fee", "size_group"]  # Features used for prediction
target = "listing_price"  # Target variable (house listing price)

# Split data into training (80%) and testing (20%) sets
X = df[features]  # Feature matrix (independent variables)
y = df[target]  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Neural network does not converge in max_iter iterations, so standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define models to test
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42),
    "LightGBM": LGBMRegressor(n_estimators=100, learning_rate=0.1, random_state=42, force_row_wise=True),
    "Neural Network": MLPRegressor(hidden_layer_sizes=(64, 64),  max_iter=2000, learning_rate_init=0.0005,
                                   activation='relu', solver='lbfgs',  random_state=42),
}

# Dictionary to store results
results = {}

# Train and evaluate each model
for name, model in models.items():
    model.fit(X_train, y_train)  # Train model
    y_pred = model.predict(X_test)  # Make predictions
    r2 = r2_score(y_test, y_pred)  # Compute R² Score
    mae = mean_absolute_error(y_test, y_pred)  # Compute MAE
    results[name] = {"R² Score": r2, "MAE": mae}  # Store results

# RESULTS
# Convert results to DataFrame for easy comparison
results_df = pd.DataFrame(results).T

# Print results
print("\nModel Performance Comparison:")
print(results_df)

# Plot results
plt.figure(figsize=(10, 5))
results_df.sort_values(by="R² Score", ascending=False, inplace=True)

# Plot R² Scores
plt.subplot(1, 2, 1)
results_df["R² Score"].plot(kind="bar", color="skyblue", title="R² Score Comparison")
plt.xticks(rotation=45)

# Plot Mean Absolute Error
plt.subplot(1, 2, 2)
results_df["MAE"].plot(kind="bar", color="orange", title="Mean Absolute Error (MAE)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
