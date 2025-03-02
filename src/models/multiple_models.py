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
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler


def train_and_evaluate_models(file_path):
    """
    Trains multiple regression models and evaluates their performance on real estate price prediction.

    :param file_path: Path to the cleaned real estate dataset.
    :return: DataFrame containing model performance metrics.
    """
    # Load dataset
    df = pd.read_csv(file_path)

    # Define features and target
    features = ["num_beds", "num_baths", "monthly_maintenance_fee", "size_group"]
    target = "listing_price"

    # Split data
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features for Neural Network
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define models
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42),
        "LightGBM": LGBMRegressor(n_estimators=100, learning_rate=0.1, random_state=42, force_row_wise=True),
        "Neural Network": MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=2000, learning_rate_init=0.0005,
                                       activation='relu', solver='lbfgs', random_state=42),
    }

    # Train and evaluate models
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)  # Train model
        y_pred = model.predict(X_test)  # Make predictions
        r2 = r2_score(y_test, y_pred)  # Compute R² Score
        mae = mean_absolute_error(y_test, y_pred)  # Compute MAE
        results[name] = {"R² Score": r2, "MAE": mae}  # Store results

    return pd.DataFrame(results).T
