"""
Practice how variables refer to Python objects.
Test each code line to understand the results of Python objects.
"""

a = -11
b = 11
c = 9.0
d = b / a
e = c / a
s = 'b / a = %g' % (b / a)

print('a : {}'.format(type(a)))
print('b : {}'.format(type(b)))
print('c : {}'.format(type(c)))
print('d : {}'.format(type(d)))
print('e : {}'.format(type(e)))
print('s : {}'.format(type(s)))