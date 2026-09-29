import numpy as np

prices = np.array([250, 700, 450, 1200, 800, 300, 1500])

result = prices[prices > 500]
print("Prices Greater Than 500:", result)