import numpy as np

ratings = np.array([4.5, 3.8, np.nan, 4.2, np.nan, 3.9, 5.0])

missing_count = np.sum(np.isnan(ratings))

print("Missing Ratings:", missing_count)