import numpy as np

visitors = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])

print("Total Visitors:", np.sum(visitors))
print("Average Visitors:", np.mean(visitors))
print("75th Percentile:", np.percentile(visitors, 75))
print("Variance:", np.var(visitors))
print("Cumulative Visitors:", np.cumsum(visitors))