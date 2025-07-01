"""Basic NumPy usage example for beginners"""

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", array_1d)

# Create a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", array_2d)

# Array attributes
print("Shape of array_2d:", array_2d.shape)
print("Data type of array_1d:", array_1d.dtype)

# Basic operations
sum_result = array_1d + 10  # add 10 to each element
print("array_1d + 10:", sum_result)

product_result = array_1d * 2  # multiply each element by 2
print("array_1d * 2:", product_result)

# Element-wise operations between arrays
array_b = np.array([10, 20, 30, 40, 50])
combined = array_1d + array_b
print("array_1d + array_b:", combined)

# Compute the mean of the array
mean_val = array_1d.mean()
print("Mean of array_1d:", mean_val)

# Reshape the array
reshaped = np.reshape(array_1d, (5, 1))
print("Reshaped array_1d to 5x1:\n", reshaped)

# Creating a range of numbers
range_arr = np.arange(0, 10, 2)  # 0 to 8 stepping by 2
print("np.arange(0, 10, 2):", range_arr)

# Using linspace for evenly spaced numbers
linspace_arr = np.linspace(0, 1, 5)
print("np.linspace(0, 1, 5):", linspace_arr)
