
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def run_sequence_plots():
    """Generates run-sequence plots for different assumption violations."""
    np.random.seed(42)
    n = 200
    
    # Random Data (Assumption Holds)
    random_data = np.random.normal(0, 1, n)
    
    # Drift (Mean changes) - Location Assumption Violation
    drift_data = random_data + np.linspace(0, 5, n)
    
    # Varying Spread (Std changes) - Variation Assumption Violation
    spread_data = np.random.normal(0, np.linspace(1, 5, n), n)
    
    # Autocorrelation (Not Random) - Independence Violation
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = 0.8 * x[t-1] + np.random.normal(0, 0.5)
    
    fig, axes = plt.subplots(4, 1, figsize=(12, 12))
    axes[0].plot(random_data)
    axes[0].set_title('Random Data (Good)')
    
    axes[1].plot(drift_data)
    axes[1].set_title('Drift (Location Shift)')
    
    axes[2].plot(spread_data)
    axes[2].set_title('Varying Spread (Heteroscedasticity)')
    
    axes[3].plot(x)
    axes[3].set_title('Autocorrelation (Not Random)')
    
    plt.tight_layout()
    plt.savefig('assumption_check_plots.png')
    print("Assumption plots saved.")

def classical_vs_eda(data):
    """
    Demonstrates Classical vs EDA approach.
    Classical: Assume Normal -> calculate Mean/Std -> done.
    EDA: Look at data -> realize it's bimodal -> mean is misleading.
    """
    print("\n--- Classical vs EDA ---")
    
    # Classical Summary
    mean_val = np.mean(data)
    std_val = np.std(data)
    print(f"[Classical] Assumed Normal. Mean: {mean_val:.2f}, Std: {std_val:.2f}")
    
    # EDA Approach
    print(f"[EDA] Let's plot it first.")
    plt.figure()
    plt.hist(data, bins=30, alpha=0.7, label='Data Histogram')
    plt.axvline(mean_val, color='r', linestyle='--', label='Mean (Classical)')
    plt.title("Why EDA Matters: Mean is in the valley!")
    plt.legend()
    plt.savefig('eda_vs_classical.png')
    print("EDA plot saved. Notice how the mean is misleading for this bimodal data.")

if __name__ == "__main__":
    run_sequence_plots()
    
    # Generate Bimodal Data (Two humps)
    bimodal_data = np.concatenate([np.random.normal(-2, 1, 100), np.random.normal(2, 1, 100)])
    classical_vs_eda(bimodal_data)
