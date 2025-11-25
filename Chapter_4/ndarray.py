import numpy as np

# Let's follow the book, but use different values.
# We'll follow the explanation from the book, so
# all credits due, for the meta-explanation, to
# Wes McKinney

# The np.random module inside NumPy provides a tool
# to generate pseudo random numbers.
# We can control the randomness using a seed,
# with the seed method np.random.seed(seed)
np.random.seed(232534)
data = np.random.randn(2, 3)
# So if we print the data, it'll come like this:
print(*data, "\n")
# The asterisk unpacks the elements of the list
# With the seed, it'll always give us the same result.
# It's useful to replicate results among other peers.

# With NumPy we can simply do data * 100
# Instead of the python longer method of
# list comprehension.
data *= 100
print(*data, "\n")

# We can also check the shape, or the matrix value, being 2x3
print("Shape", data.shape, "\n")
# Or it's type. dtype shows the datatype of an object. In this case,
# the datatype of data.
print("Type", data.dtype)
