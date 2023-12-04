#! D:\python-projects\python_chapters\numpy_env\Scripts\python.exe

import numpy as np

np1 = np.array([0, 1, 2, 3, 4, -5, 6, -7, 8, 9])

# Find positive or negative
print(np.sign(np1))

# Filter only value greater than 0
select_result = np.select([np1 > 0], [np1])
filtered_result = select_result[select_result > 0]

# Absolute
print(np.absolute(np1))

# Log
print(np.log(filtered_result))

print(np1[np.where(np1 > 0)])
