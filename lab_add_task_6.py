import matplotlib.pyplot as plt
import numpy as np


def polar_ellipse(p, ε, ф):
    return p / (1 + ε*np.cos(ф))

ε = .9
p = 1
ф = np.arange(0, 2*np.pi, .01)

plt.polar(ф, polar_ellipse(p, ε, ф))
plt.show()