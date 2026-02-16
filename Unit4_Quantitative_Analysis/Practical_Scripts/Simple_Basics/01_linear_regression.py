
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Create Synthetic Data (Linear Relationship)
np.random.seed(42)
X = np.random.rand(100, 1) * 10 # Hours Studied
y = 2.5 * X + np.random.randn(100, 1) * 2 # Exam Score

# 2. Train Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# 3. Make Predictions
X_test = np.array([[5], [8]])
y_pred = model.predict(X_test)
print(f"Prediction for 5 hours: {y_pred[0][0]:.2f}")
print(f"Prediction for 8 hours: {y_pred[1][0]:.2f}")

# 4. Visualize
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title(f'Hours vs Score (Slope: {model.coef_[0][0]:.2f})')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.savefig('01_linear_regression.png')
print("Plot saved to 01_linear_regression.png")
