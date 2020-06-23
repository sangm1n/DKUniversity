from math import pi
from math import sqrt

class SQUARE:
    def __init__(self, shape, type):
        self.shape = shape
        self.type = type

    def square(self, s):
        parameter = 4*s
        area = s**2
        return [parameter, area]

    def rectangle(self, a, b):
        parameter = 2*a + 2*b
        area = a*b
        return [parameter, area]

    def parallelogram(self, a, b, h):
        parameter = 2*a + 2*b
        area = b*h
        return [parameter, area]

    def trapezoid(self, a, b, c, d, h):
        parameter = a + b + c + d
        area = h*(a+b)/2
        return [parameter, area]

    def rectangularBox(self, a, b, c):
        area = 2*a*b + 2*a*c + 2*b*c
        volume = a*b*c
        return [area, volume]

    def cube(self, l):
        area = 6*l*l
        volume = l**3
        return [area, volume]


class CIRCLE:
    def __init__(self, shape, type):
        self.shape = shape
        self.type = type

    def circle(self, r):
        parameter = 2*pi*r
        area = round(pi*r*r, 2)
        return [parameter, area]

    def circularSector(self, r, seta):
        length = round(pi*r*seta/180, 2)
        area = round(pi*r*r*seta/360, 2)
        return [length, area]

    def circularRing(self, r, R):
        area = round(pi * (R**2 - r**2), 2)
        return area

    def sphere(self, r):
        surface = round(4*pi*r**2, 2)
        volume = round(4*pi*r**3/3, 2)
        return [surface, volume]

    def cylinder(self, r, h):
        area = round(2*pi*r * (r+h), 2)
        volume = round(pi*r*r*h, 2)
        return [area, volume]

class TRIANGLE:
    def __init__(self, shape, type):
        self.shape = shape
        self.type = type

    def triangle(self, a, b, c, h):
        parameter = a + b + c
        area = 0.5*b*h
        return [parameter, area]

    def pythagorean(self, a, b):
        theorem = round(sqrt(a**2 + b**2), 2)
        return theorem

    def rightCircularCone(self, r, h, s):
        area = round(pi*r*r + pi*r*s, 2)
        surface = round(sqrt(r**2 + h**2), 2)
        volume = round(1/3 * pi*r*r*h, 2)
        return [area, surface, volume]

    def frustumCone(self, r, h, R):
        volume = round(1/3 * pi*h * (r**2 + r*R + R**2), 2)
        return volume