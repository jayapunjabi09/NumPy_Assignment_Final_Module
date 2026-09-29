import numpy as np

prices = np.array([500, 1000, 1500, 2000, 2500])

discount = np.multiply(prices, 0.20)
final_prices = np.subtract(prices, discount)

print("Discount:", discount)
print("Final Prices:", final_prices)
print("Total Bill:", np.sum(final_prices))