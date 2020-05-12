import math

class sphere:
    def __init__(self, r):
        self.r = r
    def surface(self):
        return round(4 * math.pi * self.r**2, 2)
    def volume(self):
        return round(4 * math.pi * self.r**3 / 3, 2)

class rectangular_box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        return round(2*self.a*self.b + 2*self.a*self.c + 2*self.b*self.c, 2)
    def volume(self):
        return round(self.a * self.b * self.c, 2)

class circular_cone:
    def __init__(self, r, h, s):
        self.r = r
        self.h = h
        self.s = s
    def area(self):
        return round(math.pi * self.r**2 + math.pi * self.r * self.s, 2)
    def surface(self):
        return round(math.sqrt(self.r**2 + self.h**2), 2)
    def volume(self):
        return round(1/3 * math.pi * self.r**2 * self.h, 2)

class cube:
    def __init__(self, l):
        self.l = l
    def area(self):
        return round(6 * self.l**2, 2)
    def volume(self):
        return round(self.l**3, 2)

class cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h
    def area(self):
        return round(2 * math.pi * self.r * (self.r + self.h), 2)
    def volume(self):
        return round(math.pi * self.r**2 * self.h, 2)

class frustum_cone:
    def __init__(self, r, h, R):
        self.r = r
        self.h = h
        self.R = R
    def volume(self):
        return round(1/3 * math.pi * self.h * (self.r**2 + self.r*self.R + self.R**2), 2)