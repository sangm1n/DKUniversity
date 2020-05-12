"""
There are various geometries.
Design modules to calculate area, perimeter, volume, or surface related to a chosen geometry.
"""

import circle
import triangle
import rectangle
import dimensional

r, R, seta = map(int, input('input r, R, seta : ').split())
a, b, c, d = map(int, input('input a, b, c, d : ').split())
s, h = map(int, input('input s, h : ').split())

c1, c2, c3 = circle.circle(r), circle.circular_sector(r, seta), circle.circular_ring(r, R)
t1, t2 = triangle.triangle(a, b, c, h), triangle.pythagorean(a, b, c)
r1, r2, r3, r4 = rectangle.square(s), rectangle.rectangle(a, b), \
                    rectangle.parallelogram(a, b, h), rectangle.trapezoid(a, b, c, d, h)
d1, d2, d3, d4, d5, d6 = dimensional.sphere(r), dimensional.rectangular_box(a, b, c), \
                            dimensional.cube(s), dimensional.cylinder(r, h), \
                            dimensional.circular_cone(r, h, s), dimensional.frustum_cone(r, h, R)

print(c1.perimeter(), c1.area())
print(c2.length(), c2.area())
print(c3.area())
print(t1.perimeter(), t1.area())
print(t2.hypotenuse())
print(r1.perimeter(), r1.area())
print(r2.perimeter(), r2.area())
print(r3.perimeter(), r3.area())
print(r4.perimeter(), r4.area())
print(d1.surface(), d1.volume())
print(d2.area(), d2.volume())
print(d3.area(), d3.volume())
print(d4.area(), d4.volume())
print(d5.area(), d5.surface(), d5.volume())
print(d6.volume())