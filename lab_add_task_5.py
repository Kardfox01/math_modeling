import matplotlib.pyplot as plt
import numpy as np


def fx(t):
    return A * np.sin(a*t + δ)

def fy(t):
    return B * np.sin(b*t)

def points():
    t = np.arange(-10, 10, .1)
    x = list(map(fx, t))
    y = list(map(fy, t))

    return x, y

A = 1
a = 1
B = 10
b = 2
δ = np.pi / 2

plt.plot(*points())
plt.show()

A = 1
a = 1
B = 10
b = 4
δ = np.pi / 2

plt.plot(*points())
plt.show()

A = 1
a = 1
B = 10
b = 0.5
δ = np.pi / 12

plt.plot(*points())
plt.show()