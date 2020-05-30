"""
There are some data D which are collected from a device.
D = {(0, 0.5), (1, 2.0), (2, 1.0), (3, 1.5), (4, 7.5)}
Your task is to write a program that fits a straight line to those data.
"""

from matplotlib import pyplot as plt

D = [(0, 0.5), (1, 2.0), (2, 1.0), (3, 1.5), (4, 7.5)]
a, b = map(float, input('input a, b : ').split())

x = []
y = []
def compute_error(a, b, y):
    fx = []
    e = 0

    for i in range(len(D)):
        x.append(D[i][0])
        y.append(D[i][1])
        fx.append(a*x[i] + b)
        e += (a*x[i] + b - y[i])**2

    print('error e :', round(e, 2))

    plt.plot(x, y)
    plt.plot(x, fx)
    plt.legend(['D', 'f(x)'])
    plt.show()

compute_error(a, b, y)