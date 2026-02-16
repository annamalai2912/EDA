
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer, KNNImputer

def create_dirty_data():
    """Generates a dataset with intentional missing values, duplicates, and outliers."""
    np.random.seed(42)
    n = 20
    data = {
        'ID': range(1, n + 1),
        'Age': np.random.randint(20, 60, n).astype(float),
        'Salary': np.random.normal(50000, 15000, n),
        'City': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], n),
        'Joined_Date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, n), unit='D')
    }
    df = pd.DataFrame(data)
    
    # Introduce Missing Values (MCAR/MAR)
    df.loc[2, 'Age'] = np.nan
    df.loc[5, 'Age'] = np.nan
    df.loc[8, 'Salary'] = np.nan
    df.loc[10, 'City'] = np.nan  # Missing categorical
    df.loc[12, 'City'] = np.nan
    
    # Introduce Duplicates
    df = pd.concat([df, df.iloc[[0, 1]]], axis=0, ignore_index=True)
    
    # Introduce Outliers
    df.loc[15, 'Salary'] = 1000000  # Massive salary
    
    return df

def clean_data(df):
    """Demonstrates data cleaning steps."""
    print("--- 1. Initial Data Inspection ---")
    print("Shape:", df.shape)
    print("\nMissing Values per Column:\n", df.isnull().sum())
    
    print("\n--- 2. Handling Duplicates ---")
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
    df_cleaned = df.drop_duplicates()
    print(f"Shape after removing duplicates: {df_cleaned.shape}")

    return df_cleaned

def impute_missing_numerical(df):
    """Demonstrates numerical imputation."""
    print("\n--- 3. Handling Missing Numerical Values ---")
    
    # Strategy 1: Mean Imputation
    imputer_mean = SimpleImputer(strategy='mean')
    df_mean = df.copy()
    df_mean['Age'] = imputer_mean.fit_transform(df_mean[['Age']])
    print("Imputed Age with Mean (first 5 rows):\n", df_mean['Age'].head())
    
    # Strategy 2: Median Imputation (better for outliers)
    imputer_median = SimpleImputer(strategy='median')
    df_median = df.copy()
    df_median['Salary'] = imputer_median.fit_transform(df_median[['Salary']])
    print("Imputed Salary with Median (first 5 rows):\n", df_median['Salary'].head())
    
    # Strategy 3: KNN Imputation (advanced)
    print("Imputing with KNN (considering correlations)...")
    imputer_knn = KNNImputer(n_neighbors=3)
    # KNN works on numerical data only for sklearn implementation mostly
    numeric_df = df[['Age', 'Salary']]
    imputed_array = imputer_knn.fit_transform(numeric_df)
    df_knn = df.copy()
    df_knn[['Age', 'Salary']] = imputed_array
    print("Imputed Age/Salary with KNN:\n", df_knn[['Age', 'Salary']].head())
    
    return df_median  # Returning one for further steps

def impute_missing_categorical(df):
    """Demonstrates categorical imputation."""
    print("\n--- 4. Handling Missing Categorical Values ---")
    
    # Strategy 1: Mode (Most Frequent)
    mode_val = df['City'].mode()[0]
    df_mode = df.copy()
    df_mode['City'].fillna(mode_val, inplace=True)
    print(f"Imputed City with Mode ({mode_val}):\n", df_mode['City'].tail())
    
    # Strategy 2: New Category ('Unknown')
    df_new_cat = df.copy()
    df_new_cat['City'].fillna('Unknown', inplace=True)
    print("Imputed City with 'Unknown':\n", df_new_cat['City'].tail())

def visualize_outliers(df):
    """Visualizes outliers before and after cleaning."""
    print("\n--- 5. Visualizing Outliers ---")
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df['Salary'])
    plt.title('Salary Distribution (with Outlier)')
    
    # Simple capping for visualization
    capped_salary = df['Salary'].copy()
    upper_limit = df['Salary'].quantile(0.95)
    capped_salary[capped_salary > upper_limit] = upper_limit
    
    plt.subplot(1, 2, 2)
    sns.boxplot(y=capped_salary)
    plt.title('Salary Distribution (Capped Outlier)')
    
    plt.tight_layout()
    print("Saving outlier plot to '03_outlier_plot.png'...")
    plt.savefig('03_outlier_plot.png')
    plt.show()

if __name__ == "__main__":
    print("Creating Dirty Data...")
    df = create_dirty_data()
    
    df_cleaned = clean_data(df)
    
    df_imputed = impute_missing_numerical(df_cleaned)
    impute_missing_categorical(df_imputed)
    visualize_outliers(df_imputed)
    print("\nDone! Check the generated PNG image.")
