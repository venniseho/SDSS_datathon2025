"""
Real Estate Price Prediction Web App

This Streamlit application allows users to input property details and predicts the listing price
using a trained machine learning model.

Features:
- User-friendly interface for inputting property details
- Supports numerical and categorical input fields
- Loads a pre-trained model to make real-time predictions
- Displays the predicted listing price

Author: Vennise Ho
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
import os

import streamlit as st
import pandas as pd
import joblib  # For loading the trained model

# Get the absolute path of the current script (app.py) and define the correct model path
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "models", "real_estate_model.pkl")

# Load the path from joblib
model = joblib.load(model_path)


# Streamlit UI
def main():
    """
    Streamlit web application for real estate price prediction.

    Users can enter property details such as:
    - Number of bedrooms
    - Number of bathrooms
    - Monthly maintenance fee
    - Size group (categorized by square footage)

    The trained model will predict the estimated listing price based on the inputs.
    """
    st.title("🏠 Real Estate Price Prediction")
    st.write("Enter the details of the property to predict the listing price.")

    # User Input
    num_beds = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1, value=3)
    num_baths = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1, value=2)
    monthly_maintenance_fee = st.number_input("Monthly Maintenance Fee ($)", min_value=0, step=50, value=500)
    size_group = st.selectbox("Size Group", options=[0, 1, 2, 3, 4, 5, 6, 7, 8],
                              format_func=lambda x: {0: "0-499 sqft", 1: "500-999 sqft", 2: "1000-1499 sqft",
                                                     3: "1500-1999 sqft", 4: "2000-2499 sqft", 5: "2500-2999 sqft",
                                                     6: "3000-3499 sqft", 7: "3500-3999 sqft", 8: "4000+ sqft"}[x])

    if st.button("Predict Price"):
        # Create input DataFrame
        input_data = pd.DataFrame([[num_beds, num_baths, monthly_maintenance_fee, size_group]],
                                  columns=["num_beds", "num_baths", "monthly_maintenance_fee", "size_group"])

        # Make prediction
        predicted_price = model.predict(input_data)[0]

        # Display result
        st.success(f"🏡 Predicted Listing Price: **${predicted_price:,.2f}**")


if __name__ == "__main__":
    main()
