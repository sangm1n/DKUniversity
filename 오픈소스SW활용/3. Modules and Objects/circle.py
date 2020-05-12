import math

class circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r**2

class circular_sector:
    def __init__(self, r, seta):
        self.r = r
        self.seta = seta
    def length(self):
        return math.pi * self.r * self.seta/180
    def area(self):
        return math.pi * self.r**2 * self.seta/360

class circular_ring:
    def __init__(self, r, R):
        self.r = r
        self.R = R
    def area(self):
        return math.pi * (self.R**2 - self.r**2)