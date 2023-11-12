import numpy as np

# Zeros
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slice between index
print(np1[1:4])

# Slice to end
print(np1[5:])

# Slice reverse
print(np1[-2:-1])

# Slice and steps
print(np1[1:5:2])