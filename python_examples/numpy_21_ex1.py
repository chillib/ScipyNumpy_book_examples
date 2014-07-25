import timeit
import numpy as np

# Create an array with 10^7 elements.
arr = np.arange(1e7)

# Converting ndarray to list
larr = arr.tolist()

# Lists cannot by default broadcast,
# so a function is coded to emulate
# what an ndarray can do.


def list_times(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val * scalar
    return alist

# Number of tries
N = 10


# We are not using IPython's magic timeit command here. This enables you to 
# run the script in as a script.
# NumPy array broadcasting
time1 = timeit.timeit('arr * 1.1', 'from __main__ import arr', number=N) / N
print time1

# More closely equivalent to what is being done in example above:
# return new array where all values are multiplied by scalar, leaving orignal unchanged
time2a = timeit.timeit('[a * 1.1 for a in larr]', 
	'from __main__ import larr', number=N) / N
print time2a

# List and custom function for broadcasting
time2 = timeit.timeit('list_times(larr, 1.1)', 
	'from __main__ import list_times, larr', number=N) / N
print time2


print time2a/time1, time2/time1, "times slower"
