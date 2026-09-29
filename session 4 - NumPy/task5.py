import numpy as np

steps = np.array([4000, 5000, 6000, 5500, 45000, 6500, 7000])

new_steps = steps + 50

total_steps = np.sum(new_steps)

print("Original steps:", steps)
print("Steps after adding 50:", new_steps)
print("Total steps:", total_steps)