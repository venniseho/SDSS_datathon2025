# 🏠 Real Estate Price Prediction

## 📖 Overview
This project builds a **real estate price prediction model** using various machine learning algorithms. The goal is to estimate property listing prices based on features like the number of bedrooms, bathrooms, maintenance fees, and size category.

## 📂 Datasets
- **File:** `cleaned_real_estate_data_numerical.csv`
- **Features:**
  - `num_beds` → Number of bedrooms
  - `num_baths` → Number of bathrooms
  - `monthly_maintenance_fee` → Monthly maintenance cost (in $)
  - `size_group` → Property size category (e.g., small, medium, large)
- **Target Variable:** `listing_price` → The price of the property

## 📦 Installation
Before running the project, install the required dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib lightgbm xgboost
```

If using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

## 🚀 Running the Model
1. **Load the dataset**:  
   The script reads `cleaned_real_estate_data_numerical.csv` into a Pandas DataFrame.
   
2. **Train multiple models**:  
   - Linear Regression
   - Random Forest Regressor
   - Gradient Boosting Regressor
   - XGBoost Regressor
   - LightGBM Regressor
   - Neural Network (MLPRegressor)
   
3. **Evaluate performance**:  
   The script compares models based on:
   - **R² Score** (higher is better)
   - **Mean Absolute Error (MAE)** (lower is better)
   
4. **View results**:  
   The best model is selected based on performance metrics.

To execute the script, run:

```bash
python real_estate_model.py
```

## 📊 Model Comparison Example
| Model               | R² Score | MAE ($) |
|---------------------|---------|---------|
| Linear Regression  | 0.72    | 45,000  |
| Random Forest      | 0.85    | 30,000  |
| Gradient Boosting  | 0.88    | 28,000  |
| XGBoost           | 0.89    | 27,500  |
| LightGBM          | 0.87    | 29,000  |
| Neural Network    | 0.75    | 40,000  |

## 🔧 Model Tuning & Improvements
- **Feature Engineering:** Add `price per sqft`, `location`, or `year_built` for better accuracy.
- **Hyperparameter Tuning:** Use `GridSearchCV` or `RandomizedSearchCV` to optimize model parameters.
- **Deployment:** Save the best model using `joblib` and integrate it into a Flask or FastAPI app.

## 🏆 Best Model & Next Steps
- The **best model** is typically **XGBoost** or **Gradient Boosting**, based on accuracy.
- Future work includes **hyperparameter tuning** and deploying the model as a **web app**.

## 👥 Contributors
This project was created by:
- Vennise Ho
- Lillian Toe
- Duncan Wan
- Oceane Yembiline

Feel free to contribute to this project! If you have any suggestions, open an issue or submit a pull request.

## 🤖 AI Assistance
This project was developed with guidance from **ChatGPT (OpenAI)**.

## 📜 License
MIT License

Copyright (c) [2024] [Vennise Ho]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN
