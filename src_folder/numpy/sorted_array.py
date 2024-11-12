## Sorting NumPy Arrays

import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# Create a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# Sorting a 1D array
sorted_array = np.sort(array_1d)
print(f"Sorted 1D Array: {sorted_array}")

# Sorting a 2D array
sorted_2d_array = np.sort(array_2d, axis=1)  # Sort each row
print(f"Sorted 2D Array by Rows:\n{sorted_2d_array}")