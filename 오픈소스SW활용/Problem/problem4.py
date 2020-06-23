"""
Based on object-oriented programming,
design and implement each class for geometry objects on the next page.
"""

import geometry as geo

print('''
========== Geometry Calculation ===================
=== < shape > ========== < type > =================
=== square ============= parameter / area =========
=== rectangle ========== parameter / area =========
=== circle ============= parameter / area =========
=== triangle =========== parameter / area =========
=== parallelogram ====== parameter / area =========
=== circularSector ===== length / area ============
=== pythagorean ======== theorem ==================
=== circularRing ======= area =====================
=== sphere ============= surface / volume =========
=== trapezoid ========== parameter / area =========
=== rectangularBox ===== area / volume ============
=== cube =============== area / volume ============
=== cylinder =========== area / volume ============
=== rightCircularCone == area / surface / volume ==
=== frustumCone ======== volume ===================
''')

shape, type = map(str, input('input shape and type : ').split())

if shape == "square":
    s = int(input('input s(side) : '))
    if type == "parameter":
        answer = geo.SQUARE(shape, type).square(s)[0]
    elif type == "area":
        answer = geo.SQUARE(shape, type).square(s)[1]

elif shape == "rectangle":
    a, b = map(int, input('input a(width), b(height) : ').split())
    if type == "parameter":
        answer = geo.SQUARE(shape, type).rectangle(a, b)[0]
    elif type == "area":
        answer = geo.SQUARE(shape, type).rectangle(a, b)[1]

elif shape == "parallelogram":
    a, b, h = map(int, input('input a, b, h(height) : ').split())
    if type == "parameter":
        answer = geo.SQUARE(shape, type).parallelogram(a, b, h)[0]
    elif type == "area":
        answer = geo.SQUARE(shape, type).parallelogram(a, b, h)[1]

elif shape == "trapezoid":
    a, b, c, d, h = map(int, input('input a, b, c, d, h(height) : ').split())
    if type == "parameter":
        answer = geo.SQUARE(shape, type).trapezoid(a, b, c, d, h)[0]
    elif type == "area":
        answer = geo.SQUARE(shape, type).trapezoid(a, b, c, d, h)[1]

elif shape == "rectangularBox":
    a, b, c = map(int, input('input a, b, c : ').split())
    if type == "area":
        answer = geo.SQUARE(shape, type).rectangularBox(a, b, c)[0]
    elif type == "volume":
        answer = geo.SQUARE(shape, type).rectangularBox(a, b, c)[1]

elif shape == "cube":
    l = int(input('input l(length) : '))
    if type == "area":
        answer = geo.SQUARE(shape, type).cube(l)[0]
    elif type == "volume":
        answer = geo.SQUARE(shape, type).cube(l)[1]

elif shape == "circle":
    r = int(input('input r(radius) : '))
    if type == "parameter":
        answer = geo.CIRCLE(shape, type).circle(r)[0]
    elif type == "area":
        answer = geo.CIRCLE(shape, type).circle(r)[1]

elif shape == "circularSector":
    r, seta = map(int, input('input r, seta : ').split())
    if type == "length":
        answer = geo.CIRCLE(shape, type).circularSector(r, seta)[0]
    elif type == "area":
        answer = geo.CIRCLE(shape, type).circularSector(r, seta)[1]

elif shape == "circularRing":
    r, R = map(int, input('input r(inner), R(outer) : ').split())
    if type == "area":
        answer = geo.CIRCLE(shape, type).circularRing(r, R)

elif shape == "sphere":
    r = int(input('input r : '))
    if type == "surface":
        answer = geo.CIRCLE(shape, type).sphere(r)[0]
    elif type == "volume":
        answer = geo.CIRCLE(shape, type).sphere(r)[1]

elif shape == "cylinder":
    r, h = map(int, input('input r, h(height) : ').split())
    if type == "area":
        answer = geo.CIRCLE(shape, type).cylinder(r, h)[0]
    elif type == "volume":
        answer = geo.CIRCLE(shape, type).cylinder(r, h)[1]

elif shape == "triangle":
    a, b, c, h = map(int, input('input a, b, c, h(height) : ').split())
    if type == "parameter":
        answer = geo.TRIANGLE(shape, type).triangle(a, b, c, h)[0]
    elif type == "area":
        answer = geo.TRIANGLE(shape, type).triangle(a, b, c, h)[1]

elif shape == "pythagorean":
    a, b = map(int, input('input a, b : ').split())
    if type == "theorem":
        answer = geo.TRIANGLE(shape, type).pythagorean(a, b)

elif shape == "rightCircularCone":
    r, h, s = map(int, input('input r, h(height), s(slant height) : ').split())
    if type == "area":
        answer = geo.TRIANGLE(shape, type).rightCircularCone(r, h, s)[0]
    elif type == "surface":
        answer = geo.TRIANGLE(shape, type).rightCircularCone(r, h, s)[1]
    elif type == "volume":
        answer = geo.TRIANGLE(shape, type).rightCircularCone(r, h, s)[2]

elif shape == "frustumCone":
    r, h, R = map(int, input('input r(small), h, R(large) : ').split())
    if type == "volume":
        answer = geo.TRIANGLE(shape, type).frustumCone(r, h, R)


print('the result is', answer)
