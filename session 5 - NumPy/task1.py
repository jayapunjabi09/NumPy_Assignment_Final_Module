import numpy as np

sales1 = np.array([1000, 2000, 3000, 4000, 5000])
sales2 = np.array([500, 1000, 1500, 2000, 2500])

print("Total Sales:", np.add(sales1, sales2))
print("Sales Difference:", np.subtract(sales1, sales2))