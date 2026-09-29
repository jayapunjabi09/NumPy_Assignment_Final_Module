import numpy as np

views = np.array([1000, 2000, 3000, 4000, 5000])

view_array = views.view()
copy_array = views.copy()

view_array[0] = 9999
copy_array[0] = 8888

print("Original Array:", views)
print("View Array:", view_array)
print("Copy Array:", copy_array)