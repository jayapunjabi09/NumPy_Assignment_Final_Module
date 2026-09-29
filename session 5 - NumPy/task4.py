import numpy as np

ratings = np.random.uniform(1, 5, 10)

print("Original Ratings:", ratings)
print("Rounded Ratings:", np.round(ratings))
print("Floor Ratings:", np.floor(ratings))
print("Ceiling Ratings:", np.ceil(ratings))