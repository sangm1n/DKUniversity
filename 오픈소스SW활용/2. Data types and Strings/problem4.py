"""
Compute the equation.

sinh(x) = 1/2(e^x - e^-x)
"""

import math

x = int(input('input x : '))
result1 = round(math.sinh(x), 2)
result2 = round(0.5 * (math.exp(x) - math.exp(-x)), 2)

print('sinh({}) : {}'.format(x, result1))
print('1/2(e^{} - e^-{}) : {}'.format(x, x, result2))