import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

loop_result = []

for row in arr:
    new_row = []
    for value in row:
        new_row.append(value * 2)
    loop_result.append(new_row)

print("Using for loop:")
print(loop_result)

vectorized_result = arr * 2
print("Using vectorization:")
print(vectorized_result)