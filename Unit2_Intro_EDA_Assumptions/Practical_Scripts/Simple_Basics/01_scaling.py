
import numpy as np

# 1. Scaling vs Normalization
arr = np.array([10, 20, 30, 40, 50])

# Min-Max Scaling (0 to 1)
min_val = np.min(arr)
max_val = np.max(arr)
scaled = (arr - min_val) / (max_val - min_val)
print(f"Scaled Array (Min-Max): {scaled}")

# Z-Score Normalization (Mean=0, Std=1)
mean_val = np.mean(arr)
std_val = np.std(arr)
normalized = (arr - mean_val) / std_val
print(f"Normalized Array (Z-Score): {normalized}")
print(f"Mean of Z-Scores: {np.mean(normalized):.2f}")
