"""
Convert between object types
"""

a = 3
b = float(a)
c = 3.9
d = int(c)
e = round(c)
f = int(round(c))

print('a : {}'.format(type(a)))
print('b : {}'.format(type(b)))
print('c : {}'.format(type(c)))
print('d : {}'.format(type(d)))
print('e : {}'.format(type(e)))
print('f : {}'.format(type(f)))

d = str(c)
e = '-4.1'
f = float(e)

print('d : {}'.format(type(d)))
print('e : {}'.format(type(e)))
print('f : {}'.format(type(f)))