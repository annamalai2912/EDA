
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

def advanced_statistical_analysis():
    """Performs ANOVA, Bartlett's Test, and calculates Confidence Intervals (Lab Exp 4, 8)."""
    print("\n--- Advanced Statistical Analysis ---")
    
    # 1. Generate Data (3 groups with potentially different means)
    np.random.seed(42)
    group_A = np.random.normal(10, 2, 50)
    group_B = np.random.normal(12, 2.5, 50) # Higher mean
    group_C = np.random.normal(10.5, 2, 50)
    
    # 2. Bartlett's Test for Homogeneity of Variances
    # H0: Variances are equal.
    # H1: Variances are NOT equal.
    stat, p_val = stats.bartlett(group_A, group_B, group_C)
    print(f"Bartlett's Test: statistic={stat:.4f}, p-value={p_val:.4f}")
    if p_val > 0.05:
        print(" -> Variances are equal (Fail to reject H0). Safe to proceed with standard ANOVA.")
    else:
        print(" -> Variances are NOT equal (Reject H0). Consider Welch's ANOVA.")
        
    # 3. One-Way ANOVA
    # H0: Means are equal.
    # H1: Means are NOT equal.
    f_stat, f_p_val = stats.f_oneway(group_A, group_B, group_C)
    print(f"\nANOVA Results: F-stat={f_stat:.4f}, p-value={f_p_val:.4f}")
    if f_p_val < 0.05:
        print(" -> At least one group mean is significantly different.")
        
    # 4. Central Tendency & Confidence Intervals
    sample_mean = np.mean(group_A)
    # Calculate 95% Confidence Interval for the mean
    lower, upper = stats.t.interval(0.95, len(group_A)-1, loc=np.mean(group_A), scale=stats.sem(group_A))
    print(f"\nGroup A Statistics:")
    print(f"  Mean: {sample_mean:.2f}")
    print(f"  Std Dev: {np.std(group_A):.2f}")
    print(f"  95% Confidence Interval: ({lower:.2f}, {upper:.2f})")
    
    # 5. Skewness and Kurtosis (Symmetry/Concentration)
    skew = stats.skew(group_A)
    kurt = stats.kurtosis(group_A)
    print(f"\nDistribution Shape:")
    print(f"  Skewness: {skew:.2f} (Close to 0 is symmetric)")
    print(f"  Kurtosis: {kurt:.2f} (Close to 0 is normal-like for Fisher definition)")

def plot_distributions():
    """Visualizes different probability distributions (Unit 4 Syllabus)."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Normal Distribution
    x = np.linspace(-3, 3, 100)
    axes[0].plot(x, stats.norm.pdf(x), 'r-', label='Normal(0,1)')
    axes[0].set_title('Normal Distribution')
    
    # T-Distribution (Fat tails)
    axes[1].plot(x, stats.t.pdf(x, df=2), 'b-', label='t-dist(df=2)') # Low degrees of freedom -> heavier tails
    axes[1].plot(x, stats.norm.pdf(x), 'r--', alpha=0.5, label='Normal')
    axes[1].set_title('Student\'s t-Distribution')
    axes[1].legend()
    
    # Exponential Distribution
    x_pos = np.linspace(0, 5, 100)
    axes[2].plot(x_pos, stats.expon.pdf(x_pos), 'g-', label='Exp(1)')
    axes[2].set_title('Exponential Distribution')
    
    plt.tight_layout()
    plt.savefig('probability_distributions.png')
    print("\nSaved distribution plots to 'probability_distributions.png'")

if __name__ == "__main__":
    advanced_statistical_analysis()
    plot_distributions()
