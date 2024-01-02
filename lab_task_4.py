import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


X, Y = 0, 1

C, D = .4, .2
fractal_data = [[.1], [.1]]


def fractal_update(frame):
    fractal_data[X].append(
        fractal_data[X][-1]**2 - fractal_data[Y][-1]**2 + C
    )
    fractal_data[Y].append(
        2*fractal_data[X][-1]*fractal_data[Y][-1] + D
    )

    fractal.set_data(fractal_data)


figure, ax = plt.subplots()

fractal, = plt.plot([], [], "r")

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

fractal_animation = FuncAnimation(
    figure,
    fractal_update,
    frames=10,
    interval=200
)

plt.axis("equal")
plt.show()