"""
Compute the equation.

sinh(x) = 1/2(e^x - e^-x)
"""

import math

x = int(input('input x : '))
print('sinh({}) : {}'.format(x, math.sinh(x)))
print('1/2(e^{} - e^-{}) : {}'.format(x, x, 0.5*(math.exp(x) - math.exp(-x))))