import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, color='red')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred_2000 = pd.Series(range(2000, 2051))
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    ax.plot(x_pred_2000, y_pred_2000, color='green')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return ax