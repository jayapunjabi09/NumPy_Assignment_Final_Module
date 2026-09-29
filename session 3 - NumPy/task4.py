import numpy as np

spotify = np.array([[15, 20, 10],[18, 12, 8],[15, 25, 10]])
print("Original playlist:")
print(spotify)

transposed_1 = spotify.T

print("Using .T:")
print(transposed_1)

transposed_2 = np.transpose(spotify)

print("Using np.transpose():")
print(transposed_2)