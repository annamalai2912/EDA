
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_types_of_data():
    """Generates examples of different data types."""
    print("--- Generating Data Types (Lab Exp 1) ---")
    
    # 1. Cross Sectional (Multiple students, 1 year)
    data_cross_sec = {
        'Student': ['A', 'B', 'C', 'D'],
        'Year': [2022, 2022, 2022, 2022],
        'Score': [85, 90, 78, 92]
    }
    df_cs = pd.DataFrame(data_cross_sec)
    print("\n[Cross-Sectional Data]:\n", df_cs)
    
    # 2. Time Series (1 stock, Multiple days)
    data_ts = {
        'Date': pd.date_range(start='2022-01-01', periods=4),
        'Company': ['Apple'] * 4,
        'Price': [150, 152, 149, 155]
    }
    df_ts = pd.DataFrame(data_ts)
    print("\n[Time Series Data]:\n", df_ts)
    
    # 3. Panel Data (Multiple students, Multiple years)
    data_panel = {
        'Student': ['A', 'A', 'B', 'B'],
        'Year': [2021, 2022, 2021, 2022],
        'GPA': [3.5, 3.6, 3.8, 3.9]
    }
    df_panel = pd.DataFrame(data_panel)
    print("\n[Panel Data (Longitudinal)]:\n", df_panel)

def frequency_distribution():
    """Calculates and plots frequency distribution (Lab Exp 1 - Unit 1)."""
    print("\n--- Frequency Distribution ---")
    np.random.seed(42)
    ages = np.random.randint(18, 60, size=100) # 100 people ages
    
    # Create Frequency Table
    freq_table = pd.Series(ages).value_counts().sort_index()
    print("Top 5 Ages Frequency:\n", freq_table.head())
    
    # Plot
    plt.figure(figsize=(10, 5))
    plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
    plt.title('Frequency Distribution of Ages')
    plt.xlabel('Age Groups')
    plt.ylabel('Frequency')
    plt.savefig('frequency_dist.png')
    print("Saved frequency plot to 'frequency_dist.png'")

if __name__ == "__main__":
    generate_types_of_data()
    frequency_distribution()
