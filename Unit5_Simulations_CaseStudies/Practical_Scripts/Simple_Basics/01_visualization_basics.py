
import matplotlib.pyplot as plt
import seaborn as sns

# Basic Visualization Script
def visualize_iris():
    """Visualize the famous Iris dataset using Seaborn."""
    df = sns.load_dataset('iris')
    
    # 1. Pairplot (Multivariate Analysis)
    print("Generating Pairplot...")
    sns.pairplot(df, hue='species')
    plt.savefig('iris_pairplot.png')
    
    # 2. Violin Plot (Distribution by Category)
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='species', y='sepal_length', data=df)
    plt.title('Sepal Length Distribution by Species')
    plt.savefig('iris_violin.png')
    
    # 3. FacetGrid (Conditioned Plotting)
    g = sns.FacetGrid(df, col='species')
    g.map(sns.histplot, 'sepal_width')
    plt.savefig('iris_facet.png')
    
    print("Visualizations saved as PNG files.")

if __name__ == "__main__":
    visualize_iris()
