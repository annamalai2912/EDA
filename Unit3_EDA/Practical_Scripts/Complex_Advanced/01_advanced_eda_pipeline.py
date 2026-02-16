
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf

class DataCleaner(BaseEstimator, TransformerMixin):
    """Custom transformer to handle basic data cleaning."""
    
    def __init__(self, threshold=0.5):
        self.threshold = threshold
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        print(f"[{self.__class__.__name__}] Starting data cleaning...")
        df = X.copy()
        
        # 1. Drop duplicates
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            print(f" Dropping {duplicates} duplicate rows...")
            df = df.drop_duplicates()
            
        # 2. Check for missing values > threshold
        missing_percent = df.isnull().mean()
        high_missing_cols = missing_percent[missing_percent > self.threshold].index
        if len(high_missing_cols) > 0:
            print(f" Dropping columns with >{self.threshold*100}% missing data: {list(high_missing_cols)}")
            df = df.drop(columns=high_missing_cols)
            
        return df

class AdvancedEDA:
    """Comprehensive EDA pipeline."""
    
    def __init__(self, data_path=None, df=None):
        if data_path:
            self.df = pd.read_csv(data_path)
        elif df is not None:
            self.df = df
        else:
            raise ValueError("Provide either data_path or df.")
            
    def analyze_consistency(self):
        """Checks for data consistency issues."""
        print("\n--- Consistency Check ---")
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        # Check for negative values in columns that typically shouldn't be negative (heuristic)
        for col in numeric_cols:
            negatives = (self.df[col] < 0).sum()
            if negatives > 0:
                print(f"Warning: Column '{col}' has {negatives} negative values. Potential pollution/outlier.")
                
        # Check for identical columns (Redundant)
        visited = set()
        for i, col1 in enumerate(self.df.columns):
            for col2 in self.df.columns[i+1:]:
                if self.df[col1].equals(self.df[col2]):
                    print(f"RED FLAG: Columns '{col1}' and '{col2}' are identical (Duplicate Feature).")

    def analyze_autocorrelation(self, time_col, value_col):
        """Advanced Time Series Decomposition & Autocorrelation."""
        print(f"\n--- Advanced Time Series Analysis on '{value_col}' ---")
        
        # Ensure datetime index
        ts_df = self.df.copy()
        ts_df[time_col] = pd.to_datetime(ts_df[time_col])
        ts_df = ts_df.set_index(time_col).sort_index()
        
        # Decompose
        # Fill missing values for decomposition
        ts_df[value_col] = ts_df[value_col].interpolate(method='time')
        
        result = seasonal_decompose(ts_df[value_col], model='additive', period=12) # Assuming monthly seasonality
        
        fig, axes = plt.subplots(4, 1, figsize=(12, 10))
        result.observed.plot(ax=axes[0], title='Observed')
        result.trend.plot(ax=axes[1], title='Trend')
        result.seasonal.plot(ax=axes[2], title='Seasonality')
        result.resid.plot(ax=axes[3], title='Residuals')
        plt.tight_layout()
        plt.savefig('ts_decomposition.png')
        print("Saved decomposition plot to 'ts_decomposition.png'")
        
        # Autocorrelation Plot
        plt.figure(figsize=(10, 5))
        plot_acf(ts_df[value_col], lags=40, title=f"Autocorrelation of {value_col}")
        plt.savefig('ts_autocorrelation.png')
        print("Saved autocorrelation plot to 'ts_autocorrelation.png'")

    def multivariate_analysis(self):
        """Generates correlation heatmap and pairplots."""
        print("\n--- Multivariate Analysis ---")
        
        # Correlation Matrix
        numeric_df = self.df.select_dtypes(include=[np.number])
        corr = numeric_df.corr()
        
        plt.figure(figsize=(10, 8))
        mask = np.triu(np.ones_like(corr, dtype=bool)) # Mask upper triangle
        sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap (Lower Triangle)')
        plt.savefig('correlation_heatmap.png')
        print("Saved heatmap to 'correlation_heatmap.png'")

# Example Usage
if __name__ == "__main__":
    # Generate complex synthetic data
    np.random.seed(42)
    dates = pd.date_range(start='2020-01-01', periods=200, freq='M')
    data = {
        'Date': dates,
        'Sales': np.linspace(100, 500, 200) + np.sin(np.arange(200)/12 * 2*np.pi) * 50 + np.random.normal(0, 20, 200),
        'Marketing_Spend': np.linspace(50, 200, 200) + np.random.normal(0, 10, 200),
        'Competitor_Price': np.random.normal(100, 5, 200),
        'Redundant_Sales': np.linspace(100, 500, 200) + np.sin(np.arange(200)/12 * 2*np.pi) * 50 + np.random.normal(0, 20, 200) # Identical
    }
    # Introduce pollution
    data['Marketing_Spend'][5] = -999 # Pollution
    
    df = pd.DataFrame(data)
    
    # 1. Clean Data via Class
    cleaner = DataCleaner()
    df_cleaned = cleaner.transform(df)
    
    # 2. Advanced Analysis
    eda = AdvancedEDA(df=df_cleaned)
    eda.analyze_consistency()
    eda.multivariate_analysis()
    eda.analyze_autocorrelation('Date', 'Sales')
