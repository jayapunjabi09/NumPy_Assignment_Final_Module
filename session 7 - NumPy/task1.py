import numpy as np

zomato = np.array([4.2, 3.8, 4.5, 4.0, 3.9])
swiggy = np.array([4.1, 4.3, 3.7, 4.6, 4.0])

ratings = np.concatenate((zomato, swiggy))

print("Combined Ratings:", ratings)