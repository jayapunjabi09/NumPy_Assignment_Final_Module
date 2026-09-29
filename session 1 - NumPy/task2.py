import sys
import numpy as np

python_list = list(range(1, 1001))
numpy_array = np.arange(1,1001)

list_memory = sys.getsizeof(python_list)
array_memory = numpy_array.nbytes

print("Memory used by python list:", list_memory, "bytes")
print("Memory used by NumPy array:", array_memory, "bytes")

