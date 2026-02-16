
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf

def generate_time_series(length=200):
    """Generates synthetic time series data with trend, seasonality, and noise."""
    np.random.seed(42)
    time = np.arange(length)
    
    # Components
    trend = 0.5 * time
    seasonality = 10 * np.sin(2 * np.pi * time / 12) # Monthly cycle
    noise = np.random.normal(0, 5, length)
    
    # Combine
    data = trend + seasonality + noise
    date_rng = pd.date_range(start='1/1/2020', periods=length, freq='M')
    return pd.Series(data, index=date_rng, name='Sales')

def decompose_time_series(series):
    """Decomposes time series into Trend, Seasonal, and Residual components."""
    print("Decomposing time series...")
    result = seasonal_decompose(series, model='additive')
    
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 12), sharex=True)
    result.observed.plot(ax=ax1, title='Observed')
    result.trend.plot(ax=ax2, title='Trend')
    result.seasonal.plot(ax=ax3, title='Seasonality')
    result.resid.plot(ax=ax4, title='Residuals')
    
    plt.tight_layout()
    plt.savefig('decomposition.png')
    print("Decomposition plot saved to 'decomposition.png'")

def check_stationarity(series):
    """Performs Augmented Dickey-Fuller test (simplified visualization)."""
    # Rolling Statistics
    rolmean = series.rolling(window=12).mean()
    rolstd = series.rolling(window=12).std()

    plt.figure(figsize=(10, 6))
    plt.plot(series, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.savefig('rolling_stats.png')
    print("Rolling stats plot saved to 'rolling_stats.png'")

if __name__ == "__main__":
    print("Generating Synthetic Time Series Data...")
    ts = generate_time_series()
    
    decompose_time_series(ts)
    check_stationarity(ts)
    
    print("Done. Check the images.")
