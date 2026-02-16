
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.regressionplots import plot_leverage_resid2

def generate_leverage_data():
    """
    Generates data to demonstrate the difference between Outliers and Leverage Points.
    
    * Outlier: An observation with a large residual (unusual y-value given x).
    * Leverage Point: An observation with an extreme x-value (far from the mean of x).
    """
    np.random.seed(42)
    n = 20
    X = np.random.normal(10, 2, n)
    y = 2 * X + 5 + np.random.normal(0, 2, n)
    
    # Add an Outlier (Unusual Y, Normal X)
    # X is around 10, Mean Y is around 25. Let's make Y=50 at X=10.
    X = np.append(X, 10)
    y = np.append(y, 50) 
    
    # Add a High Leverage Point (Extreme X, follows the trend line)
    # X=20 (far from mean 10), Y should be 2*20+5 = 45.
    X = np.append(X, 20)
    y = np.append(y, 45)
    
    # Add a Reliable High Leverage Point (Extreme X, Bad Y - Influential Point)
    # X=22, Y=10 (Should be near 49). This will pull the regression line.
    X = np.append(X, 22)
    y = np.append(y, 10)
    
    return X, y

def analyze_leverage(X, y):
    """Fits a regression model and plots leverage vs residuals."""
    
    # Add constant for statsmodels
    X_const = sm.add_constant(X)
    
    # Fit OLS Model
    model = sm.OLS(y, X_const).fit()
    print(model.summary())
    
    # Influence Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sm.graphics.influence_plot(model, ax=ax, criterion="cooks")
    plt.title("Influence Plot: Leverage vs Residuals")
    plt.tight_layout()
    plt.savefig('leverage_influence_plot.png')
    print("Saved influence plot to 'leverage_influence_plot.png'")
    
    # Cook's Distance (Measure of Influence)
    # Influence = Leverage * Outlier-ness
    influence = model.get_influence()
    (c, p) = influence.cooks_distance
    
    plt.figure(figsize=(10, 4))
    plt.stem(np.arange(len(c)), c, markerfmt=",")
    plt.title("Cook's Distance (High value = Influential Point)")
    plt.xlabel("Observation Index")
    plt.ylabel("Cook's Distance")
    plt.savefig('cooks_distance.png')

if __name__ == "__main__":
    print("Generating data with Outliers and Leverage Points...")
    X, y = generate_leverage_data()
    
    print("Analyzing Leverage and Influence...")
    analyze_leverage(X, y)
