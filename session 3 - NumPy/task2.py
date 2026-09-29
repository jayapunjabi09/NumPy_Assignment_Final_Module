import numpy as np

steps = np.array([[3000, 4000],[5000, 6000],[7000, 8000],[6500, 8000],[8000,7500]])
print("Original array:")
print(steps)

print("Original shape:", steps.shape)

one_d = steps.reshape(-1)
print("1D array:")
print(one_d)
print("1D shape:", one_d.shape)

two_d = one_d.reshape(5, 2)
print("Back to 2D")
print(two_d)
print("2D shape:", two_d.shape)