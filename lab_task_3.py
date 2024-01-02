import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import pi, e, sin, cos


X, Y = 0, 1

butterfly_data = [[], []]
heart_data = [[], []]


def butterfly_update(frame):
    butterfly_data[X].append(
        20 + sin(frame)*(e**cos(frame) - 2*cos(4*frame) + sin(frame/12)**5)
    )
    butterfly_data[Y].append(
        cos(frame)*(e**cos(frame) - 2*cos(4*frame) + sin(frame/12)**5)
    )

    butterfly.set_data(butterfly_data)


def heart_update(frame):
    heart_data[X].append(
        -20 + 16*sin(frame)**3
    )
    heart_data[Y].append(
        13*cos(frame) - 5*cos(2*frame) - 2*cos(3*frame) - cos(4*frame)
    )

    heart.set_data(heart_data)


figure, ax = plt.subplots()

butterfly, = plt.plot([], [], "r")
heart, = plt.plot([], [], "r")

ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)

butterfly_animation = FuncAnimation(
    figure,
    butterfly_update,
    frames=np.linspace(0, 12*pi, 500),
    interval=10
)

heart_animation = FuncAnimation(
    figure,
    heart_update,
    frames=np.linspace(0, 2*pi, 500),
    interval=10
)

plt.axis("equal")
plt.show()