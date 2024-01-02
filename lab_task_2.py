import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import sin ,cos, pi
from utils import revlinspace


X, Y = 0, 1
R = 1.5

data = [[], []]


def update_circle(frame):
    ф = np.arange(0, 2*pi, .01)
    circle.set_data(
        [frame**2 * cos(ф)],
        [frame**2 * sin(ф)]
    )


figure, ax = plt.subplots()

circle, = plt.plot([], [], "r")
ax.set_xlim(-2*pi, 2*pi)
ax.set_ylim(-2*pi, 2*pi)

circle_animation = FuncAnimation(
    figure,
    update_circle,
    frames=revlinspace(-R, R, 150),
    interval=10
)

plt.axis("equal")
plt.show()