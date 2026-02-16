
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

def random_walk_simulation():
    """Simulate a 1D Random Walk (Lab Exp 5)."""
    print("\n--- Random Walk Simulation ---")
    np.random.seed(42)
    n_steps = 1000
    
    # Generate steps: +1 or -1 with equal probability
    steps = np.random.choice([-1, 1], size=n_steps)
    position = np.cumsum(steps) # Walk is cumulative sum of steps
    
    plt.figure(figsize=(10, 4))
    plt.plot(position)
    plt.title(f"1D Random Walk ({n_steps} steps)")
    plt.xlabel("Step")
    plt.ylabel("Position")
    plt.grid(True)
    plt.savefig('random_walk.png')
    print("Saved random walk plot to 'random_walk.png'")

def chi_square_test():
    """Perform Chi-Square Test of Independence (Lab Exp 7)."""
    print("\n--- Chi-Square Test & Contingency Table ---")
    # Example: Gender vs Preference for Tea/Coffee
    # Man: 20 Tea, 30 Coffee
    # Woman: 25 Tea, 25 Coffee
    observed = np.array([[20, 30], [25, 25]])
    
    chi2, p, dof, expected = stats.chi2_contingency(observed)
    
    print(f"Observed Table:\n{observed}")
    print(f"Chi-Sq Statistic: {chi2:.4f}")
    print(f"P-Value: {p:.4f}")
    
    # Calculate Phi Coefficient for 2x2
    n = np.sum(observed)
    phi = np.sqrt(chi2 / n)
    print(f"Phi Coefficient: {phi:.4f} (Measure of Association)")

def correlation_analysis():
    """Calculate Pearson vs Spearman Correlation (Lab Exp 6)."""
    print("\n--- Comparison of Correlation Coefficients ---")
    
    # Generate data with a monotonic but non-linear relationship (Ideal for Spearman)
    x = np.arange(10)
    y = x**2 # Non-linear (Quadratic)
    
    # Add outlier to mess up Pearson
    x_outlier = np.append(x, 100) # outlier
    y_outlier = np.append(y, 100000) # outlier
    
    pearson_r, _ = stats.pearsonr(x, y)
    spearman_rho, _ = stats.spearmanr(x, y)
    kendall_tau, _ = stats.kendalltau(x, y)
    
    print(f"Data X: {x}")
    print(f"Data Y (X^2): {y}")
    print(f"Pearson r (Linear): {pearson_r:.4f}")
    print(f"Spearman rho (Rank): {spearman_rho:.4f} (Should be 1.0 for monotonic)")
    print(f"Kendall tau: {kendall_tau:.4f}")

if __name__ == "__main__":
    random_walk_simulation()
    chi_square_test()
    correlation_analysis()
