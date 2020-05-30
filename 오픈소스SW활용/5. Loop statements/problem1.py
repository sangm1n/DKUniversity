"""
Write a program that takes a positive integer N as input and draws N random integers in the interval [1, 6]
(both ends inclusive). N increase by 10 to 100. Answer the following questions.
"""

import numpy as np
from matplotlib import pyplot as plt

N = int(input('input N : '))

idx = 1
for step in range(10, N+1, 10):
    count = [0 for x in range(8)]
    base = [x for x in range(8)]
    rand = [np.random.randint(1, 7) for _ in range(step)]

    for i in range(step):
        for j in range(step):
            if rand[j] == i:
                count[i] += 1

    plt.subplot(2, 5, idx)
    plt.bar(base, count, width=0.5, color='r', edgecolor='black')
    plt.title('N = %d' % step)
    plt.xlabel('number')
    plt.ylabel('count')
    idx += 1

plt.show()



