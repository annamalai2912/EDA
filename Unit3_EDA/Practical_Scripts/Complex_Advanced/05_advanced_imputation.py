
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, KNNImputer
from sklearn.metrics import mean_squared_error

# Setting seed for reproducibility
np.random.seed(42)

def generate_missing_data(n_samples=500, missing_fraction=0.2):
    """Generates synthetic data with correlated features and introduces missing values."""
    X1 = np.random.normal(loc=10, scale=3, size=n_samples)
    X2 = 0.5 * X1 + np.random.normal(loc=0, scale=1, size=n_samples) # X2 depends on X1
    X3 = 2.0 * X2 + np.random.normal(loc=5, scale=2, size=n_samples) # X3 depends on X2
    
    df_complete = pd.DataFrame({'Feature_1': X1, 'Feature_2': X2, 'Feature_3': X3})
    
    # Introduce missing values (MAR/MCAR)
    df_missing = df_complete.copy()
    
    # Set values to NaN randomly
    mask = np.random.rand(n_samples) < missing_fraction
    df_missing.loc[mask, 'Feature_2'] = np.nan
    
    return df_complete, df_missing

def compare_imputations(df_truth, df_missing):
    """Compares different imputation techniques against the ground truth."""
    
    methods = {
        'Mean Imputation': lambda df: df.fillna(df.mean()),
        'Median Imputation': lambda df: df.fillna(df.median()),
        'KNN Imputation (k=5)': lambda df: pd.DataFrame(KNNImputer(n_neighbors=5).fit_transform(df), columns=df.columns),
        'MICE (Iterative Imputer)': lambda df: pd.DataFrame(IterativeImputer(random_state=42).fit_transform(df), columns=df.columns)
    }
    
    results = {}
    
    plt.figure(figsize=(15, 10))
    # Plot truth distribution
    plt.subplot(3, 2, 1)
    df_truth['Feature_2'].plot(kind='kde', color='black', linewidth=2, label='True Distribution')
    plt.title('Ground Truth')
    plt.legend()

    for i, (name, func) in enumerate(methods.items(), 2):
        imputed_df = func(df_missing.copy())
        
        # Calculate RMSE for the missing entries only
        mask = df_missing['Feature_2'].isnull()
        rmse = np.sqrt(mean_squared_error(df_truth.loc[mask, 'Feature_2'], imputed_df.loc[mask, 'Feature_2']))
        results[name] = rmse
        
        # Plot distribution
        plt.subplot(3, 2, i)
        imputed_df['Feature_2'].plot(kind='kde', color='red', linestyle='--', label='Imputed')
        df_truth['Feature_2'].plot(kind='kde', color='black', alpha=0.3, label='Truth')
        plt.title(f'{name}\nRMSE: {rmse:.4f}')
        plt.legend()
        
    plt.tight_layout()
    plt.savefig('imputation_comparison.png')
    print("Saved imputation comparison plot to 'imputation_comparison.png'")
    
    return results

if __name__ == "__main__":
    print("Generating synthetic data with correlations...")
    df_truth, df_missing = generate_missing_data()
    
    print("Comparing Imputation Techniques...")
    results = compare_imputations(df_truth, df_missing)
    
    print("\n--- RMSE Results (Lower is Better) ---")
    for method, score in sorted(results.items(), key=lambda x: x[1]):
        print(f"{method}: {score:.4f}")
