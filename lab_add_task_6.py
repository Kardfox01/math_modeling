import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import pi


X, Y = 0, 1
R = .06


def sin1_update(frame):
    x = np.linspace(-4*pi, 4*pi, 500)
    y = 2*np.sin(x*3)

    sin1.set_data(x + frame, y)


def sin2_update(frame):
    x = np.linspace(-4*pi, 4*pi, 500)
    y = 3*np.sin(x*.5)

    sin2.set_data(x - frame, y)


figure, ax = plt.subplots()

sin1, = plt.plot([], [], "g")
sin2, = plt.plot([], [], "b")

ax.set_xlim(-2*pi, 2*pi)
ax.set_ylim(-3, 3)

sin1_animation = FuncAnimation(
    figure,
    sin1_update,
    frames=np.linspace(-2*pi, 2*pi, 100),
    interval=10
)

sin2_animation = FuncAnimation(
    figure,
    sin2_update,
    frames=np.linspace(-2*pi, 2*pi, 100),
    interval=10
)

# plt.axis("equal")
plt.show()