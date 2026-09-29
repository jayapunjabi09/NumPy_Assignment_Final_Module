import numpy as np

ratings = np.array([3.8, 4.7, 4.1, 3.9, 4.8, 4.3, 3.6, 4.9, 4.0, 3.7, 4.5, 4.0, 3.5, 5.0, 4.2])

print("Original 1D ratings:")
print(ratings)

reshaped = ratings.reshape(3, 5)
print("3 x 5 array:")
print(reshaped)

flattened = reshaped.flatten()
print("Back to 1D")
print(flattened)