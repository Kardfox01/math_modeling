import matplotlib.pyplot as plt
import numpy as np


def parabola(a=-10, b=10, N=100):
    x = np.linspace(a, b, N)
    y = x**2

    plt.plot(x, y)
    plt.show()

parabola()