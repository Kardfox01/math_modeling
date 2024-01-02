import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from itertools import tee
from numpy import sin, cos


X, Y = 0, 1

square_data = [
    np.array([-5, -5, 5, 5, -5]),
    np.array([-5, 5, 5, -5, -5])
]


def square_update(frame):
    square.set_data(
        square_data[X]*cos(frame) - square_data[Y]*sin(frame),
        square_data[Y]*cos(frame) + square_data[X]*sin(frame)
    )


figure, ax = plt.subplots()

square, = plt.plot([], [], "r")

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

square_animation = FuncAnimation(
    figure,
    square_update,
    frames=np.linspace(-5, 5, 1000),
    interval=10
)

plt.axis("equal")
plt.show()