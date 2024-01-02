import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import pi, sin, cos
from utils import revlinspace


X, Y = 0, 1
R = .06

cycloid_data = [[], []]
astroid_data = [[], []]


def cycloid_update(frame):
    cycloid_data[X].append(2 * R * (frame - sin(frame)))
    cycloid_data[Y].append(2 * R * (frame - cos(frame)))

    cycloid.set_data(cycloid_data)


def astroid_update(frame):
    astroid_data[X].append(5 * R * cos(frame)**3)
    astroid_data[Y].append(5 * R * sin(frame)**3)

    astroid.set_data(astroid_data)


figure, ax = plt.subplots()

cycloid, = plt.plot([], [], "b")
astroid, = plt.plot([], [], "g")

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)


cycloid_animation = FuncAnimation(
    figure,
    cycloid_update,
    frames=revlinspace(-4 * pi, 4 * pi, 100),
    interval=10
)

astroid_animation = FuncAnimation(
    figure,
    astroid_update,
    frames=np.linspace(0, 2 * pi, 100),
    interval=10
)

plt.axis("equal")
plt.show()