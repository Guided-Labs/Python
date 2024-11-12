## Searching NumPy Arrays

import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Find the index of the element that equals 4
search_result= np.where(array_1d == 4)

print(f"Index of the element that equals 4:  {search_result}")