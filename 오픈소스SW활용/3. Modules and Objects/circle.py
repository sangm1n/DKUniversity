import math

class circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return round(2 * math.pi * self.r, 2)
    def area(self):
        return round(math.pi * self.r**2, 2)

class circular_sector:
    def __init__(self, r, seta):
        self.r = r
        self.seta = seta
    def length(self):
        return round(math.pi * self.r * self.seta/180, 2)
    def area(self):
        return round(math.pi * self.r**2 * self.seta/360, 2)

class circular_ring:
    def __init__(self, r, R):
        self.r = r
        self.R = R
    def area(self):
        return round(math.pi * (self.R**2 - self.r**2), 2)