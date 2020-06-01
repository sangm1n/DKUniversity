"""
Develop a function that finds the minimum or maximum value in a list, depending on the caller’s request.
"""

import numpy as np

arr = [np.random.randint(100) for x in range(50)]

min_value = arr[0]
idx = 0
for i in range(len(arr)):
    if arr[i] <= min_value:
        min_value = arr[i]
        idx = i

def min_index(arr):
    return (min(arr), arr.index(min(arr)))

def max_index(arr):
    return (max(arr), arr.index(max(arr)))

print('(min value, min index) using loop :', (min_value, idx))
print('(min value, min index) using function :', min_index(arr))
print('(max value, max index) using function :', max_index(arr))