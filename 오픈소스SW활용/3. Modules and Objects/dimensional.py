import math

class sphere:
    def __init__(self, r):
        self.r = r
    def surface(self):
        return 4 * math.pi * self.r**2
    def volume(self):
        return 4 * math.pi * self.r**3 / 3

class rectangular_box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        return 2*self.a*self.b + 2*self.a*self.c + 2*self.b*self.c
    def volume(self):
        return self.a * self.b * self.c

class circular_cone:
    def __init__(self, r, h, s):
        self.r = r
        self.h = h
        self.s = s
    def area(self):
        return math.pi * self.r**2 + math.pi * self.r * self.s
    def surface(self):
        return math.sqrt(self.r**2 + self.h**2)
    def volume(self):
        return 1/3 * math.pi * self.r**2 * self.h

class cube:
    def __init__(self, l):
        self.l = l
    def area(self):
        return 6 * self.l**2
    def volume(self):
        return self.l**3

class cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h
    def area(self):
        return 2 * math.pi * self.r * (self.r + self.h)
    def volume(self):
        return math.pi * self.r**2 * self.h

class frustum_cone:
    def __init__(self, r, h, R):
        self.r = r
        self.h = h
        self.R = R
    def volume(self):
        return 1/3 * math.pi * self.h * (self.r**2 + self.r*self.R + self.R**2)