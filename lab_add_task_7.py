import matplotlib.pyplot as plt
import numpy as np


def f(x):
    if x < a:
        return a**2
    elif x > b:
        return b**2
    else:
        return x**2

a = 0
b = 10

x = np.arange(-9, 20, 1)
y = list(map(f, x))

plt.plot(x, y)
plt.show()