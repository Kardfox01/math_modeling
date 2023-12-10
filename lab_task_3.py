import matplotlib.pyplot as plt
import numpy as np


def circle(a=-10, b=10, N=100):
    x = np.linspace(a, b, N)
    y = x.copy()

    X, Y = np.meshgrid(x, y)
    f = X**2 + Y**2 - 10**2

    plt.contour(X, Y, f, levels=(0,))
    plt.axis("equal")
    plt.show()

circle()