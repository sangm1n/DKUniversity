"""
Write a program that takes a positive integer N as input and draws N random integers in the interval [1, 6]
(both ends inclusive). N increase by 10 to 100. Answer the following questions.
"""

import numpy as np

N = int(input())
arr = [np.random.randint(1, 7) for _ in range(N)]
print(arr)