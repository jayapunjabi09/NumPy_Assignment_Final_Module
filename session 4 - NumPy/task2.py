import numpy as np

prices = np.array([200, 250, 150, 300, 350])
discounts = np.array([20, 30, 15, 100, 70])

final_price = prices - discounts

print("Original Prices:", prices)
print("Discounts:", discounts)
print("Final prices:", final_price)