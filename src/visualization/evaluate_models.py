"""
Real Estate Price Prediction - Comparison of Multiple Models Evaluation Visualization

This script produces a visualization of the evaluation of the performance
of multiple models in predicting listing prices.

Author: Vennise Ho
Date: 2025-03-01
Generated with assistance from ChatGPT (OpenAI)
"""
from matplotlib import pyplot as plt
from src.models.multiple_models import train_and_evaluate_models


def plot_model_comparison(results_df):
    """
    Generates a visualization comparing model performance metrics.

    This function takes a DataFrame containing model evaluation results and creates
    bar plots comparing the models based on their R² Score and Mean Absolute Error (MAE).

    :param results_df: DataFrame containing model performance metrics with "R² Score" and "MAE" columns.
    :type results_df: pd.DataFrame
    :return: None (Displays the visualization)
    """
    plt.figure(figsize=(10, 5))
    results_df.sort_values(by="R² Score", ascending=False, inplace=True)

    # Plot R² Scores
    plt.subplot(1, 2, 1)
    results_df["R² Score"].plot(kind="bar", color="skyblue")
    plt.title("R² Score Comparison")
    plt.xticks(rotation=45)

    # Plot Mean Absolute Error
    plt.subplot(1, 2, 2)
    results_df["MAE"].plot(kind="bar", color="orange")
    plt.title("Mean Absolute Error (MAE)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


file_path = "../../data/cleaned_real_estate_data_numerical.csv"
results = train_and_evaluate_models(file_path)
plot_model_comparison(results)
