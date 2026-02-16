
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf

def generate_time_series():
    """Generates synthetic time series data showing different autocorrelation patterns."""
    np.random.seed(123)
    n = 100
    
    # Random Data (White Noise)
    random_data = np.random.normal(0, 1, n)
    
    # Moderate Correlation (Random Walk)
    moderate_corr = np.cumsum(np.random.normal(0, 1, n))
    
    # Strong Autoregressive (AR(1))
    strong_ar = np.zeros(n)
    strong_ar[0] = 0.5
    for t in range(1, n):
        strong_ar[t] = 0.9 * strong_ar[t-1] + np.random.normal(0, 0.1)
        
    # Sinusoidal Correlation (Seasonality)
    time = np.arange(n)
    sinusoidal = np.sin(time / 5) + np.random.normal(0, 0.2, n)
    
    return {
        'Random': random_data,
        'Moderate Trend': moderate_corr,
        'Strong AR(1)': strong_ar,
        'Sinusoidal': sinusoidal
    }

def plot_autocorrelation(ts_dict):
    """Plots the time series and its corresponding autocorrelation function (ACF)."""
    fig, axes = plt.subplots(4, 2, figsize=(15, 20))
    fig.suptitle('Time Series patterns and their Autocorrelation Plots', fontsize=16)
    
    for i, (name, data) in enumerate(ts_dict.items()):
        # Plot Time Series
        axes[i, 0].plot(data)
        axes[i, 0].set_title(f'{name} - Time Series')
        axes[i, 0].set_ylabel('Value')
        
        # Plot Autocorrelation
        plot_acf(data, ax=axes[i, 1], lags=20, title=f'{name} - Autocorrelation')
        
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)
    print("Saving plot to '02_autocorrelation_plots.png'...")
    plt.savefig('02_autocorrelation_plots.png')
    plt.show()

if __name__ == "__main__":
    print("Generating Synthetic Time Series Data...")
    ts_data = generate_time_series()
    
    print("Plotting Autocorrelation Functions...")
    plot_autocorrelation(ts_data)
    print("Done! Check the generated PNG image.")
