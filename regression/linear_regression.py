'''
Problem - Linear Regression
Class - Regression
Category - Supervised Learning
Author - Siddhant Nautiyal
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5]) #hours studies
y = np.array([2, 4, 5, 4, 5]) #marks scored
n = len(x)

numerator = n*np.sum(x*y) - np.sum(x)*np.sum(y)
denominator = n*np.sum(x**2) - (np.sum(x)**2)

#slope(m) and intercept(b)
slope = numerator / denominator
intercept = (np.sum(y) - slope * np.sum(x)) / n

print(f"Slope (m): {slope:.2f}")
print(f"Intercept (b): {intercept:.2f}")

# Hypothesis
y_pred = slope * x + intercept

# Visualization
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
