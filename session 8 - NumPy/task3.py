import numpy as np

prices = np.array([50, 200, 500, 1200, 1500, 800, 90])

clipped_prices = np.clip(prices, 100, 1000)

print("Original Prices:", prices)
print("Clipped Prices:", clipped_prices)