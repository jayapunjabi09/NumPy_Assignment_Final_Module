import numpy as np

scores = np.array([210, 180, 195, 220, 205, 175])

indices = np.where(scores > 200)

print("Indices of Scores Above 200:", indices[0])