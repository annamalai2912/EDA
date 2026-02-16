
import numpy as np
import pandas as pd

def numpy_basics():
    """Demonstrates basic Numpy array operations."""
    print("--- Numpy Basics ---")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print(f"Mean: {np.mean(arr):.2f}")
    print(f"Std Dev: {np.std(arr):.2f}")
    print(f"Sum: {np.sum(arr)}")
    
    # 2D Array (Matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\nMatrix Shape: {matrix.shape}")
    print(f"Transpose:\n{matrix.T}")

def pandas_basics():
    """Demonstrates basic Pandas Series and DataFrame."""
    print("\n--- Pandas Basics ---")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    
    print("\nFiltering (Age > 28):")
    filtered_df = df[df['Age'] > 28]
    print(filtered_df)

if __name__ == "__main__":
    numpy_basics()
    pandas_basics()
