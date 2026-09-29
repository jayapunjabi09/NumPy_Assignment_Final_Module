import numpy as np

product_ids = np.array([
    101, 102, 103, 104, 105, 106,
    107, 108, 109, 110, 111, 112])

parts = np.array_split(product_ids, 3)

for part in parts:
    print("Product IDs:", part)
    print("Shape:", part.shape)