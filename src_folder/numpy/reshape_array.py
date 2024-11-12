## Reshaping Arrays

import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Reshape 1D array to 2D array
reshaped_array = array_1d.reshape(4, 2)
print(f"Reshaped Array:\n{reshaped_array}")