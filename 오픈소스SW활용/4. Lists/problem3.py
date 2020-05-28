"""
Up through history, great minds have developed different computational schemes for the number PI.
There are two schemes: one by Leibniz (1646-1716) and one by Euler (1707 - 1783).
"""

import math

N = int(input('input N : '))
leibniz = euler = 0

for i in range(N):
    leibniz += (8 / (4*i+1) / (4*i+3))

for i in range(1, N):
    euler += (6 / i**2)
euler = math.sqrt(euler)

print('math.pi :', round(math.pi, 4))
print('Leibniz pi :', round(leibniz, 4))
print('Euler pi :', round(euler, 4))