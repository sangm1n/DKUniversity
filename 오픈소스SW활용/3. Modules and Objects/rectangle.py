class square:
    def __init__(self, s):
        self.s = s
    def perimeter(self):
        return round(4 * self.s, 2)
    def area(self):
        return round(self.s**2, 2)

class rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        return round(2*self.a + 2*self.b, 2)
    def area(self):
        return round(self.a * self.b, 2)

class parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def perimeter(self):
        return round(2*self.a + 2*self.b, 2)
    def area(self):
        return round(self.b * self.h, 2)

class trapezoid:
    def __init__(self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
    def perimeter(self):
        return round(self.a + self.b + self.c + self.d, 2)
    def area(self):
        return round(self.h * (self.a + self.b)/2, 2)