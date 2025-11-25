import time
import numpy as np

# Let's create a start time to measure the output
time_start = time.time()

# Let's create a list with np using the .arange() function.
# This will create a array, instead of a range() object, like
# Python would. This is optimized for numerical values
array_np = np.arange(100000)
array_np_2 = array_np * 2


# Let's create an end time.
time_end = time.time()
final_time = time_end - time_start
print(f"Time for NumPY operation:  {final_time:.6f}")

# While doing with range(100000 of python)
time_start = time.time()

# Let's do the same with python, but we'll have to create a list
# comprehension
array = range(100000)
array_2 = [i * 2 for i in array]

# Let's create an end time.
time_end = time.time()
final_time = time_end - time_start
print(f"Time for Python operation:  {final_time:.6f}")

# While doing with range(100000 of python)
time_start = time.time()

# Let's do the same with python, but we'll have to create a list
# comprehension
array = range(100000)
array_2 = []
for i in array:
    array_2.append(i*2)

# Let's create an end time.
time_end = time.time()
final_time = time_end - time_start
print(f"Time for Python operation with append:  {final_time:.6f}")
