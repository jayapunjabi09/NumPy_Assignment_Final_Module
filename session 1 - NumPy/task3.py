import time
import numpy as np

python_list = list(range(10000))
numpy_array = np.arange(10000)

start = time.time()
list_result = [x + 5 for x in python_list]
list_time = time.time() - start

start = time.time()
array_result = numpy_array + 5
array_time = time.time() - start

print("Python list time:", list_time)
print("NumPy array time:", array_time)