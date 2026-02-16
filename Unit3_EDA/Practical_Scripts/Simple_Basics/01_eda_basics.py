
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set_theme(style="whitegrid")

def generate_sample_data():
    """Generates a sample dataset for EDA demonstration."""
    np.random.seed(42)
    n = 200
    data = {
        'Student_ID': range(1, n + 1),
        'Age': np.random.randint(18, 25, n),
        'Study_Hours': np.random.normal(5, 2, n),
        'Exam_Score': np.random.normal(70, 15, n),
        'Gender': np.random.choice(['Male', 'Female'], n),
        'Department': np.random.choice(['CS', 'BCA', 'DS', 'IT'], n)
    }
    df = pd.DataFrame(data)
    
    # Introduce some noise/outliers
    df.loc[0, 'Exam_Score'] = 350  # Outlier
    df.loc[5, 'Study_Hours'] = -5  # Impossible value
    
    return df

def basic_eda(df):
    """Performs basic EDA steps."""
    print("--- 1. Data Characterization ---")
    print(f"Shape of dataset: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\n--- 2. Data Info (Types & Missing) ---")
    print(df.info())
    
    print("\n--- 3. Statistical Summary ---")
    print(df.describe())
    
    print("\n--- 4. Checking for Outliers/Anomalies ---")
    # Simple rule: Exam scores shouldn't exceed 100
    outliers = df[df['Exam_Score'] > 100]
    print(f"Potential Outliers in Exam_Score (> 100):\n{outliers}")

def graphical_techniques(df):
    """Demonstrates various graphical techniques."""
    plt.figure(figsize=(15, 10))
    
    # 1. Histogram - Distribution of Exam Scores
    plt.subplot(2, 2, 1)
    sns.histplot(df['Exam_Score'], kde=True, color='blue')
    plt.title('Distribution of Exam Scores (Histogram)')
    
    # 2. Box Plot - Detecting Outliers
    plt.subplot(2, 2, 2)
    sns.boxplot(x='Department', y='Exam_Score', data=df)
    plt.title('Exam Scores by Department (Box Plot)')
    
    # 3. Scatter Plot - Relationship between Study Hours and Score
    plt.subplot(2, 2, 3)
    sns.scatterplot(x='Study_Hours', y='Exam_Score', hue='Gender', data=df)
    plt.title('Study Hours vs Exam Score')
    
    # 4. Bar Chart - Count of Students by Department (Categorical)
    plt.subplot(2, 2, 4)
    sns.countplot(x='Department', data=df, palette='viridis')
    plt.title('Student Count by Department')
    
    plt.tight_layout()
    print("\nSaving plot to '01_eda_plots.png'...")
    plt.savefig('01_eda_plots.png')
    plt.show()

if __name__ == "__main__":
    print("Generating Sample Data...")
    df = generate_sample_data()
    
    print("\nRunning Basic EDA...")
    basic_eda(df)
    
    print("\nGenerating Graphical Analysis...")
    graphical_techniques(df)
    print("\nDone! Check the generated PNG image.")
