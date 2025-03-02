# 🏠 Real Estate Price Prediction

## 📖 Table of Contents
1. [Overview](#-overview)
2. [Installation](#-installation)
3. [Running the Web App](#-running-the-web-app)
4. [Code Structure](#-code-structure)
5. [Datasets](#-datasets)
6. [Model Performance Evaluation](#-model-performance-evaluation)
7. [Model Tuning & Improvements](#-model-tuning--improvements)
8. [Best Model & Next Steps](#-best-model--next-steps)
9. [Open Source & Licensing](#-open-source--licensing)
10. [Contributors](#-contributors)
11. [AI Assistance](#-ai-assistance)
12. [License](#-license)

## 📖 Overview
This project builds a **real estate price prediction web application** using a pre-trained machine learning model. The goal is to provide an interactive tool for users to estimate property listing prices based on features such as:
- Number of bedrooms
- Number of bathrooms
- Maintenance fees
- Property size category
- Distance to the nearest subway station (Toronto Transit Commission - TTC)

## 📦 Installation
Before running the project, install the required dependencies:

```bash
pip install -r requirements.txt
```

### If you're using a virtual environment:
#### 🔹 Windows
1. Open **Command Prompt (cmd)**
2. Run the following commands:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

#### 🔹 macOS/Linux
1. Open **Terminal**
2. Run the following commands:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
  If you encounter issues with XGBoost, install `libomp`:
  ```bash
  brew install libomp
  pip install xgboost
  ```

## 🚀 Running the Web App
The real estate price prediction tool is available as a **web application** using **Streamlit**.  
To launch the app, run:

```bash
streamlit run src/real_estate_dashboard.py
```

This will open a web browser where you can:
- Input property details (e.g., bedrooms, bathrooms, size group, subway proximity).
- Get **price predictions** using the **pre-trained model**.
- View model evaluation results.

## 📂 Code Structure
This project consists of three main components:

1. **Data Processing (`src/data_processing/`)**
   - Scripts responsible for cleaning and transforming raw real estate data.
   - Integrates geospatial data (TTC subway distances) to enhance the dataset.

2. **Model Training & Evaluation (`src/models/`)**
   - Code to train multiple regression models and compare their performance.
   - Saves the best pre-trained model for deployment.

3. **Visualization & Web App (`src/visualizations/` and `src/`)**
   - Code for generating exploratory data analysis and model performance visualizations.
   - The **Streamlit web application** is in `src/toronto_property_price_prediction_web_app.py` and serves as the user interface.

## 📂 Datasets
This project includes two datasets:
1. **Base Real Estate Data:** `cleaned_real_estate_data_numerical.csv`
   - This dataset was provided by the **SDSS Datathon 2025** and contains general real estate features such as bedrooms, bathrooms, maintenance fees, and property size category.
2. **Enhanced Real Estate Data:** `real_estate_data_with_subway_distance.csv`
   - Includes all base dataset features plus `subway_distance`, which represents the distance to the nearest TTC subway station (in meters).

**Data Sources:**
- **Real Estate Data:** Provided by the [SDSS Datathon 2025](https://sdss.datathon2025.org)
- **Geospatial Data:** [Toronto Transit Commission (TTC) Subway Stations](https://mdl.library.utoronto.ca/collections/geospatial-data/toronto-transit-commission-ttc)

**Features:**
  - `num_beds` → Number of bedrooms
  - `num_baths` → Number of bathrooms
  - `monthly_maintenance_fee` → Monthly maintenance cost (in $)
  - `size_group` → Property size category (e.g., small, medium, large)
  - `subway_distance` → Distance to the nearest TTC subway station (available in enhanced dataset)
- **Target Variable:** `listing_price` → The price of the property

## 📊 Model Performance Evaluation
| Model               | R² Score | MAE ($) |
|---------------------|---------|---------|
| **Gradient Boosting**  | 0.9229  | 106,186  |
| **Neural Network**    | 0.9209  | 112,586  |
| **Linear Regression**  | 0.9169  | 113,061  |
| **LightGBM**          | 0.9137  | 109,008  |
| **XGBoost**           | 0.9113  | 111,094  |
| **Random Forest**      | 0.9040  | 119,793  |

## 🔧 Model Tuning & Improvements
- **Feature Engineering:** Add `price per sqft`, `location`, or `year_built` for better accuracy.
- **Hyperparameter Tuning:** Use `GridSearchCV` or `RandomizedSearchCV` to optimize model parameters.
- **Geospatial Data Integration:** Include distance to TTC subway stations for location-based price adjustments.
- **Deployment:** The pre-trained model is stored and used directly for predictions.

## 🏆 Best Model & Next Steps
✅ The **best model** based on performance is **Gradient Boosting**.  
📌 Future work includes **improving model generalization** and enhancing the **web app UI**.

## 📜 Open Source & Licensing
This project uses the following open-source models and libraries:
- **Scikit-learn** (BSD-3 License) – Linear Regression, Random Forest, Gradient Boosting, MLPRegressor.
- **XGBoost** (Apache 2.0 License) – XGBoostRegressor.
- **LightGBM** (MIT License) – LightGBMRegressor.

For full licensing details, refer to the respective repositories:
- [Scikit-learn License](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING)
- [XGBoost License](https://github.com/dmlc/xgboost/blob/master/LICENSE)
- [LightGBM License](https://github.com/microsoft/LightGBM/blob/master/LICENSE.txt)

## 👥 Contributors
This project was created by:
- **Vennise Ho**
- **Lillian Toe**
- **Duncan Wan**
- **Oceane Yembiline**

## 🤖 AI Assistance
This project was developed with guidance from **ChatGPT (OpenAI)**.

## 📜 License
📄 MIT License

© 2024 Vennise Ho
