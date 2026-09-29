import numpy as np

prices = np.array([80, 120, 200, 150, 90, 130, 100, 60, 110, 75, 220, 250])

print("Original array:")
print(prices)

ravel_result = prices.ravel()

print("Using ravels:")
print(ravel_result)

flatten_result = prices.flatten()

print("Using flatten:")
print(flatten_result)

resize_results = np.resize(prices, (3, 4))
print("Using resize:")
print(resize_results)