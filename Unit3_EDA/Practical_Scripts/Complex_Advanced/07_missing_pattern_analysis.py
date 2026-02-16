
import numpy as np
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

def generate_missing_data_patterns():
    """
    Simulates MCAR, MAR, and MNAR missing patterns.
    """
    np.random.seed(42)
    n = 200
    
    # Base Data (Complete)
    X1 = np.random.normal(10, 2, n)
    X2 = 0.5 * X1 + np.random.normal(0, 1, n)
    X3 = np.random.normal(5, 1, n)
    
    df = pd.DataFrame({'X1': X1, 'X2': X2, 'X3': X3})
    
    # 1. MCAR (Randomly missing X1)
    mask_mcar = np.random.rand(n) < 0.2
    df.loc[mask_mcar, 'X1'] = np.nan
    
    # 2. MAR (Depends on Observed X2)
    # If X2 > 12 (observed), then chance of missing X3
    mask_mar = (df['X2'] > 12) & (np.random.rand(n) < 0.5)
    df.loc[mask_mar, 'X3'] = np.nan
    
    # 3. MNAR (Depends on itself)
    # If X2 was small, it "hided" itself.
    mask_mnar = (df['X2'] < 5)
    df.loc[mask_mnar, 'X2'] = np.nan # This is now tricky to prove since X2 is gone!
    
    return df

def analyze_missing_patterns(df):
    """
    Visualizes missing data patterns using 'missingno' library.
    """
    print("--- Analyzing Missing Patterns ---")
    print(df.isnull().sum())
    
    # Matrix Plot (Where are missing values?)
    msno.matrix(df)
    plt.title("Missing Data Matrix")
    plt.savefig('missing_matrix.png')
    
    # Heatmap (Correlation of missingness)
    # Are X1 and X3 missing together?
    msno.heatmap(df)
    plt.title("Missing Data Correlation Heatmap")
    plt.savefig('missing_heatmap.png')
    
    # Dendrogram (Cluster missingness)
    msno.dendrogram(df)
    plt.title("Missing Data Dendrogram")
    plt.savefig('missing_dendrogram.png')
    
    print("Saved missing pattern visualizations.")

if __name__ == "__main__":
    df = generate_missing_data_patterns()
    analyze_missing_patterns(df)
