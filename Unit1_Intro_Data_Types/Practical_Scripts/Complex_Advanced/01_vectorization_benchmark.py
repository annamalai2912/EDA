
import numpy as np

# 1. Advanced Broadcasting:
# Multiply a (3x4) matrix by a (1x4) vector and a (3x1) vector.
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
vector_1x4 = np.array([10, 100, 1000, 10000])
vector_3x1 = np.array([[0.1], [0.2], [0.3]])

result = (matrix + vector_1x4) * vector_3x1
print("Broadcasting Result:")
print(result)

# 2. Vectorized Optimization
# Often in Data Science, for loops are EXTREMELY slow compared to vectorization.
import time

def slow_loop_calculation(n=1000000):
    # Calculate sum of squares
    start = time.time()
    total = 0
    for i in range(n):
        total += i**2
    end = time.time()
    print(f"Loop Time: {end - start:.5f} seconds")

def fast_vectorized_calculation(n=1000000):
    start = time.time()
    arr = np.arange(n)
    total = np.sum(arr**2)
    end = time.time()
    print(f"Vectorized Time: {end - start:.5f} seconds")

if __name__ == "__main__":
    slow_loop_calculation()
    fast_vectorized_calculation()
