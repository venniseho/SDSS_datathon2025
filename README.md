# 🏠 Toronto Property Price Prediction Web App

## 📖 Table of Contents
1. [Overview](#-overview)
2. [Installation](#-installation)
3. [Running the Web App](#-running-the-web-app)
4. [Code Structure](#-code-structure)
5. [Datasets](#-datasets)
6. [Model Performance Evaluation](#-model-performance-evaluation)
7. [Model Tuning & Improvements](#-model-tuning--improvements)
8. [Next Steps](#-next-steps)
9. [Open Source & Licensing](#-open-source--licensing)
10. [Troubleshooting](#-troubleshooting)
11. [Contributors](#-contributors)
12. [AI Assistance](#-ai-assistance)
13. [License](#-license)

## 📖 Overview
This project builds a **real estate price prediction web application** using a pre-trained machine learning model. The goal is to provide an interactive tool for users to estimate property listing prices based on the following features:
- Number of bedrooms
- Number of bathrooms
- Maintenance fees
- Property size 

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
streamlit run src/toronto_property_price_prediction_web_app.py
```
To close the web app CTRL + C while the tab is still open.

This will open a web browser where you can:
- Input property details (e.g., bedrooms, bathrooms, size group).
- Get **price predictions** using the **pre-trained model**.
- View model evaluation results.

## 📂 Code Structure
This project consists of three main components:

1. **Data Processing (`src/data_processing/`)**
   - Scripts responsible for cleaning and transforming raw real estate data. (Availabe to run with the command: ```python src/data_processing/data_cleaning_full_numerical.py```)
   - Integrates geospatial data (TTC subway distances) to enhance the dataset. (Availabe to run with the command: ```python src/data_processing/subway_distance_data_cleaning.py```)

2. **Model Training & Evaluation (`src/models/`)**
   - Code to train multiple regression models and compare their performance.
   - Saves the best pre-trained model for deployment.

3. **Visualization & Web App (`src/visualizations/` and `src/`)**
   - Code for generating exploratory data analysis and model performance visualizations. (Availabe to run with the command: ```python src/visualization/[visualization file name]```
        - Already generated visualization images are in the folder ```src/visualization/visualization_images```
   - The **Streamlit web application** is in ```src/toronto_property_price_prediction_web_app.py``` and serves as the user interface.

## 📂 Datasets
This project includes two datasets:
1. **Base Real Estate Data:** `cleaned_real_estate_data_numerical.csv`
   - Contains general real estate features such as price, number of bedrooms, size, ward, and days on market
2. **Enhanced Real Estate Data:** `real_estate_data_with_subway_distance.csv`
   - Includes all base dataset features plus `subway_distance`, which represents the distance to the nearest TTC subway station.

**Data Sources:**
- **Real Estate Data:** Provided by the [SDSS Datathon 2025](https://sdss.datathon2025.org)
- **Geospatial Data:** [Toronto Transit Commission (TTC) Subway Stations](https://mdl.library.utoronto.ca/collections/geospatial-data/toronto-transit-commission-ttc)

**Features:**
  - `num_beds` → Number of bedrooms
  - `num_baths` → Number of bathrooms
  - `monthly_maintenance_fee` → Monthly maintenance cost (in $)
  - `size_group` → Property size category (e.g., small, medium, large)
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

✅ The **best model** based on performance is **Gradient Boosting**.  

This information is found in: ```src/visualization/visualization_images/model_evaluation_scores.txt``` and as a graph in ```src/visualization/visualization_images/model_evaluation.png```
The model evaluation script produces the text file and graph which is run with the command: ```python src/visualization/evaluate_models.py```

## 🔧 Model Tuning & Improvements
- **Feature Engineering:** Add `price per sqft`, `location`, or `year_built` for better accuracy.
- **Hyperparameter Tuning:** Use `GridSearchCV` or `RandomizedSearchCV` to optimize model parameters.
- **Geospatial Data Integration:** Include distance to TTC subway stations for location-based price adjustments.
- **Deployment:** The pre-trained model is stored and used directly for predictions.

## 🏆 Next Steps
To further enhance the model and improve usability, we plan to:

- **Enhance Model Generalization** – Optimize hyperparameters and expand training data to improve model accuracy across diverse property listings.
- **Improve the Web App UI** – Implement a more user-friendly interface with interactive elements and enhanced visualization features.
- **Expand Location Coverage** – Incorporate additional real estate data beyond Toronto’s downtown core to improve model applicability.
- **Integrate Complete Location Data** – Utilize more comprehensive geospatial datasets to refine property location-based predictions.
- **Enable Real-Time Data Updates** – Implement dynamic data updates to provide more accurate, real-time price predictions, helping stakeholders make informed decisions.

## 📜 Open Source & Licensing
This project uses the following open-source libraries:

### **Machine Learning Libraries**
- **[Scikit-learn](https://github.com/scikit-learn/scikit-learn)** (BSD-3 License) – Used for regression models and preprocessing.
- **[XGBoost](https://github.com/dmlc/xgboost)** (Apache 2.0 License) – Used for gradient boosting regression.
- **[LightGBM](https://github.com/microsoft/LightGBM)** (MIT License) – Used for efficient boosting regression.

### **Data Handling & Computation**
- **[Pandas](https://github.com/pandas-dev/pandas)** (BSD-3 License) – Used for data manipulation and analysis.
- **[NumPy](https://github.com/numpy/numpy)** (BSD License) – Used for numerical computing.
- **[SciPy](https://github.com/scipy/scipy)** (BSD License) – Used for scientific computations.
- **[Joblib](https://github.com/joblib/joblib)** (BSD License) – Used for model persistence.

### **Data Visualization**
- **[Matplotlib](https://github.com/matplotlib/matplotlib)** (PSF License) – Used for data visualization.
- **[Seaborn](https://github.com/mwaskom/seaborn)** (BSD License) – Used for statistical data visualization.

### **Geospatial Data & Mapping**
- **[GeoPandas](https://github.com/geopandas/geopandas)** (BSD License) – Used for geospatial data handling.
- **[Folium](https://github.com/python-visualization/folium)** (MIT License) – Used for interactive map visualizations.
- **[Shapely](https://github.com/shapely/shapely)** (BSD License) – Used for spatial operations.

### **Web Application**
- **[Streamlit](https://github.com/streamlit/streamlit)** (Apache 2.0 License) – Used for building the interactive web application.

For full licensing details, please refer to the respective repositories.

## 📜 Troubleshooting
If you encounter a `ModuleNotFoundError` when running a script from the command line, ensure the `src` directory is recognized as a package.

### ✅ **Fix: Set the Python Path**
#### **Windows (cmd)**
```bash
set PYTHONPATH=%CD%
```
#### **PowerShell**
```powershell
$env:PYTHONPATH = $PWD
```
#### **Mac/Linux**
```bash
export PYTHONPATH=$(pwd)
```
Alternatively, navigate to the `src` directory and run:
```bash
cd src
```

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
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
