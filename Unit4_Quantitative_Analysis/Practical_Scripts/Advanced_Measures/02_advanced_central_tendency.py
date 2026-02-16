
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def central_tendency_comparison():
    """
    Compares Standard Mean, Geometric Mean, and Harmonic Mean.
    - Mean: Typical value.
    - Geometric: For Growth Rates (Multiplicative).
    - Harmonic: For Rates/Ratio (Speed, Efficiency).
    """
    print("--- Comparing Means (Lab Exp 4, 8) ---")
    
    # 1. Growth Rates (Geometric Mean is Appropriate)
    growth_rates = np.array([1.10, 1.50, 0.90]) # +10%, +50%, -10%
    geo_mean = stats.gmean(growth_rates)
    arith_mean = np.mean(growth_rates)
    print(f"\n[Scenario: Growth Rates {growth_rates}]")
    print(f"Geometric Mean (Correct): {geo_mean:.4f} -> {(geo_mean-1)*100:.2f}% avg growth")
    print(f"Arithmetic Mean (Wrong): {arith_mean:.4f} -> {(arith_mean-1)*100:.2f}% avg growth - Overestimates return!")
    
    # 2. Speed (Harmonic Mean is Appropriate)
    # Go 100km at 60km/h, Return 100km at 40km/h. Avg Speed?
    speeds = np.array([60, 40])
    har_mean = stats.hmean(speeds)
    arith_mean_speed = np.mean(speeds)
    print(f"\n[Scenario: Speed {speeds}]")
    print(f"Harmonic Mean (Correct): {har_mean:.2f} km/h")
    print(f"Arithmetic Mean (Wrong): {arith_mean_speed:.2f} km/h")
    
    # 3. Robustness (Median vs Mean)
    salaries = np.array([50, 55, 60, 1000]) # CEO salary outlier
    print(f"\n[Scenario: Salary Skew {salaries}]")
    print(f"Mean: {np.mean(salaries):.2f} (Affected by outlier)")
    print(f"Median: {np.median(salaries):.2f} (Robust)")
    print(f"Trimmed Mean (10%): {stats.trim_mean(salaries, 0.1):.2f} (Robust)")

def dispersion_deep_dive():
    """
    Explores Range, Variance, Std Dev, MAD, CV.
    """
    print("\n--- Measures of Dispersion ---")
    data = np.random.normal(100, 15, 50)
    
    # Range
    r = np.ptp(data)
    print(f"Range (Max-Min): {r:.2f}")
    
    # Variance & Std Dev (Sample vs Population)
    var_sample = np.var(data, ddof=1) # Unbiased (n-1)
    std_sample = np.std(data, ddof=1)
    print(f"Sample Variance: {var_sample:.2f}")
    print(f"Sample Std Dev: {std_sample:.2f}")
    
    # Mean Absolute Deviation (MAD around Mean)
    mad_mean = np.mean(np.abs(data - np.mean(data)))
    print(f"Mean Absolute Deviation: {mad_mean:.2f}")
    
    # Coefficient of Variation (CV) - Unitless Comparison
    cv = (std_sample / np.mean(data)) * 100
    print(f"Coefficient of Variation: {cv:.2f}%")
    
    # Interquartile Range (IQR)
    iqr = stats.iqr(data)
    print(f"Interquartile Range: {iqr:.2f}")

if __name__ == "__main__":
    central_tendency_comparison()
    dispersion_deep_dive()
