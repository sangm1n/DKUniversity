"""
Design and implement a function that takes a set of integers as its input argument
and returns a set of those integers that occur two or more times in the list.
The input integers are generated randomly in [1, 20].
"""

import numpy as np

print('making random 20 number from 1 to 20 ...')
arr = [np.random.randint(1, 21) for _ in range(20)]
print('random 20 number :', arr)
temp = [0 for _ in range(20)]

def duplicate(arr):
    for i in range(20):
        for j in range(20):
            if arr[j] - 1 == i:
                temp[i] += 1

    result = []
    for i in range(20):
        if temp[i] >= 2:
            result.append(i + 1)

    return result

print('\nintegers that occur two or more times :', duplicate(arr))