import math

class triangle:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def perimeter(self):
        return round(self.a + self.b + self.c, 2)
    def area(self):
        return round(0.5 * self.b * self.h, 2)

class pythagorean:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def hypotenuse(self):
        return round(math.sqrt(self.a**2 + self.b**2), 2)