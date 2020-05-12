"""
Given two d-dimensional vectors u and v, the ways to compute their distance are various.
"""

import numpy as np

N = int(input('input N-dimension : '))
u = [np.random.randint(10) for x in range(N)]
v = [np.random.randint(10) for x in range(N)]
print('u vector :', u)
print('v vector :', v)

import euclidean
import manhattan
import hamming
import cosine
import chebyshev

print('Euclidean distance :', euclidean.dist(u, v))
print('Manhattan distance :', manhattan.dist(u, v))
print('Hamming distance :', hamming.dist(u, v))
print('Cosine distance :', cosine.dist(u, v))
print('Chebyshev distance :', chebyshev.dist(u, v))