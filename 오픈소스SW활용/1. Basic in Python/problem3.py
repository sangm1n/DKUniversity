"""
Design a program to compute the height of a ball in vertical motion.

h(t) = v0 * (-1/2) * g * t^2
"""

v0 = 100        # initial velocity
g = 32          # acceleration of gravity (32 feet/sec)
t = 3.2         # time
d = 50          # initial vertical position

# compute the vertical position
h = -0.5 * g * t**2 + v0 * t + d
print(round(h, 2), 'feet')