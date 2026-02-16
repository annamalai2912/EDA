
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

def generate_4_plot_data(scenario='random'):
    """
    Generates data for a 4-Plot demonstration.
    Scenarios:
        - random (Ideal case)
        - drift (Location parameter changes)
        - spread (Variation parameter changes)
        - correlated (Not random, dependent)
    """
    np.random.seed(42)
    n = 200
    
    if scenario == 'random':
        # Ideal: Normal(0, 1)
        return np.random.normal(0, 1, n)
    
    elif scenario == 'drift':
        # Non-fixed Location: Mean shifts over time
        mean_shift = np.linspace(0, 5, n)
        return np.random.normal(mean_shift, 1, n)
    
    elif scenario == 'correlated':
        # Non-Random: AR(1) Process
        x = np.zeros(n)
        for t in range(1, n):
            x[t] = 0.9 * x[t-1] + np.random.normal(0, 0.5)
        return x

def create_4_plot(data, scenario_name="Random Normal Data"):
    """
    Creates the 4-Plot (Run Sequence, Lag, Histogram, Normal Prob Plot).
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle(f'4-Plot of {scenario_name}', fontsize=16)

    # 1. Run Sequence Plot
    axes[0, 0].plot(data)
    axes[0, 0].set_title("Run Sequence Plot ($Y_i$ vs $i$)")
    axes[0, 0].set_xlabel("Time (i)")
    axes[0, 0].set_ylabel("Y")

    # 2. Lag Plot
    pd.plotting.lag_plot(pd.Series(data), ax=axes[0, 1])
    axes[0, 1].set_title("Lag Plot ($Y_i$ vs $Y_{i-1}$)")

    # 3. Histogram
    axes[1, 0].hist(data, bins=20, density=True, alpha=0.6, color='g')
    # Fit line
    xmin, xmax = axes[1, 0].get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, np.mean(data), np.std(data))
    axes[1, 0].plot(x, p, 'k', linewidth=2)
    axes[1, 0].set_title("Histogram")

    # 4. Normal Probability Plot (QQ Plot)
    stats.probplot(data, dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title("Normal Probability Plot")

    plt.tight_layout()
    plt.savefig(f'4_plot_{scenario_name.lower().replace(" ", "_")}.png')
    print(f"Saved 4-Plot to '4_plot_{scenario_name.lower().replace(' ', '_')}.png'")

if __name__ == "__main__":
    # Simulate Lab Experiment 2
    # 1. Random Data (Assumptions Hold)
    data_random = generate_4_plot_data('random')
    create_4_plot(data_random, "Random Data")

    # 2. Correlated Data (Assumptions Fail)
    data_correlated = generate_4_plot_data('correlated')
    create_4_plot(data_correlated, "Correlated Data")
    
    # 3. Drift Data (Assumptions Fail)
    data_drift = generate_4_plot_data('drift')
    create_4_plot(data_drift, "Drift Data")
