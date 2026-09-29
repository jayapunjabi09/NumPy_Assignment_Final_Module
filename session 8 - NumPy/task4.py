import numpy as np

views = np.array([1000, 2000, np.nan, 5000, np.inf, 3000])

max_finite = np.max(views[np.isfinite(views)])

views[np.isnan(views)] = 0
views[np.isinf(views)] = max_finite

print("Updated Views:", views)