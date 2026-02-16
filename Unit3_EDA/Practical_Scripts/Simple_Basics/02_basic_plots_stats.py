
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

def create_simple_dataset():
    """Calculates basic statistics for a small dataset."""
    data = {
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Cable'],
        'Price': [800, 20, 50, 200, 10],
        'Quantity': [10, 100, 50, 15, 200],
        'Category': ['Electronics', 'Accessory', 'Accessory', 'Electronics', 'Accessory']
    }
    df = pd.DataFrame(data)
    print("Dataset Created:")
    print(df)
    return df

def generate_simple_plots(df):
    """Creates basic histograms and bar charts."""
    plt.figure(figsize=(12, 6))

    # 1. Bar Chart - Count of Products by Category
    plt.subplot(1, 2, 1)
    sns.countplot(x='Category', data=df)
    plt.title('Product Count by Category')

    # 2. Scatter Plot - Price vs Quantity
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='Price', y='Quantity', data=df, hue='Category', s=100)
    plt.title('Price vs Quantity Relationship')

    plt.tight_layout()
    plt.savefig('simple_basic_plots.png')
    plt.show()
    print("\nCheck 'simple_basic_plots.png' for the visualizations.")

def calculate_stats(df):
    """Computes basic descriptive statistics."""
    print("\n--- Descriptive Statistics ---")
    print("Mean Price:", df['Price'].mean())
    print("Median Quantity:", df['Quantity'].median())
    print("Mode Category:", df['Category'].mode()[0])
    print("Standard Deviation of Price:", df['Price'].std())

if __name__ == "__main__":
    df = create_simple_dataset()
    calculate_stats(df)
    generate_simple_plots(df)
