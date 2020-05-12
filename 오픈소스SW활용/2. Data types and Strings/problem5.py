"""
Throw a ball with velocity v0, at an angle θ with the horizontal,
from the point(x = 0; y = y0). The trajectory of the all is a parabola.
We neglect air resistance.
"""

import math

v0 = float(input('input velocity : '))
seta = float(input('input angle : '))
y0 = float(input('input y0 : '))

x = 0
g = 9.81

y = x*math.tan(seta) - (g*pow(x, 2)) / (2*pow(v0, 2)*pow(math.cos(seta), 2)) + y0

print('y : %.2f' % y)