
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

def clean_data_example():
    """Demonstrates handling missing values and duplicates."""
    
    # 1. Create a "dirty" dataset
    data = {
        'CustomerID': [1, 2, 3, 4, 2, 5], # Duplicate ID
        'Age': [25, 30, np.nan, 22, 30, 999], # Missing, Duplicate, Outlier
        'PurchaseAmount': [100, 200, 150, np.nan, 200, 50] # Missing, Duplicate
    }
    df = pd.DataFrame(data)
    print("--- Original Dirty Data ---")
    print(df)
    
    print("\n--- Step 1: Handling Duplicates ---")
    duplicates = df.duplicated()
    print(f"Found {duplicates.sum()} duplicate rows.")
    df_no_dupes = df.drop_duplicates()
    print("Dropped Duplicates:")
    print(df_no_dupes)
    
    print("\n--- Step 2: Handling Missing Values (Simple) ---")
    # Identify Nulls
    print("Null Values Check:\n", df_no_dupes.isnull().sum())
    
    # Fill NA with Mean (Simple)
    df_imputed = df_no_dupes.copy()
    mean_age = df_imputed['Age'][df_imputed['Age'] != 999].mean() # Excluding outlier
    df_imputed['Age'] = df_imputed['Age'].fillna(mean_age)
    
    median_purchase = df_imputed['PurchaseAmount'].median()
    df_imputed['PurchaseAmount'] = df_imputed['PurchaseAmount'].fillna(median_purchase)
    
    print("\nImputed Data:")
    print(df_imputed)

    return df_imputed

if __name__ == "__main__":
    clean_data_example()
