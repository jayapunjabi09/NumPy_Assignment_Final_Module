import numpy as np

numbers = np.array([10, 15, 22, 33, 40, 51, 60, 71])

even_indices = np.where(numbers % 2 == 0)

print("Even Numbers:", numbers[even_indices])
print("Indices of Even Numbers:", even_indices[0])