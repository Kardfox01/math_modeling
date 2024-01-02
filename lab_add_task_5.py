import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import pi
from utils import revlinspace


X, Y = 0, 1
R = .06


def point_cycloid_update(frame):
    point_cycloid.set_data(
        [2 * R * (frame - np.sin(frame))],
        [2 * R * (frame - np.cos(frame))]
    )


def point_asteroid_update(frame):
    point_asteroid.set_data(
        [5 * R * np.cos(frame)**3],
        [5 * R * np.sin(frame)**3]
    )


figure, (ax1, ax2) = plt.subplots(2, 1)

cycloid, = ax1.plot(
    [2 * R * (frame - np.sin(frame)) for frame in np.linspace(-4*pi, 4*pi, 100)],
    [2 * R * (frame - np.cos(frame)) for frame in np.linspace(-4*pi, 4*pi, 100)],
    "b"
)

astroid, = ax2.plot(
    [5 * R * np.cos(frame)**3 for frame in np.linspace(0, 2 * pi, 100)],
    [5 * R * np.sin(frame)**3 for frame in np.linspace(0, 2 * pi, 100)],
    "g"
)

point_cycloid,  = ax1.plot([], [], "or")
point_asteroid, = ax2.plot([], [], "or")

ax1.set_xlim(-3, 3)
ax2.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax2.set_ylim(-3, 3)

point_cycloid_animation = FuncAnimation(
    figure,
    point_cycloid_update,
    frames=revlinspace(-4 * pi, 4 * pi, 100),
    interval=10
)

point_astroid_animation = FuncAnimation(
    figure,
    point_asteroid_update,
    frames=np.linspace(0, 2 * pi, 100),
    interval=10
)

plt.axis("equal")
plt.show()