import numpy as np
scores = np.array([
    [45, 60, 70, 80, 90],
    [30, 50, 65, 75, 85],
    [40, 55, 60, 70, 95]])

print("Scores of all players in matches 2 to 4:")
print(scores[:, 1:4])