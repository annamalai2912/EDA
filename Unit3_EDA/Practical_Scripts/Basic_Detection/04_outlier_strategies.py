
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def outliers_iqr(data):
    """
    Detects outliers using IQR (Interquartile Range) Method.
    Upper Bound = Q3 + 1.5 * IQR
    Lower Bound = Q1 - 1.5 * IQR
    """
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    print(f"\n[IQR Method] Bounds: ({lower_bound:.2f}, {upper_bound:.2f})")
    print(f"Outliers Found: {outliers}")
    return outliers

def outliers_zscore(data, thresh=3):
    """
    Detects outliers using Z-Score Method.
    Typically, any > 3 or < -3 is considered an outlier.
    Assumes Normal Distribution.
    """
    z_scores = stats.zscore(data)
    outliers = data[np.abs(z_scores) > thresh]
    print(f"\n[Z-Score Method] Threshold: {thresh}")
    print(f"Outliers Found: {outliers}")
    return outliers

def outliers_mad(data, thresh=3.5):
    """
    Detects outliers using MAD (Median Absolute Deviation).
    Formula: MAD = median(|x_i - median(x)|)
    Modified Z-Score = 0.6745 * (x_i - median(x)) / MAD
    This is ROBUST to outliers itself.
    """
    med = np.median(data)
    mad = np.median(np.abs(data - med))
    
    modified_z_score = 0.6745 * (data - med) / mad
    outliers = data[np.abs(modified_z_score) > thresh]
    
    print(f"\n[MAD Method] (Robust)")
    print(f"Outliers Found: {outliers}")
    return outliers

if __name__ == "__main__":
    np.random.seed(42)
    # Generate Normal Data
    data = np.random.normal(0, 1, 100)
    
    # Introduce Outliers
    data[0] = 10 # Obvious Outlier
    data[1] = -8 # Obvious Outlier
    
    print("--- Visualizing Outliers ---")
    plt.boxplot(data)
    plt.title("Box Plot (Visual Outlier Detection)")
    plt.savefig('boxplot_outliers.png')
    
    outliers_iqr(data)
    outliers_zscore(data)
    outliers_mad(data)
